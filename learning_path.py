from gemini_client import gemini_generate

def get_learning_recommendations(topic: str) -> str:
    topic = topic.strip()
    if not topic:
        return "Please enter a topic."

    prompt = """Create a personalized learning path for the topic below.
Organize it from beginner to intermediate to advanced.
For each stage, include concepts to learn, a suggested sequence, practical activities,
and useful resource types (videos, articles, books, documentation).
Keep the plan actionable and adaptable.

TOPIC:
""" + topic
    return gemini_generate(prompt)
