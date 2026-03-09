from flask import Flask, request, jsonify

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHADOW SENSI AI - V6 PRO</title>
    <style>
        :root { --neon: #00f3ff; --purple: #bc13fe; --dark: #050505; }
        body { background: var(--dark); color: white; font-family: 'Orbitron', sans-serif; margin: 0; padding: 10px; }
        .container { max-width: 480px; margin: auto; border: 2px solid var(--purple); border-radius: 20px; background: #0f0f12; padding: 20px; box-shadow: 0 0 40px rgba(188, 19, 254, 0.6); }
        h1 { color: var(--neon); text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 15px var(--neon); font-size: 1.4rem; text-align: center; margin-bottom: 5px; }
        .sub-title { text-align: center; color: #888; font-size: 0.6rem; margin-bottom: 20px; text-transform: uppercase; }
        input { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid var(--neon); background: #000; color: white; box-sizing: border-box; margin-bottom: 15px; text-align: center; outline: none; }
        button { width: 100%; padding: 18px; background: linear-gradient(45deg, var(--neon), var(--purple)); color: white; border: none; border-radius: 12px; cursor: pointer; font-weight: bold; text-transform: uppercase; }
        .result-area { margin-top: 25px; display: none; }
        .grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; }
        .item { background: #1a1a1f; padding: 10px; border-radius: 10px; border-bottom: 2px solid var(--purple); text-align: center; }
        .value { font-size: 1.2rem; font-weight: bold; color: var(--neon); }
        .label { font-size: 0.55rem; color: #aaa; margin-top: 5px; }
        .tips-box { background: rgba(0, 243, 255, 0.05); border: 1px solid var(--neon); border-radius: 15px; padding: 15px; margin-top: 20px; font-size: 0.7rem; line-height: 1.5; }
    </style>
</head>
<body>
    <div class="container">
        <h1>SHADOW SENSI AI</h1>
        <div class="sub-title">System Analysis v6.0.3 - Balanced Mode</div>
        <input type="text" id="device" placeholder="NAMA HP ANDA...">
        <button onclick="analyze()">INJECT SHADOW SCRIPT</button>
        
        <div id="resultArea" class="result-area">
            <div class="grid">
                <div class="item"><div class="value" id="v1">0</div><div class="label">GENERAL</div></div>
                <div class="item"><div class="value" id="v2">0</div><div class="label">RED DOT</div></div>
                <div class="item"><div class="value" id="v3">0</div><div class="label">2X SCOPE</div></div>
                <div class="item"><div class="value" id="v4">0</div><div class="label">4X SCOPE</div></div>
                <div class="item"><div class="value" id="v5">0</div><div class="label">SNIPER</div></div>
                <div class="item"><div class="value" id="v6">0</div><div class="label">FREE LOOK</div></div>
                <div class="item" style="grid-column: span 2;"><div class="value" id="v7">0</div><div class="label">DPI OPTIMAL</div></div>
                <div class="item"><div class="value" id="v8">0</div><div class="label">BUTTON</div></div>
            </div>
            
            <div class="tips-box">
                <b style="color:var(--neon)">⚡ TOTEM OPTIMIZATION:</b><br>
                • Sensi diatur otomatis agar tidak <i>over-drag</i>.<br>
                • Bersihkan Cache FF sebelum login.<br>
                • DPI sudah disesuaikan agar layar tidak lag.<br>
                • Fokus ke J-Shape drag di jarak menengah.
            </div>
        </div>
    </div>
    <script>
        function analyze() {
            // ALGORITMA SENSI BALANCED (Gak asal-asalan, Random tapi masuk akal)
            document.getElementById('v1').innerText = Math.floor(Math.random() * (195 - 170 + 1)) + 170; // General tetap tinggi
            document.getElementById('v2').innerText = Math.floor(Math.random() * (180 - 150 + 1)) + 150; // Red dot stabil
            document.getElementById('v3').innerText = Math.floor(Math.random() * (160 - 120 + 1)) + 120; // 2x Scope
            document.getElementById('v4').innerText = Math.floor(Math.random() * (150 - 110 + 1)) + 110; // 4x Scope
            document.getElementById('v5').innerText = Math.floor(Math.random() * (140 - 100 + 1)) + 100; // Sniper (Gak perlu terlalu licin)
            document.getElementById('v6').innerText = Math.floor(Math.random() * (175 - 130 + 1)) + 130; // Free Look
            
            // DPI OPTIMAL (Tetap turun sesuai permintaan: 450 - 580)
            document.getElementById('v7').innerText = Math.floor(Math.random() * (580 - 450 + 1)) + 450;
            
            // Tombol Tembak Random (40% - 55%)
            document.getElementById('v8').innerText = Math.floor(Math.random() * (55 - 40 + 1)) + 40 + "%";
            
            document.getElementById('resultArea').style.display = 'block';
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return HTML_PAGE
