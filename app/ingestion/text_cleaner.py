import re


def clean_text(text: str) -> str:
    """
    Clean extracted text
    """

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove weird characters
    text = re.sub(r"[^\w\s.,!?]", "", text)

    return text.strip()