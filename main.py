from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# --- TAMPILAN FULL SPEK SULTAN ---
HTML_PAGE = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OMEGA SENSI AI V4 - KAREEMXD</title>
    <style>
        :root { --neon: #00f3ff; --purple: #bc13fe; }
        body { background: #050505; color: white; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 20px; }
        .container { max-width: 500px; margin: auto; border: 2px solid var(--purple); border-radius: 20px; background: #0f0f12; padding: 25px; box-shadow: 0 0 30px rgba(188, 19, 254, 0.4); }
        h1 { color: var(--neon); text-transform: uppercase; letter-spacing: 3px; text-shadow: 0 0 10px var(--neon); font-size: 1.5rem; }
        input { width: 100%; padding: 15px; border-radius: 10px; border: 1px solid var(--neon); background: #000; color: white; box-sizing: border-box; margin-bottom: 20px; font-weight: bold; }
        button { width: 100%; padding: 15px; background: linear-gradient(45deg, var(--neon), var(--purple)); color: white; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; text-transform: uppercase; transition: 0.3s; }
        button:hover { transform: scale(1.02); box-shadow: 0 0 20px var(--neon); }
        .result-box { margin-top: 25px; display: none; border-top: 1px solid #333; padding-top: 20px; animation: fadeIn 0.5s; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
        .item { background: #1a1a1f; padding: 12px; border-radius: 8px; border-left: 4px solid var(--neon); }
        .label { font-size: 0.7rem; color: #888; text-transform: uppercase; }
        .value { font-size: 1.2rem; font-weight: bold; color: var(--neon); }
        .tips { margin-top: 20px; padding: 15px; background: rgba(0, 243, 255, 0.1); border-radius: 10px; border: 1px dashed var(--neon); font-size: 0.85rem; line-height: 1.5; color: #ddd; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    </style>
</head>
<body>
    <div class="container">
        <h1>OMEGA SENSI V4 PRO</h1>
        <p style="color:#888; font-size:0.8rem;">ENGINE BY KAREEMXD - AUTO LICIN & HEADSHOT</p>
        <input type="text" id="hp" placeholder="NAMA HP (Contoh: ASUS ROG 8)...">
        <button onclick="generate()">GENERATE FULL SCRIPT</button>

        <div id="result" class="result-box">
            <div class="grid" id="mainGrid"></div>
            <div class="tips" id="tipsArea"></div>
            <p style="text-align:center; color:lime; font-weight:bold; margin-top:15px;">ACCURACY: 99.8% AIM LOCK</p>
        </div>
    </div>

    <script>
        function generate() {
            const hp = document.getElementById('hp').value;
            if(!hp) return alert('Masukkan Merk HP, Yang Mulia!');
            
            document.querySelector('button').innerText = "INJECTING SCRIPT...";
            
            setTimeout(() => {
                const settings = [
                    {n: "Lihat Sekeliling", v: Math.floor(Math.random() * (200 - 185 + 1)) + 185},
                    {n: "Red Dot Sight", v: Math.floor(Math.random() * (195 - 170 + 1)) + 170},
                    {n: "2X Scope", v: Math.floor(Math.random() * (190 - 160 + 1)) + 160},
                    {n: "4X Scope", v: Math.floor(Math.random() * (185 - 150 + 1)) + 150},
                    {n: "Sniper Scope", v: Math.floor(Math.random() * (120 - 80 + 1)) + 80},
                    {n: "Free Look", v: Math.floor(Math.random() * (200 - 150 + 1)) + 150},
                    {n: "DPI", v: Math.floor(Math.random() * (800 - 400 + 1)) + 400},
                    {n: "Tombol Tembak", v: Math.floor(Math.random() * (55 - 42 + 1)) + 42 + "%"}
                ];

                let gridHtml = "";
                settings.forEach(s => {
                    gridHtml += `<div class="item"><div class="label">${s.n}</div><div class="value">${s.v}</div></div>`;
                });

                document.getElementById('mainGrid').innerHTML = gridHtml;
                document.getElementById('tipsArea').innerHTML = `
                    <strong>SULTAN TIPS (${hp}):</strong><br>
                    1. Gunakan <strong>U-Shape Drag</strong> untuk jarak dekat.<br>
                    2. Aktifkan <strong>Pointer Speed</strong> maksimal di pengaturan HP.<br>
                    3. Bersihkan layar dengan kain microfiber agar licin maksimal!<br>
                    4. Atur <strong>Grafik ke Smooth</strong> agar FPS stabil dan Aim tidak berat.
                `;
                
                document.getElementById('result').style.display = 'block';
                document.querySelector('button').innerText = "RE-GENERATE SCRIPT";
            }, 1500);
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return HTML_PAGE

app = app
