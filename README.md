ContextForge - Production RAG AI Agent
Project Overview
ContextForge is a production-ready Retrieval-Augmented Generation (RAG) AI Agent built with LangGraph and the Groq LLM. It uses ChromaDB for vector storage, BGE for reranking, SQLite for persistent memory, and includes deterministic guardrails for safety. The application is deployed on Streamlit Cloud.

Step 1: Core System Features
Capabilities & Infrastructure
LangGraph Agent
Advanced agentic workflow with access to 7 distinct tools.

Groq LLM
High-speed inference powered by the llama-3.1-8b-instant model.

ChromaDB & BGE Reranking
Vector database for document search with BGE reranker for highly accurate PDF results.

SQLite Memory
Persistent chat history storage for session management.

Deterministic Guardrails
Input safety filter to block restricted queries.

Streamlit Cloud
Simple and quick deployment.

Step 2: Available Agent Tools
Functional Toolset
The agent has access to the following tools:

Weather
Get current weather for any city.

Time
Get the current date and time.

Calculator
Perform mathematical calculations.

Word Count
Count words in a text string.

Reverse Text
Reverse any given text.

PDF Search
Query and retrieve information from uploaded PDF documents (using RAG).

Send Email
Send emails via SMTP (requires configuration).

Step 3: Project Structure
Directory Layout
The project code is organized into dedicated directories for the web interface, source core logic, and local data storage. Key files include configuration files, dependency requirements, and local execution scripts located in the root directory.

text
contextforge/
├── app/
│   └── app.py                 # Streamlit web interface
├── src/
│   ├── __init__.py
│   ├── agent.py               # Main agent class (UltimateRerankedAgent)
│   ├── tools.py               # Definitions for all 7 tools
│   └── guardrails.py          # Safety filter layer
├── data/
│   ├── chroma_db/             # Persistent vector database
│   └── documents/             # Folder for PDF documents (e.g., attention.pdf)
├── agent_memory.db            # SQLite memory file (auto-created)
├── .env                       # Environment variables (API keys) - not committed
├── config.yaml                # Configuration settings
├── requirements.txt           # Python dependencies
├── run.py                     # Local entry point
└── README.md                  # This file
Step 4: Local Development Setup
Step-by-Step Installation
Clone the repository

bash
git clone https://github.com/rajan7838/contextforge-rag-agent.git
cd contextforge-rag-agent
Install dependencies

bash
pip install -r requirements.txt
Set up environment variables
Create a .env file in the root directory and add your API keys:

env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=GENAI
LANGCHAIN_TRACING_V2=true
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
Run the application locally

bash
streamlit run app/app.py
# or
python run.py
Step 5: Cloud Deployment
Deploying on Streamlit Cloud
Push code
Upload your code changes to a GitHub repository.

Connect account
Go to Streamlit Cloud and link your GitHub profile.

Select entry file
Deploy the application by choosing the repo and the main file (app/app.py).

Configure environment secrets
Add keys in the Streamlit Cloud dashboard under Settings -> Secrets.

Publish
Click "Redeploy" to push the application live.

Step 6: System Architecture
Modular Code Layout
The application follows a modular design pattern:

src/agent.py
Contains the UltimateRerankedAgent class which orchestrates the LLM, tools, memory, and RAG pipeline.

src/tools.py
Defines the functions for the agent's tools (weather, time, calculator, etc.).

src/guardrails.py
Implements a safety filter that scans user input for restricted keywords.

app/app.py
The Streamlit interface that handles user interaction, session state, and displays results.

Step 7: Contribution & Governance
Community Rules & Credits
Contributing
Contributions are welcome. Please fork the repository, create your feature branch, commit changes, and open a Pull Request.

License
This project is licensed under the MIT License.

Acknowledgements
Built using LangGraph, Groq, Hugging Face sentence-transformers, and Streamlit.

Project Links
Deployment Assets
Live App
https://contextforge-rag-agent-bj2pypmhvukqurxctrclih.streamlit.app/

GitHub Repository
https://github.com/rajan7838/contextforge-rag-agent

