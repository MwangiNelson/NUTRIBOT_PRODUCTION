from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/generate-text', methods=['POST'])
def generate_text():
    input_text = request.json.get('text')
    response = requests.post(
        "https://api-inference.huggingface.co/models/MwangiNelson/NutriBot",
        headers={"Authorization": "Bearer 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"},
        json={"inputs": input_text, "parameters": {"max_length": 50}}
    )
    if response.status_code == 200:
        return jsonify(response.json()[0]['generated_text'])
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
