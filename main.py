import os
from flask import Flask, render_template, request, jsonify
from brain_ai import calculate_unique_sensi
from assistant import get_assistant_advice

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    device = data.get('device', 'Samsung Galaxy S25 Ultra')
    settings = calculate_unique_sensi(device)
    advice = get_assistant_advice(device)
    return jsonify({"settings": settings, "advice": advice})

if __name__ == "__main__":
    # Penting: Koyeb membutuhkan port dari environment variable atau default 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
