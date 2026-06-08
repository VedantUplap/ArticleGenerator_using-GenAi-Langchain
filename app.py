from flask import Flask, render_template, request
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os


load_dotenv()

app = Flask(__name__)


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)


article_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
You are a professional content writer.

Write a detailed article on the topic: {topic}

Instructions:
1. Create an attractive title.
2. Use proper headings and subheadings.
3. Explain concepts clearly.
4. Include examples where relevant.
5. End with a conclusion.

Generate the article:
"""
)

# LCEL Chain
article_chain = article_prompt | llm

@app.route("/", methods=["GET", "POST"])
def home():

    article = ""
    error = ""

    if request.method == "POST":

        topic = request.form.get("topic")

        try:
            response = article_chain.invoke({
                "topic": topic
            })

            article = response.content

        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        article=article,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)