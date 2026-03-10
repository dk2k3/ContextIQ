from app.core.config import CHUNK_SIZE, CHUNK_OVERLAP


def split_into_chunks(text: str):

    chunks = []

    start = 0

    while start < len(text):

        end = start + CHUNK_SIZE

        chunk = text[start:end]

        chunks.append(chunk)

        start += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks