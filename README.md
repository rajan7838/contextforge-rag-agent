# ContextForge - Production RAG AI Agent

## Overview
ContextForge is a production-grade RAG AI Agent using LangGraph + Groq LLM with ChromaDB vector storage, BGE reranking, SQLite memory persistence, and deterministic guardrails.

## Features
- **LangGraph Agent** - Advanced agent workflow with 7 tools
- **Groq LLM** - Fast inference with llama-3.1-8b-instant
- **ChromaDB** - Vector database for PDF document search
- **BGE Reranking** - Accurate PDF search results
- **SQLite Memory** - Persistent chat history
- **Guardrails** - Safety filter for restricted queries
- **Streamlit Cloud** - Deploy in minutes

## Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file with your API keys
# Run locally
python run.py