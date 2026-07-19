import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver
from sentence_transformers import CrossEncoder
from langchain_core.tools import tool

from src.tools import calculator, get_time, word_count, reverse_text, get_weather, send_email
from src.guardrails import check_guardrails

class UltimateRerankedAgent:

    def __init__(self, pdf_path='data/documents/attention.pdf', model="llama-3.1-8b-instant", temperature=0):
        print("Initializing ContextForge Framework...")
        
        self.llm = ChatGroq(model=model, temperature=temperature)
        self.embeddings = OllamaEmbeddings(model='nomic-embed-text')
        self.store = {}
        
        print("Loading Reranker...")
        self.reranker = CrossEncoder("BAAI/bge-reranker-base")
        
        persist_dir = "data/chroma_db"
        
        if os.path.exists(persist_dir):
            print("Loading ChromaDB...")
            vectorstore = Chroma(
                persist_directory=persist_dir,
                embedding_function=self.embeddings,
                collection_name="hybrid_agent_knowledge"
            )
        elif os.path.exists(pdf_path):
            print("Processing PDF...")
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()
            splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = splitter.split_documents(docs)
            
            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=self.embeddings,
                persist_directory=persist_dir,
                collection_name="hybrid_agent_knowledge"
            )
            print("ChromaDB created!")
        else:
            vectorstore = None
            print(" No PDF found.")

        if vectorstore:
            self.retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        else:
            self.retriever = None

        @tool
        def query_pdf_document(query: str) -> str:
            """Search PDF document for information"""
            if self.retriever is None:
                return "PDF not available"
            
            try:
                initial_docs = self.retriever.invoke(query)
                if not initial_docs:
                    return "No results found"
                
                pairs = [[query, doc.page_content] for doc in initial_docs]
                scores = self.reranker.predict(pairs)
                
                scored_docs = sorted(zip(scores, initial_docs), key=lambda x: x[0], reverse=True)
                top_doc = scored_docs[0][1]
                
                result = top_doc.page_content[:200]
                return result
                
            except Exception as e:
                return "Error"

        self.tools = [
            get_weather, get_time, reverse_text, calculator, word_count, query_pdf_document,
            send_email
        ]
        
        print("Setting up Database State Storage...")
        self.conn = sqlite3.connect("agent_memory.db", check_same_thread=False)
        self.memory_saver = SqliteSaver(self.conn)
        
        system_prompt = (
            "You are a professional AI assistant with access to specific tools.\n"
            "Available tools: get_weather, get_time, reverse_text, calculator, word_count, query_pdf_document, send_email.\n"
            "IMPORTANT RULES:\n"
            "1. You do NOT have any search tool like brave_search, google_search, or web_search.\n"
            "2. Always provide a complete, natural language response - not just the tool output.\n"
            "3. Format your response professionally with proper sentences.\n"
            "4. For weather: 'The current weather in [city] is [condition] with temperature [temp].'\n"
            "5. For math: 'The result of [expression] is [result].'\n"
            "6. For PDF: Provide a clear explanation based on the document.\n"
            "7. For email: 'Email sent successfully to [recipient].'\n"
            "8. Keep responses concise but complete."
        )
        
        self.agent = create_react_agent(
            model=self.llm,
            tools=self.tools,
            prompt=system_prompt,
            checkpointer=self.memory_saver
        )
        
        self.set_session("default_user")
        print("System Ready!")

    def set_session(self, session_id):
        self.session_id = session_id
        self.config = {
            "configurable": {"thread_id": session_id},
            "recursion_limit": 50
        }

    def get_session_history(self):
        if self.session_id not in self.store:
            self.store[self.session_id] = ChatMessageHistory()
        return self.store[self.session_id]

    def stream_query(self, query):
        if not check_guardrails(query):
            return "\nGuardrail Alert: Request violates safety policies."

        full_response = ""
        try:
            for chunk in self.agent.stream(
                {"messages": [("human", query)]}, 
                config=self.config, 
                stream_mode="values"
            ):
                if "messages" in chunk:
                    latest_message = chunk["messages"][-1]
                    
                    if hasattr(latest_message, "type") and latest_message.type == "ai":
                        if hasattr(latest_message, "content") and latest_message.content:
                            full_response = latest_message.content
            
            if full_response:
                self.get_session_history().add_user_message(query)
                self.get_session_history().add_ai_message(full_response)
                return full_response
            else:
                return "\nNo response generated."

        except Exception as streaming_error:
            return f"\nError: {streaming_error}"

    def show_history(self):
        messages = self.get_session_history().messages
        if not messages:
            return "No history."
        result = f"\n--- History for {self.session_id} ---\n"
        for msg in messages:
            role = "User" if isinstance(msg, HumanMessage) else "AI"
            result += f"{role}: {msg.content}\n"
        result += "------------------------------------------"
        return result

    def clear_memory(self):
        self.store[self.session_id] = ChatMessageHistory()
        return "✅ Memory cleared."

    def show_stats(self):
        msgs = self.get_session_history().messages
        stats = {
            "session": self.session_id,
            "total_messages": len(msgs),
            "user_queries": sum(isinstance(m, HumanMessage) for m in msgs),
            "ai_responses": sum(isinstance(m, AIMessage) for m in msgs),
        }
        return stats

    def close_connection(self):
        self.conn.close()