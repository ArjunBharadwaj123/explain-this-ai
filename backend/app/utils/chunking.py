def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50):
    """
    Split text into overlapping chunks.
    chunk_size = number of characters per chunk
    overlap = overlapping characters between chunks
    """

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks
