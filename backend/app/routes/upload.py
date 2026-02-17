from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid
from app.services.ocr_service import extract_text
from app.utils.text_cleaning import clean_text
from app.utils.chunking import chunk_text
from app.services.embedding_service import embed_chunks
from app.services.vector_store import store_document




router = APIRouter()

UPLOAD_DIR = "uploaded_files"

# Create directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    # Generate unique filename
    file_extension = file.filename.split(".")[-1]
    unique_filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    # Save file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Run OCR
    raw_text = extract_text(file_path)
    cleaned_text = clean_text(raw_text)
    chunks = chunk_text(cleaned_text)
    embeddings = embed_chunks(chunks)
    store_document(unique_filename, chunks, embeddings)


    return {
        "message": "Image uploaded and processed successfully",
        "filename": unique_filename,
        "num_chunks": len(chunks),
    }

