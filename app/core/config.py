import os
from dotenv import load_dotenv

load_dotenv()

# Embedding model
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

# Vector database path
VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "app/storage/vector_db"
)

# Upload directory
UPLOAD_DIR = os.getenv(
    "UPLOAD_DIR",
    "app/storage/uploads"
)

# Chunk settings
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))

# Retrieval setting
TOP_K = int(os.getenv("TOP_K", 5))