import os

def explain_topic(topic: str) -> str:
    topic = topic.strip()
    if not topic:
        return "Please enter a topic to explain."

    # The project specification uses LaMini-Flan-T5-783M for explanations.
    # Set USE_LOCAL_EXPLAINER=true to load it locally.
    if os.getenv("USE_LOCAL_EXPLAINER", "false").lower() == "true":
        try:
            from transformers import pipeline
            generator = pipeline(
                "text2text-generation",
                model="MBZUAI/LaMini-Flan-T5-783M",
                max_new_tokens=220
            )
            prompt = (
                "Explain the following educational topic simply and clearly "
                "for a beginner. Use short paragraphs and examples when useful:\n\n"
                + topic
            )
            return generator(prompt)[0]["generated_text"].strip()
        except Exception as exc:
            return f"Local explanation model error: {exc}"

    # Cloud fallback keeps the default install lightweight.
    from gemini_client import gemini_generate
    return gemini_generate(
        "Explain this educational topic in simple, concise language for a beginner. "
        "Include a small example if appropriate.\n\nTopic: " + topic
    )
