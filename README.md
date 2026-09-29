# EduGenie — Google Gemini Powered Learning Assistant

EduGenie is a FastAPI + HTML/CSS educational assistant based on the supplied project specification.

## Features

- Q&A: `/qa`
- Concept explanation: `/explain`
- 3-question MCQ generation: `/quiz`
- Passage summarization: `/summarize`
- Beginner-to-advanced learning recommendations: `/learn/recommendations`
- Browser frontend at `/`

The specification describes Gemini 1.5 Pro for Q&A, summarization, quiz generation and learning paths, and LaMini-Flan-T5-783M for explanations.

## Requirements

- Python 3.10+
- A Gemini API key for cloud AI features

## Windows setup

Open Command Prompt or PowerShell inside this folder:

```text
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
```

Open `.env` and replace `PASTE_YOUR_GEMINI_API_KEY_HERE` with your Gemini API key.

Then run:

```text
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## macOS / Linux

```text
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env`, then:

```text
uvicorn main:app --reload
```

## Local explanation model

The original specification calls for LaMini-Flan-T5-783M for concept explanation.

To enable it:

```text
USE_LOCAL_EXPLAINER=true
```

The first explanation request will download the model from Hugging Face and requires substantially more disk space and RAM than the default cloud-explanation mode.

## API examples

### Q&A

POST `/qa`

```json
{"text":"What is the largest ocean?"}
```

### Explain

POST `/explain`

```json
{"text":"Pythagoras theorem"}
```

### Quiz

POST `/quiz`

```json
{"text":"The Earth revolves around the Sun..."}
```

### Summarize

POST `/summarize`

```json
{"text":"Long educational passage here..."}
```

### Learning path

POST `/learn/recommendations`

```json
{"topic":"SQL"}
```

## Project structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Notes

The supplied document specifies Gemini 1.5 Pro and LaMini-Flan-T5-783M. Google model availability can change over time, so `GEMINI_MODEL` is configurable rather than hard-coded. The application itself follows the documented module and endpoint architecture.
