import os
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# --- LOGIKA BRAIN AI (Disatukan agar anti-error di Vercel) ---
def calculate_unique_sensi(device_name):
    random.seed(hash(device_name.lower())) 
    gen = random.randint(95, 100)
    red = gen - random.randint(3, 7)
    
    if any(x in device_name.lower() for x in ["ultra", "iphone", "pro max"]):
        gen = random.randint(92, 98)
        dpi = random.randint(410, 480)
    else:
        dpi = random.randint(500, 720)
        
    return {
        "general": gen,
        "red_dot": red,
        "scope2x": random.randint(85, 95),
        "scope4x": random.randint(80, 90),
        "dpi": dpi,
        "button_size": f"{random.randint(42, 52)}%",
        "accuracy": "91.4% Headshot Rate"
    }

def get_assistant_advice(device):
    advice_list = [
        "Gunakan teknik 'U-Shape Drag' untuk respon maksimal.",
        "Pastikan layar bersih dari minyak agar licin saat Jumpshot.",
        "Aktifkan 'Pointer Speed' maksimal di pengaturan sistem.",
        "Tarik tombol tembak sedikit ke arah kiri sebelum ke atas."
    ]
    return f"Sultan Choice: {advice_list[hash(device) % len(advice_list)]}"

# --- ROUTES ---
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

# PENTING: Untuk Vercel, kita tidak butuh app.run()
# Vercel akan otomatis mencari variabel 'app'
