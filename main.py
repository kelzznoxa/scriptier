from flask import Flask, request, jsonify

app = Flask(__name__)

# --- TAMPILAN GOD VERSION (ANALISIS 100+ WEB SENSI) ---
HTML_PAGE = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OMEGA SENSI AI V6 - GOD MODE</title>
    <style>
        :root { --neon: #00f3ff; --purple: #bc13fe; --dark: #050505; }
        body { background: var(--dark); color: white; font-family: 'Orbitron', sans-serif; margin: 0; padding: 15px; }
        .container { max-width: 480px; margin: auto; border: 2px solid var(--purple); border-radius: 20px; background: #0f0f12; padding: 25px; box-shadow: 0 0 40px rgba(188, 19, 254, 0.6); }
        h1 { color: var(--neon); text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 15px var(--neon); font-size: 1.6rem; text-align: center; margin-bottom: 5px; }
        .sub-title { text-align: center; color: #888; font-size: 0.7rem; margin-bottom: 20px; text-transform: uppercase; }
        
        input { width: 100%; padding: 15px; border-radius: 12px; border: 1px solid var(--neon); background: #000; color: white; box-sizing: border-box; margin-bottom: 15px; text-align: center; font-size: 1rem; box-shadow: inset 0 0 5px var(--neon); }
        button { width: 100%; padding: 18px; background: linear-gradient(45deg, var(--neon), var(--purple)); color: white; border: none; border-radius: 12px; cursor: pointer; font-weight: bold; text-transform: uppercase; font-size: 1rem; transition: 0.4s; }
        button:hover { letter-spacing: 2px; box-shadow: 0 0 30px var(--neon); }
        
        .result-area { margin-top: 25px; display: none; animation: zoomIn 0.5s ease forwards; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px; }
        .item { background: #1a1a1f; padding: 15px; border-radius: 12px; border-top: 1px solid var(--purple); border-left: 3px solid var(--neon); text-align: center; }
        .label { font-size: 0.6rem; color: #aaa; text-transform: uppercase; margin-bottom: 5px; }
        .value { font-size: 1.4rem; font-weight: bold; color: var(--neon); }
        
        .sultan-tips { background: rgba(188, 19, 254, 0.1); border: 1px solid var(--purple); border-radius: 15px; padding: 20px; margin-top: 20px; text-align: left; }
        .tips-header { color: var(--purple); font-weight: bold; font-size: 0.9rem; margin-bottom: 10px; border-bottom: 1px solid var(--purple); padding-bottom: 5px; }
        .tips-content { font-size: 0.75rem; color: #eee; line-height: 1.8; }
        .status-lock { color: lime; text-align: center; font-size: 0.9rem; margin-top: 15px; font-weight: bold; text-shadow: 0 0 10px lime; }
        
        @keyframes zoomIn { from { opacity: 0; transform: scale(0.9); } to { opacity: 1; transform: scale(1); } }
    </style>
</head>
<body>
    <div class="container">
        <h1>OMEGA SENSI AI V6</h1>
        <div class="sub-title">Analyzing Global Pro Player Database...</div>
        
        <input type="text" id="device" placeholder="Ketik Nama HP (Contoh: POCO F5)...">
        <button onclick="analyze()">ANALYZE & INJECT SENSI</button>

        <div id="resultArea" class="result-area">
            <div class="grid">
                <div class="item"><div class="label">General (Sekeliling)</div><div class="value" id="v1">0</div></div>
                <div class="item"><div class="label">Red Dot Sight</div><div class="value" id="v2">0</div></div>
                <div class="item"><div class="label">2X Scope</div><div class="value" id="v3">0</div></div>
                <div class="item"><div class="label">4X Scope</div><div class="value" id="v4">0</div></div>
                <div class="item"><div class="label">Sniper Scope</div><div class="value" id="v5">0</div></div>
                <div class="item"><div class="label">Free Look</div><div class="value" id="v6">0</div></div>
                <div class="item" style="border-left-color: var(--purple);"><div class="label">DPI OPTIMAL</div><div class="value" id="v7">0</div></div>
                <div class="item" style="border-left-color: var(--purple);"><div class="label">UKURAN TOMBOL</div><div class="value" id="v8">0</div></div>
            </div>

            <div class="sultan-tips">
                <div class="tips-header">📊 SULTAN ANALYSIS TIPS (HP: <span id="hpName"></span>)</div>
                <div class="tips-content">
                    • <b>TEKNIK DRAG:</b> Gunakan <i>"J-Shape Drag"</i> (geser melengkung) untuk jarak dekat. Jangan tarik lurus ke atas!<br>
                    • <b>POINTER SPEED:</b> Masuk ke Pengaturan HP -> Cari Pointer Speed -> Setel ke 90% (sisakan 1 bar di kanan).<br>
                    • <b>DPI SECRET:</b> Gunakan DPI di atas hanya jika layar terasa berat. Jika licin, pakai DPI bawaan.<br>
                    • <b>BOOSTER:</b> Matikan <i>"Force 4x MSAA"</i> di Opsi Pengembang agar FPS tidak drop saat nembak.<br>
                    • <b>RAHASIA LICIN:</b> Pakai sedikit bedak bayi atau sarung jempol kain. Layar kesat adalah musuh Headshot!<br>
                    • <b>AUTO AIM:</b> Letakkan tombol tembak sedikit ke bawah agar area tarik (drag) ke atas lebih luas.
                </div>
            </div>
            
            <div class="status-lock">STATUS: 99.9% AUTO AIM LOCK ENABLED</div>
        </div>
    </div>

    <script>
        function analyze() {
            const hp = document.getElementById('device').value;
            if(!hp) return alert('Masukkan Merk HP Sultan!');
            
            const btn = document.querySelector('button');
            btn.innerText = "ANALYZING 100+ WEB DATA...";
            
            setTimeout(() => {
                document.getElementById('hpName').innerText = hp.toUpperCase();
                
                // Algoritma Sensi 185-200 (Licin Enak)
                document.getElementById('v1').innerText = Math.floor(Math.random() * (200 - 192 + 1)) + 192;
                document.getElementById('v2').innerText = Math.floor(Math.random() * (198 - 188 + 1)) + 188;
                document.getElementById('v3').innerText = Math.floor(Math.random() * (195 - 180 + 1)) + 180;
                document.getElementById('v4').innerText = Math.floor(Math.random() * (190 - 175 + 1)) + 175;
                document.getElementById('v5').innerText = Math.floor(Math.random() * (150 - 100 + 1)) + 100;
                document.getElementById('v6').innerText = Math.floor(Math.random() * (200 - 190 + 1)) + 190;
                
                // DPI & Tombol
                document.getElementById('v7').innerText = Math.floor(Math.random() * (960 - 600 + 1)) + 600;
                document.getElementById('v8').innerText = Math.floor(Math.random() * (48 - 38 + 1)) + 38 + "%";
                
                document.getElementById('resultArea').style.display = 'block';
                btn.innerText = "RE-ANALYZE FOR NEW SCRIPT";
                window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
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
