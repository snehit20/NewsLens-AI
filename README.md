<div align="center">

# 📰 NewsLens AI

### AI-Powered News Research Assistant using RAG

Ask questions about the latest news and get source-grounded answers powered by Retrieval-Augmented Generation (RAG).

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)]()
[![ChromaDB](https://img.shields.io/badge/VectorDB-Chroma-blue?style=for-the-badge)]()
[![Groq](https://img.shields.io/badge/LLM-Groq-black?style=for-the-badge)]()

### 🌐 Live Demo
👉 **https://YOUR_STREAMLIT_URL**

</div>

---

## 📖 Overview

NewsLens AI is an intelligent news research assistant that transforms live news into a searchable knowledge base.

Instead of reading multiple articles individually, simply enter any news topic and ask questions naturally. The application retrieves relevant news articles, builds a vector database, and answers your questions using Retrieval-Augmented Generation (RAG).

Every response is grounded in the retrieved articles and includes the corresponding sources.

---

## ✨ Features

- 📰 Fetches latest news articles using GNews API
- 🌐 Loads article content directly from news websites
- ✂️ Intelligent text chunking
- 🔍 Semantic search with ChromaDB
- 🤖 RAG-powered question answering
- 📚 Source-aware responses
- ⚡ Fast inference using Groq Llama 3.3 70B
- 🎨 Interactive Streamlit interface

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | Streamlit |
| LLM | Groq (Llama 3.3 70B) |
| Framework | LangChain |
| Embeddings | HuggingFace (all-MiniLM-L6-v2) |
| Vector Store | ChromaDB |
| News API | GNews |
| Document Loader | WebBaseLoader |

---

## 🧠 How It Works

```text
User Query
      │
      ▼
 GNews API
      │
      ▼
Retrieve News URLs
      │
      ▼
WebBaseLoader
      │
      ▼
Clean & Chunk Articles
      │
      ▼
HuggingFace Embeddings
      │
      ▼
Chroma Vector Store
      │
      ▼
Retriever
      │
      ▼
Groq LLM
      │
      ▼
Answer + Sources
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/NewsLens-AI.git

cd NewsLens-AI
```

### Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key

GNEWS_API_KEY=your_gnews_api_key
```

---

## ▶️ Run the application

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```text
NewsLens-AI/
│
├── app.py
├── sample.py
├── requirements.txt
├── .env
├── README.md
└── assets/
```

---

## 💬 Example Questions

- What happened in AI this week?
- Summarize today's healthcare news.
- Explain the recent developments in quantum computing.
- What are the latest updates on Tesla?
- How is AI being used in education?

---

## 📸 Demo

<img width="100%" src="assets/demo.png">

> Add a screenshot named **demo.png** inside an **assets** folder.

---

## 📌 Future Improvements

- [ ] Multi-turn conversations
- [ ] Streaming responses
- [ ] Better article cleaning
- [ ] Hybrid Search (Dense + BM25)
- [ ] Source ranking
- [ ] Citation highlighting
- [ ] Multi-language news support
- [ ] Research report generation

---

## 🤝 Contributing

Contributions, ideas and suggestions are always welcome!

Feel free to fork the repository and submit a pull request.

---

## ⭐ Support

If you found this project useful,

**leave a ⭐ on the repository!**

It helps more people discover the project.

---

<div align="center">

Made with ❤️ by **Snehit Singh**

Building AI applications with LangChain • RAG • LLMs

</div>
