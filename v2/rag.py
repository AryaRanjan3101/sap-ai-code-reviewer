import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DOCS_PATH = os.path.join(os.path.dirname(__file__), "docs")
CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")

def build_knowledge_base():   
    documents = []
    for filename in os.listdir(DOCS_PATH):
        if filename.endswith(".md") or filename.endswith(".txt"):
            loader = TextLoader(os.path.join(DOCS_PATH, filename), encoding="utf-8")
            documents.extend(loader.load())
  
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
  
    db = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)
    print(f"Knowledge base built with {len(chunks)} chunks")
    return db

def get_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    if not os.path.exists(CHROMA_PATH):
        return build_knowledge_base().as_retriever(search_kwargs={"k": 5})
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    return db.as_retriever(search_kwargs={"k": 5})