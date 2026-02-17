from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np

from app.services.retrieval_service import retrieve_top_k
from app.services.embedding_service import embed_chunks
from app.utils.chunking import chunk_text
from app.utils.text_cleaning import clean_text
from app.services.ocr_service import extract_text
from app.services.llm_service import generate_answer
from app.services.vector_store import get_document



router = APIRouter()


class QueryRequest(BaseModel):
    image_path: str
    question: str


@router.post("/retrieve")
def retrieve_context(request: QueryRequest):
    # Full pipeline (temporary for testing)

    raw_text = extract_text(request.image_path)
    cleaned_text = clean_text(raw_text)
    chunks = chunk_text(cleaned_text)
    embeddings = embed_chunks(chunks)

    top_chunks = retrieve_top_k(
        request.question,
        chunks,
        embeddings,
        k=3
    )

    return {
        "top_chunks": top_chunks
    }

@router.post("/ask")
def ask_question(request: QueryRequest):
    document = get_document(request.image_path.split("/")[-1])

    if document is None:
        return {"error": "Document not found. Upload image first."}

    chunk_objects = document["chunks"]
    chunks = [chunk["text"] for chunk in chunk_objects]

    embeddings = document["embeddings"]

    top_chunks_with_scores = retrieve_top_k(
        request.question,
        chunks,
        embeddings,
        k=3
    )

    answer = generate_answer(request.question, top_chunks_with_scores)


    # Format sources cleanly
    sources = []

    for item in top_chunks_with_scores:
        chunk_text = item["chunk"]
        score = float(item["score"])

        # Find matching chunk ID
        chunk_id = next(
            chunk["id"]
            for chunk in chunk_objects
            if chunk["text"] == chunk_text
        )

        sources.append({
            "chunk_id": chunk_id,
            "score": score,
            "preview": chunk_text[:120]  # Short preview
        })


    return {
        "answer": answer,
        "sources": sources
    }
