import faiss
import numpy as np
import os
import pickle


class VectorStore:

    def __init__(self):

        self.index = None
        self.documents = []

        self.index_path = "vector_store_data/faiss_index.bin"
        self.docs_path = "vector_store_data/documents.pkl"

        os.makedirs("vector_store_data", exist_ok=True)

    def build_index(self, embeddings, chunks):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(np.array(embeddings))

        self.documents = chunks

        self.save_index()

    def search(self, query_embedding, k=5):

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for i in indices[0]:
            results.append(self.documents[i])

        return results

    def save_index(self):

        if self.index is not None:

            faiss.write_index(self.index, self.index_path)

            with open(self.docs_path, "wb") as f:
                pickle.dump(self.documents, f)

            print("Vector database saved to disk.")

    def load_index(self):

        if os.path.exists(self.index_path) and os.path.exists(self.docs_path):

            self.index = faiss.read_index(self.index_path)

            with open(self.docs_path, "rb") as f:
                self.documents = pickle.load(f)

            print("Vector database loaded from disk.")

            return True

        return False