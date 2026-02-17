import re


def clean_text(text: str) -> str:
    """
    Clean OCR text output for better embedding and retrieval.
    """

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove strange characters (keep basic punctuation)
    text = re.sub(r"[^\w\s.,!?;:()\-]", "", text)

    # Strip leading/trailing spaces
    text = text.strip()

    return text
