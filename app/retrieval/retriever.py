from app.embeddings.embedding_generator import model


def retrieve_chunks(vector_store, query, top_k=3):

    query_embedding = model.encode([query])

    distances, indices = vector_store.index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(vector_store.documents[idx])

    return results