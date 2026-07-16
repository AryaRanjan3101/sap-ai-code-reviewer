 # SAP AI Code Reviewer
  
  An AI-powered developer assistant for SAP ABAP developers that reviews ABAP code against official SAP Clean
  ABAP guidelines and modern S/4HANA development best practices.

  ## Why This Project?

  SAP developers frequently use tools like ATC and Code Inspector to identify issues in ABAP programs. While
  these tools are excellent at detecting problems, understanding the reason behind an issue and finding the
  right solution can still take time.

  SAP AI Code Reviewer bridges that gap by using Generative AI to:

  - Explain code quality issues in plain language
  - Suggest modern ABAP and Clean ABAP improvements
  - Recommend performance optimizations
  - Highlight security vulnerabilities and S/4HANA Clean Core violations

  The goal is not to replace ATC, but to help developers understand and resolve findings more efficiently.
  
  ---

  ## Versions

  ### V1 — Prompt-Based AI Reviewer (`/`)
  The first version uses a carefully engineered system prompt with embedded SAP best practices to review ABAP
  code using Google Gemini 2.5 Flash.
  
  **Covers:**
  - Performance issues (SELECT *, nested SELECTs, missing WHERE clauses)
  - Modern ABAP (inline declarations, string templates, FIELD-SYMBOL)
  - Object-Oriented ABAP principles
  - Security (authority checks, dynamic SQL)
  - S/4HANA Clean Core compliance
  - Overall rating out of 10

  ### V2 — RAG-Based Reviewer (`/v2`)
  The second version introduces Retrieval-Augmented Generation (RAG). Before reviewing code, the system searches
   SAP's official Clean ABAP Style Guide and retrieves the most relevant guidelines. These are passed to Gemini 
  alongside the code, making reviews grounded in SAP's official documentation.

  **Additional capabilities:**
  - Reviews code against SAP's official Clean ABAP Style Guide
  - Cites specific guidelines in the review output
  - More accurate and authoritative recommendations
  - Local embeddings using HuggingFace (no additional API quota needed)

  ---

  ## Architecture

  ### V1
  Developer → Web Interface → Flask Backend → Google Gemini → Structured Review
  
  ### V2 (RAG)
  Developer → Web Interface → Flask Backend
                                    │
                                    
                            ┌───────┴────────┐
                            ▼                ▼
                            
                    Google Gemini    ChromaDB (Clean ABAP)
                    
                            │                │
                            └───────┬────────┘
                                    ▼
                                    
                            Grounded Code Review

  ---
  
  ## Tech Stack

  - Python + Flask
  - Google Gemini 2.5 Flash
  - HuggingFace Sentence Transformers (embeddings)
  - ChromaDB (vector database)  
  - SAP BTP Business Application Studio
  - HTML / CSS / JavaScript

  ---
  
  ## Installation

  ```bash
  git clone https://github.com/AryaRanjan3101/sap-ai-code-reviewer.git
  cd sap-ai-code-reviewer
  pip install -r requirements.txt
  export GOOGLE_API_KEY=your_api_key

  Run V1:
  python app.py

  Run V2:
  cd v2
  python app.py

  ---
  Future Roadmap
  
  - ATC finding explainer — paste ATC message, get plain English explanation
  - ABAP to Modern ABAP converter
  - ABAP HTTP client to call reviewer directly from SAP system
  - FastAPI migration
  - Docker support
  - GitHub Pull Request integration

  ---
  Author

  Arya Ranjan
  SAP ABAP Developer | SAP BTP | Generative AI
  LinkedIn (https://www.linkedin.com/in/aryaranjan1) | GitHub (https://github.com/AryaRanjan3101)
  
