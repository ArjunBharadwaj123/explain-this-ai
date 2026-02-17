import numpy as np
from app.services.embedding_service import model


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """
    Compute cosine similarity between two vectors.
    """
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve_top_k(query: str, chunks: list[str], embeddings: np.ndarray, k: int = 3):

    query_embedding = model.encode([query])[0]

    similarities = []

    for i, chunk_embedding in enumerate(embeddings):
        score = float(cosine_similarity(query_embedding, chunk_embedding))

        similarities.append({
            "chunk": chunks[i],
            "score": score,
            "chunk_id": i
        })

    # Sort highest similarity first
    similarities.sort(key=lambda x: x["score"], reverse=True)

    # 🔥 Filter out weak matches
    SIMILARITY_THRESHOLD = 0.3

    filtered = [
        item for item in similarities
        if item["score"] > SIMILARITY_THRESHOLD
    ]

    return filtered[:k]

