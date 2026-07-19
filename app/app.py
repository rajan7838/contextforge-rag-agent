import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent import UltimateRerankedAgent

st.set_page_config(
    page_title="ContextForge - RAG AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("ContextForge - RAG AI Agent")
st.markdown("### Production-grade RAG with LangGraph + Groq LLM")

# Initialize agent
@st.cache_resource
def get_agent():
    return UltimateRerankedAgent(pdf_path='data/documents/attention.pdf')

try:
    agent = get_agent()
except Exception as e:
    st.error(f"Error initializing agent: {e}")
    st.stop()

# Sidebar
with st.sidebar:
    st.header("Controls")
    
    session_id = st.text_input("Session ID", value="default_user")
    if st.button("Switch Session"):
        agent.set_session(session_id)
        st.success(f"Switched to: {session_id}")
    
    st.divider()
    
    if st.button("Show History"):
        history = agent.show_history()
        st.text_area("History", history, height=200)
    
    if st.button("Clear Memory"):
        result = agent.clear_memory()
        st.success(result)
    
    if st.button("Show Stats"):
        stats = agent.show_stats()
        st.json(stats)
    
    st.divider()
    st.markdown("### Available Tools")
    st.markdown("""
    - Weather
    - Time
    - Calculator
    - Word Count
    - Reverse Text
    - PDF Search
    - Send Email
    """)

# Main chat interface
st.markdown("###  Chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = agent.stream_query(prompt)
            st.markdown(response)
    
    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.divider()
st.markdown("""
 **Technologies**: LangGraph | Groq LLM | ChromaDB | BGE Reranking | SQLite Memory | Deterministic Guardrails
""")