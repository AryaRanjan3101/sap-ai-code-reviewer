# SAP AI Code Reviewer

An AI-powered developer assistant for SAP ABAP developers that reviews ABAP code, explains potential ATC findings in simple language, and recommends modern SAP development best practices.

---

## Why This Project?

SAP developers frequently use tools like ATC and Code Inspector to identify issues in ABAP programs. While these tools are excellent at detecting problems, understanding the reason behind an issue and finding the right solution can still take time.

SAP AI Code Reviewer aims to bridge that gap by using Generative AI to:

* Explain code quality issues in simple language
* Suggest modern ABAP and Clean ABAP improvements
* Recommend performance optimizations
* Highlight security and S/4HANA best practices

The goal is not to replace ATC, but to help developers understand and resolve findings more efficiently.

---

## Features

* AI-powered ABAP code review
* Performance recommendations
* Modern ABAP best practices
* Object-Oriented ABAP suggestions
* Security checks
* Clean Core and S/4HANA recommendations
* Overall code quality assessment

---

## Tech Stack

* Python
* Flask
* Google Gemini 2.5 Flash
* HTML
* SAP BTP Business Application Studio

---

## Current Architecture

```text
Developer
      │
      ▼
Web Interface
      │
      ▼
Flask Backend
      │
      ▼
Google Gemini
      │
      ▼
Structured Code Review
```

---

## Future Roadmap

* FastAPI migration
* Docker support
* Retrieval-Augmented Generation (RAG)
* Structured JSON responses
* GitHub Pull Request review
* SAP BTP deployment enhancements
* SAP developer knowledge base

---

## Author

**Arya Ranjan**

SAP ABAP Developer passionate about Enterprise AI, SAP BTP, and building AI-powered developer tools.
