import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END


# Load environment
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Flask
app = Flask(__name__)
os.makedirs("blog", exist_ok=True)

# Configure LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY)

# Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template=(
        "Write a detailed, SEO-friendly blog post (500-700 words) about '{topic}'. "
        "Include markdown headings, code examples if relevant, and a short conclusion."
    )
)

# Define generation logic for LangGraph
def generate_article(state):
    topic = state["topic"]
    final_prompt = prompt.format(topic=topic)
    response = llm.invoke(final_prompt)
    content = response.content
    return {"topic": topic, "content": content}

# LangGraph setup
builder = StateGraph(dict)
builder.add_node("generate", generate_article)
builder.set_entry_point("generate")
builder.add_edge("generate", END)
graph = builder.compile()

# Flask routes
@app.route("/", methods=["GET", "POST"])
def home():
    articles = []
    if request.method == "POST":
        titles = request.form["titles"].split("\n")
        for title in titles:
            title = title.strip()
            if not title:
                continue
            result = graph.invoke({"topic": title})
            articles.append(result)
            
            # Save blog to /blog folder
            filename = f"blog/{title.replace(' ', '_')}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n{result['content']}")
    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
