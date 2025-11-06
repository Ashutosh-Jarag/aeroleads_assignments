import os
import csv
from flask import Flask, render_template, request, redirect, url_for
from twilio.rest import Client
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

app = Flask(__name__)

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GOOGLE_API_KEY)

prompt = PromptTemplate(
    input_variables=["product", "lead_name"],
    template="Create a friendly short phone call script to introduce {product} to {lead_name}. Keep it under 80 words."
)

if not os.path.exists("call_logs.csv"):
    with open("call_logs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Lead Name", "Phone", "Product", "Message", "Status"])

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        lead_name = request.form["lead_name"]
        phone = request.form["phone"]
        product = request.form["product"]

        ai_prompt = prompt.format(product=product, lead_name=lead_name)
        ai_response = llm.invoke(ai_prompt)
        message = ai_response.content.strip()

        try:
            call = client.calls.create(
                to=phone,
                from_=TWILIO_PHONE,
                twiml=f"<Response><Say>{message}</Say></Response>"
            )
            status = "Success"
        except Exception as e:
            status = f"Failed: {str(e)}"

        with open("call_logs.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([lead_name, phone, product, message, status])

        return redirect(url_for("home"))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
