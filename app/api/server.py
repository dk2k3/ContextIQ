from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.embeddings.vector_store import VectorStore
from app.rag_pipeline import ask_question

from app.ingestion.pdf_loader import load_pdf
from app.ingestion.text_cleaner import clean_text
from app.ingestion.chunker import split_into_chunks
from app.embeddings.embedding_generator import generate_embeddings


app = FastAPI(title="ContextIQ API")

vector_db = VectorStore()
vector_db.load_index()

UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():
    return {"message": "ContextIQ API running"}


@app.get("/ask")
def ask(query: str):

    answer = ask_question(vector_db, query)

    return {"question": query, "answer": answer}


@app.post("/upload-document")
def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Document ingestion pipeline
    text = load_pdf(file_path)
    cleaned_text = clean_text(text)
    chunks = split_into_chunks(cleaned_text)
    embeddings = generate_embeddings(chunks)

    vector_db.build_index(embeddings, chunks)

    return {
        "message": "Document uploaded and indexed successfully",
        "chunks_created": len(chunks)
    }