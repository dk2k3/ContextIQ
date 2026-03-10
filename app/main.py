import os

from app.ingestion.pdf_loader import load_pdf
from app.ingestion.text_cleaner import clean_text
from app.ingestion.chunker import split_into_chunks

from app.embeddings.embedding_generator import generate_embeddings
from app.embeddings.vector_store import VectorStore

from app.rag_pipeline import ask_question


def ingest_document(file_path):

    print("Loading PDF...")

    text = load_pdf(file_path)

    print("Cleaning text...")

    cleaned_text = clean_text(text)

    print("Chunking text...")

    chunks = split_into_chunks(cleaned_text)

    print(f"Created {len(chunks)} chunks")

    print("Generating embeddings...")

    embeddings = generate_embeddings(chunks)

    print("Building vector store...")

    vector_store = VectorStore()

    vector_store.build_index(embeddings, chunks)

    print("Document ingestion complete")

    return vector_store


if __name__ == "__main__":

    vector_db = VectorStore()

    # Try loading existing vector database
    loaded = vector_db.load_index()

    if not loaded:

        print("No existing vector database found.")
        print("Starting document ingestion...")

        pdf_path = "data/sample.pdf"

        vector_db = ingest_document(pdf_path)

    else:

        print("Vector database loaded successfully.")

    print("\nVector database ready.")
    print("\nYou can now ask questions about the document.")

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = ask_question(vector_db, question)

        print("\nAnswer:\n")
        print(answer)