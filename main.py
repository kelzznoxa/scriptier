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
        .sub-title { text-align: center; color: #888; font-size: 0.6rem; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 1px; }
        input { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid var(--neon); background: #000; color: white; box-sizing: border-box; margin-bottom: 15px; text-align: center; outline: none; }
        button { width: 100%; padding: 18px; background: linear-gradient(45deg, var(--neon), var(--purple)); color: white; border: none; border-radius: 12px; cursor: pointer; font-weight: bold; text-transform: uppercase; transition: 0.3s; }
        button:hover { opacity: 0.8; box-shadow: 0 0 20px var(--neon); }
        .result-area { margin-top: 25px; display: none; }
        .grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; }
        .item { background: #1a1a1f; padding: 10px; border-radius: 10px; border-bottom: 2px solid var(--purple); text-align: center; }
        .value { font-size: 1.2rem; font-weight: bold; color: var(--neon); }
        .label { font-size: 0.55rem; color: #aaa; margin-top: 5px; }
        .tips-box { background: rgba(0, 243, 255, 0.05); border: 1px solid var(--neon); border-radius: 15px; padding: 15px; margin-top: 20px; font-size: 0.7rem; line-height: 1.5; }
        .totem-title { color: var(--neon); font-weight: bold; display: block; margin-bottom: 5px; text-transform: uppercase; }
    </style>
</head>
<body>
    <div class="container">
        <h1>SHADOW SENSI AI</h1>
        <div class="sub-title">System Analysis v6.0.2 - Optimized for 2026</div>
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
                <div class="item"><div class="value" id="v8">45%</div><div class="label">BUTTON</div></div>
            </div>
            
            <div class="tips-box">
                <span class="totem-title">⚡ TOTEM OPTIMIZATION:</span>
                • Bersihkan Cache Free Fire sebelum login.<br>
                • Aktifkan <b>Opsi Pengembang</b> > Force 4x MSAA.<br>
                • Gunakan <b>Game Turbo</b> untuk stabilkan FPS Totem.<br>
                • Sensi ini bypass limit sistem (Auto Aim Lock).
            </div>
        </div>
    </div>
    <script>
        function analyze() {
            // ALL SENSI FULL SAKTI (190 - 200)
            document.getElementById('v1').innerText = Math.floor(Math.random() * (200 - 195 + 1)) + 195;
            document.getElementById('v2').innerText = Math.floor(Math.random() * (200 - 192 + 1)) + 192;
            document.getElementById('v3').innerText = Math.floor(Math.random() * (200 - 190 + 1)) + 190;
            document.getElementById('v4').innerText = Math.floor(Math.random() * (200 - 194 + 1)) + 194;
            document.getElementById('v5').innerText = Math.floor(Math.random() * (200 - 185 + 1)) + 185;
            document.getElementById('v6').innerText = Math.floor(Math.random() * (200 - 190 + 1)) + 190;
            
            // DPI TETAP OPTIMAL (Diturunkan sesuai permintaan)
            document.getElementById('v7').innerText = Math.floor(Math.random() * (580 - 520 + 1)) + 520;
            
            document.getElementById('resultArea').style.display = 'block';
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return HTML_PAGE

if __name__ == "__main__":
    app.run()
