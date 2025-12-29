from google import genai
from flask import Flask, request, jsonify, render_template
client = genai.Client(api_key="API KEY ")

# Change this line in your main.py
app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["message"]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return jsonify({"reply": response.text})

app.run(port="8000")
