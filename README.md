# ContextForge - Production RAG AI Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://contextforge-rag-agent-bj2pypmhvukqurxctrclih.streamlit.app/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

---

## 📋 **Project Overview**

ContextForge is a **production-ready Retrieval-Augmented Generation (RAG) AI Agent** built with LangGraph and the Groq LLM. It uses ChromaDB for vector storage, BGE for reranking, SQLite for persistent memory, and includes deterministic guardrails for safety. The application is deployed on **Streamlit Cloud**.

---

## 🚀 **Live Demo**

🔗 **Live App:** [https://contextforge-rag-agent-bj2pypmhvukqurxctrclih.streamlit.app/](https://contextforge-rag-agent-bj2pypmhvukqurxctrclih.streamlit.app/)

---

## ✨ **Key Features**

### **Core System Capabilities**

| Feature | Description |
|---------|-------------|
| **LangGraph Agent** | Advanced agentic workflow with access to 7 distinct tools. |
| **Groq LLM** | High-speed inference powered by the `llama-3.1-8b-instant` model. |
| **ChromaDB & BGE Reranking** | Vector database for document search with BGE reranker for highly accurate PDF results. |
| **SQLite Memory** | Persistent chat history storage for session management. |
| **Deterministic Guardrails** | Input safety filter to block restricted queries. |
| **Streamlit Cloud** | Simple and quick deployment. |

---

## 🛠️ **Available Tools**

The agent has access to the following **7 tools**:

| Tool | Description |
|------|-------------|
| 🌤️ **Weather** | Get current weather for any city. |
| ⏰ **Time** | Get the current date and time. |
| 🧮 **Calculator** | Perform mathematical calculations. |
| 📝 **Word Count** | Count words in a text string. |
| 🔄 **Reverse Text** | Reverse any given text. |
| 📄 **PDF Search** | Query and retrieve information from uploaded PDF documents (using RAG). |
| ✉️ **Send Email** | Send emails via SMTP (requires configuration). |

---

## 📁 **Project Structure**
contextforge/
├── app/
│ └── app.py # Streamlit web interface
├── src/
│ ├── init.py
│ ├── agent.py # Main agent class (UltimateRerankedAgent)
│ ├── tools.py # Definitions for all 7 tools
│ └── guardrails.py # Safety filter layer
├── data/
│ ├── chroma_db/ # Persistent vector database
│ └── documents/ # Folder for PDF documents (e.g., attention.pdf)
├── agent_memory.db # SQLite memory file (auto-created)
├── .env # Environment variables (API keys) - not committed
├── config.yaml # Configuration settings
├── requirements.txt # Python dependencies
├── run.py # Local entry point
└── README.md # This file

text

---

## 💻 **Local Development Setup**

### **Prerequisites**
- Python 3.8 or higher
- Git

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/rajan7838/contextforge-rag-agent.git
cd contextforge-rag-agent
Step 2: Install Dependencies
bash
pip install -r requirements.txt
Step 3: Set Up Environment Variables
Create a .env file in the root directory and add your API keys:

env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=GENAI
LANGCHAIN_TRACING_V2=true
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
Step 4: Run the Application Locally
bash
streamlit run app/app.py
OR

bash
python run.py
☁️ Cloud Deployment
Deploying on Streamlit Cloud
Push Code: Upload your code changes to a GitHub repository.

Connect Account: Go to Streamlit Cloud and link your GitHub profile.

Select Entry File: Deploy the application by choosing the repo and the main file (app/app.py).

Configure Secrets: Add keys in the Streamlit Cloud dashboard under Settings → Secrets.

Publish: Click "Redeploy" to push the application live.

🏗️ System Architecture
The application follows a modular design pattern:

File	Purpose
src/agent.py	Contains the UltimateRerankedAgent class which orchestrates the LLM, tools, memory, and RAG pipeline.
src/tools.py	Defines the functions for the agent's tools (weather, time, calculator, etc.).
src/guardrails.py	Implements a safety filter that scans user input for restricted keywords.
app/app.py	The Streamlit interface that handles user interaction, session state, and displays results.
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create your feature branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgements
LangGraph for the agent framework.

Groq for the fast LLM inference.

Hugging Face for the sentence-transformers and BGE-reranker models.

Streamlit for the easy-to-use deployment platform.

🔗 Project Links
🐙 GitHub Repository: https://github.com/rajan7838/contextforge-rag-agent

🌐 Live App: https://contextforge-rag-agent-bj2pypmhvukqurxctrclih.streamlit.app/

Built with ❤️ using LangGraph, Groq, and Streamlit

text

---

## ✅ **How to Update Your GitHub README**

1. Copy the entire Markdown code block above.
2. In your GitHub repository, click on the **README.md** file.
3. Click the **pencil icon (✏️)** to edit.
4. **Delete all existing content** and paste the new one.
5. Scroll down and click **"Commit changes"**.

---

## 🎯 **What This Fixes**

| Issue | Solution |
|-------|----------|
| Text appearing as one block | Added proper Markdown formatting with headers and separators |
| No visual hierarchy | Used headers (`##`, `###`), bold text, and tables |
| No structure | Organized into clear sections with step-by-step guides |
| Missing visual elements | Added badges, emojis, and tables for better readability |
| Hard to read | Added bullet points and code blocks for commands |

---

## 📊 **Result Preview**

After updating, your GitHub page will display:

✅ Professional headers with clear hierarchy  
✅ **Bold** and *italicized* text for emphasis  
✅ Tables for features and tools  
✅ Code blocks with proper syntax highlighting  
✅ Badges for quick reference (Live App, License)  
✅ Emojis for visual appeal (but not overly used)  
✅ Clean, well-spaced sections  

---

**Your README will now look clean, professional, and well-organized!** 🚀
