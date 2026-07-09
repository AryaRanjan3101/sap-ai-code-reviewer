import os
from flask import Flask, request, jsonify, render_template
from google import genai

app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

SYSTEM_PROMPT = """You are a senior SAP ABAP developer with 15+ years of experience. Review the ABAP code 
  provided and give a structured review covering: 1. Performance Issues 2. Code Quality 3. Best Practices 4. 
  Security 5. Overall Rating out of 10. Be specific and give concrete suggestions."""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/review", methods=["POST"])
def review():
    code = request.json.get("code", "")
    if not code.strip():
        return jsonify({"error": "No code provided"}), 400
    prompt = f"{SYSTEM_PROMPT}\n\nReview this ABAP code:\n\n{code}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
      )
    return jsonify({"review": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
