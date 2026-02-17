import easyocr

# Initialize reader once (important for performance)
reader = easyocr.Reader(["en"], gpu=False)


def extract_text(image_path: str) -> str:
    """
    Extract text from image using EasyOCR
    """
    results = reader.readtext(image_path)

    # results format: [(bbox, text, confidence), ...]
    extracted_text = [text for (_, text, _) in results]

    return "\n".join(extracted_text)
