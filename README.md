# AI Article Generator

A Generative AI web application built using:

- Flask
- LangChain
- Groq (Llama 3)
- Prompt Templates
- LCEL Chains

## Features

- Generate detailed articles from any topic
- Uses Llama 3.3 through Groq
- Built with LangChain PromptTemplate
- Clean Flask UI

## Installation

```bash
git clone <repo-url>
cd ArticleGenerator

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Tech Stack

- Flask
- LangChain
- Groq
- HTML/CSS