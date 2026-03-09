from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# --- TAMPILAN WEBSITE (HTML) ---
HTML_PAGE = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OMEGA SENSI AI - KAREEMXD</title>
    <style>
        body { background: #0a0a0c; color: #00f3ff; font-family: 'Courier New', monospace; text-align: center; padding: 20px; }
        .box { border: 2px solid #bc13fe; padding: 20px; border-radius: 15px; background: #111; max-width: 400px; margin: auto; box-shadow: 0 0 15px #bc13fe; }
        input { width: 80%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #00f3ff; background: #000; color: white; }
        button { padding: 10px 20px; background: linear-gradient(45deg, #00f3ff, #bc13fe); color: white; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
        #result { margin-top: 20px; text-align: left; font-size: 0.9em; line-height: 1.6; color: #fff; }
        .val { color: #00f3ff; font-weight: bold; }
    </style>
</head>
<body>
    <h1>OMEGA SENSI AI</h1>
    <div class="box">
        <p>MASUKKAN NAMA HP ANDA:</p>
        <input type="text" id="hp" placeholder="Contoh: POCO X3 Pro...">
        <br>
        <button onclick="proses()">GENERATE SENSI</button>
        <div id="result"></div>
    </div>

    <script>
        function proses() {
            const hp = document.getElementById('hp').value;
            if(!hp) return alert('Isi Nama HP-nya, Sultan!');
            const res = document.getElementById('result');
            res.innerHTML = "CALCULATING SCRIPT FOR " + hp + "...";
            
            // Simulasi Logika Sultan
            setTimeout(() => {
                const g = Math.floor(Math.random() * (100 - 95 + 1)) + 95;
                const r = g - 5;
                res.innerHTML = `
                    <hr>
                    STATUS: <span style="color:lime">ACTIVE</span><br>
                    GENERAL: <span class="val">${g}</span><br>
                    RED DOT: <span class="val">${r}</span><br>
                    DPI: <span class="val">580</span><br>
                    ACCURACY: <span class="val">91.4% HEADSHOT RATE</span><br>
                    <p style="font-size:0.7em; color:yellow italic">Gunakan U-Shape Drag untuk hasil maksimal!</p>
                `;
            }, 1000);
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return HTML_PAGE

# app = app untuk Vercel
app = app
