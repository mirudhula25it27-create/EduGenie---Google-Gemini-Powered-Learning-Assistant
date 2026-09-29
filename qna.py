from gemini_client import gemini_generate

def answer_question(question: str) -> str:
    question = question.strip()
    if not question:
        return "Please enter a question."

    prompt = """You are EduGenie, an educational assistant.
Answer the student's question accurately and concisely.
Use plain language. If the question is academic, show the key reasoning or steps.
Do not invent facts when you are uncertain.

Student question:
""" + question
    return gemini_generate(prompt)
