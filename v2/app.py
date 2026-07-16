
import os
from flask import Flask, request, jsonify, render_template
from google import genai
from rag import get_retriever
  
app = Flask(__name__)

client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
retriever = None
  
def get_rag_retriever():
    global retriever
    if retriever is None:
        print("Building knowledge base from Clean ABAP PDF...")
        retriever = get_retriever()
        print("Knowledge base ready.")
    return retriever

SYSTEM_PROMPT = """You are an expert SAP ABAP Code Reviewer specializing in Clean Core, S/4HANA development standards, and modern
ABAP practices.
   
You have been provided with relevant excerpts from SAP's official Clean ABAP Style Guide below.
Your reviews must be grounded in these official guidelines — cite them where applicable.

CLEAN ABAP GUIDELINES: 
{guidelines}

Review the ABAP code and give a structured review covering:

1. PERFORMANCE ISSUES
- SELECT * usage, nested SELECTs in loops, missing WHERE clauses
- Use FOR ALL ENTRIES instead of nested SELECT

2. MODERN ABAP & CLEAN ABAP
- Inline declarations, string templates, FIELD-SYMBOL usage
- Violations of the Clean ABAP guidelines provided above
  
3. CODE QUALITY
- Naming conventions, hardcoded values, deep nesting
- Single responsibility, dead code

4. OBJECT ORIENTED ABAP
- Proper class/interface usage, avoid FORM routines
- Exception handling with CX_ classes

5. SECURITY
- Authority checks, dynamic SQL risks

6. S/4HANA SPECIFIC
- Clean core compliance, avoid compatibility views

7. OVERALL RATING out of 10 with one line summary"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/review", methods=["POST"])
def review():
    code = request.json.get("code", "")
    if not code.strip():
        return jsonify({"error": "No code provided"}), 400

    r = get_rag_retriever()   
    docs = r.invoke(code)
    guidelines = "\n\n".join([doc.page_content for doc in docs])

    prompt = SYSTEM_PROMPT.format(guidelines=guidelines) + f"\n\nReview this ABAP code:\n\n{code}"
  
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
      )
    return jsonify({"review": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=False)