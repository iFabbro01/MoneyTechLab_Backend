from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("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")

@app.route("/ai", methods=["POST"])
def ai():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800
        )
        return jsonify({"response": response.choices[0].message["content"].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "MoneyTech Lab AI backend attivo"
