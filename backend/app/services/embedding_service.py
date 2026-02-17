from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once at startup (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_chunks(chunks: list[str]) -> np.ndarray:
    """
    Convert list of text chunks into embedding vectors.
    
    Returns:
        NumPy array of shape (num_chunks, embedding_dim)
    """
    embeddings = model.encode(chunks)
    return np.array(embeddings)
