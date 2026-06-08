#  AI Article Generator

A Generative AI web application that creates high-quality articles from any topic using **LangChain**, **Groq's Llama 3.3**, and **Flask**.

##  Features

* Generate detailed AI-powered articles instantly
* Powered by **Llama 3.3** via Groq API
* Modular prompt engineering using LangChain Prompt Templates
* Built with LCEL (LangChain Expression Language)
* Simple and responsive Flask-based web interface


##  Tech Stack

* Python
* Flask
* LangChain
* Groq API
* Llama 3.3
* HTML/CSS
* Python-dotenv

##  Project Structure

```bash
ArticleGenerator/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .env
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ArticleGenerator
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## How It Works

1. User enters a topic.
2. LangChain PromptTemplate formats the prompt.
3. Groq's Llama 3.3 generates the article.
4. Flask renders the output on the web interface.

## Future Improvements

* Article length selection
* Tone customization (Formal, Casual, Technical)
* Export articles as PDF
* Article history and saving
* Multi-language support

##  Author

**Vedant Uplap**
B.Tech CSE Student 

---
