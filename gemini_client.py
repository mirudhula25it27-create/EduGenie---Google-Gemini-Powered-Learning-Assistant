import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the same folder as this Python file
load_dotenv(Path(__file__).resolve().parent / ".env")

_client = None


def get_gemini_client():
    """Create the Google GenAI client lazily."""
    global _client

    if _client is not None:
        return _client

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    if not api_key:
        return None

    try:
        from google import genai

        _client = genai.Client(api_key=api_key)
        return _client

    except Exception:
        return None


def gemini_generate(prompt: str) -> str:
    client = get_gemini_client()

    if client is None:
        return (
            "Gemini API is not configured. "
            "Add GEMINI_API_KEY to the .env file and restart the application."
        )

    model = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        return (response.text or "").strip()

    except Exception as exc:
        return f"Gemini API error: {exc}"