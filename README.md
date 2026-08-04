<img width="1837" height="522" alt="image" src="https://github.com/user-attachments/assets/a0231978-d1d3-46ce-af9b-05a7591ad88e" /><div align="center">

# 📰 NewsLens AI

### AI-Powered News Research Assistant using Retrieval-Augmented Generation (RAG)

Research any news topic, chat with the latest news articles, and get source-grounded answers powered by AI.

<p>
<a href="https://newslens-ai-3p4rfqc3mfsoubvscuwpyw.streamlit.app/"><img src="https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-red?style=for-the-badge"></a>
<a href="https://github.com/snehit20/NewsLens-AI"><img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github"></a>
</p>

</div>

---

# 📖 Overview

**NewsLens AI** is an AI-powered news research assistant that transforms the latest news articles into a searchable knowledge base using **Retrieval-Augmented Generation (RAG)**.

Instead of reading multiple articles individually, simply enter any news topic and ask questions naturally. NewsLens AI retrieves relevant news articles, builds a vector database, and generates grounded answers with citations.

---

# ✨ Features

- 📰 Fetches the latest news articles using the GNews API
- 🌐 Automatically extracts article content
- ✂️ Intelligent document chunking
- 🧠 Semantic search using HuggingFace embeddings
- 📚 ChromaDB vector database
- 🤖 Source-grounded answers using Groq Llama 3.3 70B
- 🔍 Retrieval-Augmented Generation (RAG)
- 📎 Displays sources used for every answer
- ⚡ Fast and interactive Streamlit interface

---

# 🏗️ Architecture

```text
                User Query
                     │
                     ▼
             GNews API Search
                     │
                     ▼
          Retrieve Relevant URLs
                     │
                     ▼
             WebBaseLoader
                     │
                     ▼
          Text Cleaning & Chunking
                     │
                     ▼
      HuggingFace Embeddings
                     │
                     ▼
            Chroma Vector Store
                     │
                     ▼
              Semantic Retriever
                     │
                     ▼
          Groq Llama 3.3 70B LLM
                     │
                     ▼
          Answer + Source Citations
```

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | Streamlit |
| Framework | LangChain |
| LLM | Groq (Llama 3.3 70B) |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database | ChromaDB |
| News API | GNews |
| Document Loader | WebBaseLoader |
| Language | Python |

---

# 🚀 Live Demo

### Try it here 👇

**https://newslens-ai-3p4rfqc3mfsoubvscuwpyw.streamlit.app/**

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/snehit20/NewsLens-AI.git
cd NewsLens-AI
```

Create a virtual environment

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

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
GNEWS_API_KEY=your_gnews_api_key
```

---

# ▶️ Run Locally

```bash
streamlit run app.py
```

---

# 📂 Project Structure

```text
NewsLens-AI
│
├── app.py
├── sample.py
├── requirements.txt
├── README.md
└── assets
```

---

# 💡 Example Queries

- What are the latest developments in AI?
- Summarize today's healthcare news.
- Explain the recent Tesla announcements.
- What's happening in the world of robotics?
- How is AI transforming education?

---

# 📸 Demo

> Add a screenshot of your application below.

<img width="1837" height="522" alt="image" src="https://github.com/user-attachments/assets/d382d10e-7847-435d-8d32-6e1964ed6b8b" />
<img width="1770" height="797" alt="image" src="https://github.com/user-attachments/assets/b96e5364-83c7-42b2-9d07-4bc718a59552" />


---

# 🚧 Future Improvements

- Multi-turn conversations
- Persistent chat history
- Better article preprocessing
- Hybrid Search (Dense + BM25)
- Source ranking
- Streaming responses
- Research report generation
- Multi-language support

---

# 🤝 Contributing

Contributions are always welcome!

If you'd like to improve NewsLens AI, feel free to fork the repository and open a pull request.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---

<div align="center">

### Built with ❤️ by Snehit Singh

**LangChain • RAG • Groq • ChromaDB • HuggingFace • Streamlit**

</div>
