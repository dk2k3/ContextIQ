from app.retrieval.retriever import retrieve_chunks
from app.llm.ollama_client import ask_llm


def ask_question(vector_store, question):

    chunks = retrieve_chunks(vector_store, question)

    context = "\n\n".join(chunks)

    answer = ask_llm(context, question)

    return answer