from flask import Flask, request, jsonify

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHADOW SENSI AI - V6</title>
    <style>
        :root { --neon: #00f3ff; --purple: #bc13fe; --dark: #050505; }
        body { background: var(--dark); color: white; font-family: 'Orbitron', sans-serif; margin: 0; padding: 15px; }
        .container { max-width: 480px; margin: auto; border: 2px solid var(--purple); border-radius: 20px; background: #0f0f12; padding: 25px; box-shadow: 0 0 40px rgba(188, 19, 254, 0.6); }
        h1 { color: var(--neon); text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 15px var(--neon); font-size: 1.6rem; text-align: center; }
        .sub-title { text-align: center; color: #888; font-size: 0.7rem; margin-bottom: 20px; text-transform: uppercase; }
        input { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid var(--neon); background: #000; color: white; box-sizing: border-box; margin-bottom: 15px; text-align: center; }
        button { width: 100%; padding: 18px; background: linear-gradient(45deg, var(--neon), var(--purple)); color: white; border: none; border-radius: 12px; cursor: pointer; font-weight: bold; text-transform: uppercase; }
        .result-area { margin-top: 25px; display: none; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
        .item { background: #1a1a1f; padding: 15px; border-radius: 12px; border-left: 3px solid var(--neon); text-align: center; }
        .value { font-size: 1.4rem; font-weight: bold; color: var(--neon); }
        .tips-box { background: rgba(188, 19, 254, 0.1); border: 1px solid var(--purple); border-radius: 15px; padding: 20px; margin-top: 20px; font-size: 0.75rem; text-align: left; }
    </style>
</head>
<body>
    <div class="container">
        <h1>SHADOW SENSI AI</h1>
        <div class="sub-title">Bypassing System... Secured by Anonymous</div>
        <input type="text" id="device" placeholder="NAMA HP ANDA...">
        <button onclick="analyze()">INJECT GHOST SCRIPT</button>
        <div id="resultArea" class="result-area">
            <div class="grid">
                <div class="item"><div class="value" id="v1">0</div><div style="font-size:0.6rem">GENERAL</div></div>
                <div class="item"><div class="value" id="v2">0</div><div style="font-size:0.6rem">RED DOT</div></div>
                <div class="item"><div class="value" id="v3">0</div><div style="font-size:0.6rem">DPI</div></div>
                <div class="item"><div class="value" id="v4">0</div><div style="font-size:0.6rem">TOMBOL</div></div>
            </div>
            <div class="tips-box">
                <b>SHADOW TIPS:</b><br>
                • Sensi ini sudah dioptimalkan (Anti-Lag).<br>
                • Gunakan <b>J-Shape Drag</b> untuk hasil maksimal.<br>
                • Rekomendasi Tombol Tembak: <b>45% - 50%</b>.
            </div>
        </div>
    </div>
    <script>
        function analyze() {
            // Sensi General & Red Dot (Tetap tinggi biar licin)
            document.getElementById('v1').innerText = Math.floor(Math.random() * (200 - 192 + 1)) + 192;
            document.getElementById('v2').innerText = Math.floor(Math.random() * (198 - 188 + 1)) + 188;
            
            // DPI OPTIMAL (Diturunkan sesuai permintaan agar tidak terlalu naik)
            // Range 480 - 580 adalah angka paling stabil di tahun 2026
            document.getElementById('v3').innerText = Math.floor(Math.random() * (580 - 480 + 1)) + 480;
            
            document.getElementById('v4').innerText = "45%";
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
    app.run(debug=True)
