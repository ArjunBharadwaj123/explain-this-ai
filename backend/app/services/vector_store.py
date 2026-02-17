import numpy as np

# Simple in-memory storage
# Structure:
# {
#   "filename": {
#       "chunks": [...],
#       "embeddings": np.ndarray
#   }
# }

vector_store = {}


def store_document(doc_id: str, chunks: list[str], embeddings: np.ndarray):
    vector_store[doc_id] = {
        "chunks": [
            {"id": i, "text": chunk}
            for i, chunk in enumerate(chunks)
        ],
        "embeddings": embeddings
    }



def get_document(doc_id: str):
    return vector_store.get(doc_id)
