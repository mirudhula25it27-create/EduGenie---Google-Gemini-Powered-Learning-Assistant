from gemini_client import gemini_generate

def summarize_text(text: str) -> str:
    text = text.strip()
    if not text:
        return "Please enter text to summarize."

    prompt = """Summarize the following educational passage.
Keep the essential facts and ideas, remove redundancy, and use clear concise language.
Prefer a short paragraph followed by key points when helpful.

PASSAGE:
""" + text
    return gemini_generate(prompt)
