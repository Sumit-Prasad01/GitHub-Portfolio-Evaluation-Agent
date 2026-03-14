import re


def clean_text(text: str) -> str:
    """
    Clean README or description text.
    Removes extra spaces and special characters.
    """

    if not text:
        return ""

    text = text.lower()

    # remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_keywords(text: str):
    """
    Extract potential technical keywords.
    """

    common_tech = [
        "python",
        "fastapi",
        "docker",
        "kubernetes",
        "machine learning",
        "deep learning",
        "ai",
        "llm",
        "langchain",
        "react",
        "node",
        "api",
        "database",
        "sql",
        "tensorflow",
        "pytorch"
    ]

    text = clean_text(text)

    detected = []

    for tech in common_tech:
        if tech in text:
            detected.append(tech)

    return list(set(detected))


def summarize_text(text: str, max_length: int = 200):
    """
    Basic text summarization for README previews.
    """

    if not text:
        return ""

    text = clean_text(text)

    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."