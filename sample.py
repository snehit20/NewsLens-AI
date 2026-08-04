def build_chain(que):

    import requests
    import os 
    from langchain_groq import ChatGroq
    from langchain_core.documents import Document
    from langchain_community.document_loaders import WebBaseLoader
    from langchain_chroma import Chroma
    from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import PromptTemplate
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    import bs4
    import re
    from dotenv import load_dotenv
    load_dotenv()
    import streamlit as st

    API_KEY = os.getenv("GNEWS_API_KEY") or st.secrets["GNEWS_API_KEY"]
    os.environ["GROQ_API_KEY"] = (
        os.getenv("GROQ_API_KEY") or st.secrets["GROQ_API_KEY"]
    )

    #calling GNews for url
    response = requests.get(
        "https://gnews.io/api/v4/search",
        params={
            "q": query,
            "apikey": API_KEY,
            "max": 10,
            "lang": "en"
        },
        timeout=20
    )

    data = response.json()

    print("Status:", response.status_code)
    print("Response:", data)

    if response.status_code != 200:
        raise Exception(f"GNews Error: {response.status_code}\n{data}")

    if "articles" not in data:
        raise Exception(f"GNews did not return articles.\nResponse: {data}")

    metadata_lookup = {}

    for article in data["articles"]:
        metadata_lookup[article["url"]] = {
            "title": article["title"],
            "publishedAt": article["publishedAt"],
            "url": article["url"],
            "source": article["source"]["name"],
        }

    urls = list(metadata_lookup.keys())

    #loading all the content in the form of documents
    docs = []
    for i, url in enumerate(urls, start=1):
        print(f"Loading {i}/10: {url}")

        try:
            loader = WebBaseLoader(
            web_path=[url],
            requests_kwargs={
                "timeout":20,
                "headers":{
                    "User-Agent":"Mozilla/5.0"
                }
            }
        )

            doc = loader.load()
            docs.extend(doc)

            print(f"Loaded {len(doc)} docs")

        except Exception as e:
            print(f"Skipped {url}")
            print(f"Reason: {e}")


    #improving metadat
    for d in docs:
        article_url = d.metadata["source"]

        d.metadata.update({
            "title": metadata_lookup[article_url]["title"],
            "publisher": metadata_lookup[article_url]["source"],
            "publishedAt": metadata_lookup[article_url]["publishedAt"],
            "url": metadata_lookup[article_url]["url"]
        })



    #reviewing what how the content is 
    # for doc in docs:
    #     print("=" * 100)
    #     print(doc.metadata["title"])
    #     print("Next...\n")
    #     print(doc.page_content[:1500])

    # Junk in the start and end (use simple tech - later may replace it with LLM)


    for d in docs:
        text = d.page_content
        text = re.sub(r"\s+", " ", text)
        d.page_content = text  

    #chunk
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    print("Documents:", len(docs))
    print("Chunks:", len(chunks))

    if not chunks:
        raise Exception(
            "No document chunks were created. Most likely every news website blocked scraping."
        )

    print(len(chunks))

    #vectorise and vector store
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(
        chunks,
        embeddings
    )

    #retriver 
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 10}
    )


    #main Mind
    llm = ChatGroq(model="llama-3.3-70b-versatile")
    temp = """
    You are NewsLens AI, a news research assistant.

    Your task is to answer questions using ONLY the provided news article excerpts.

    Each source contains:

    * Title
    * Publisher
    * Publication date
    * URL
    * Article content

    Instructions:

    1. Answer the user's question using only information found in the provided sources.
    2. Do not invent facts, statistics, events, or conclusions.
    3. If the sources do not contain enough information to answer the question, explicitly say so.
    4. When multiple sources discuss the same topic, combine their information into a coherent answer.
    5. When sources disagree, mention the disagreement and identify the sources involved.
    6. After the answer, provide a "Sources" section listing the articles that contributed to the response.
    7. Include the article title and URL for every source used.
    8. Prefer recent and more detailed sources when relevant.
    9. Ignore website navigation text, advertisements, subscription prompts, and unrelated boilerplate that may appear in the context.

    CONTEXT:
    {context}

    QUESTION:
    {question}

    Provide your response in the following format:

    Answer: <detailed answer>

    Sources:

    * <Article Title> | <URL>
    * <Article Title> | <URL>

    """
    prompt = PromptTemplate(
        template=temp,
        input_variables=["context","question"]
    )

    #context + metadata
    def text(docs):
        context_parts = []

        for i, doc in enumerate(docs, start=1):
            context_parts.append(
                f"""
        SOURCE {i}
        Title: {doc.metadata.get('title')}
        Publisher: {doc.metadata.get('publisher', doc.metadata.get('source'))}
        Published: {doc.metadata.get('publishedAt')}
        URL: {doc.metadata.get('url')}

        CONTENT:
        {doc.page_content}
        """
            )

        context = "\n\n".join(context_parts)

        return context


    #chain
    parser = StrOutputParser()
    p_chain = RunnableParallel({
        "context": retriever|RunnableLambda(text),
        "question":RunnablePassthrough()
    })
    main_chain = p_chain|prompt|llm|parser
    return main_chain

