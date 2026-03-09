from flask import Flask, request, jsonify

app = Flask(__name__)

# --- TAMPILAN FULL SPEK 200 (OMNISCIENT ENGINE) ---
HTML_PAGE = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OMEGA SENSI AI V5 - KAREEMXD</title>
    <style>
        :root { --neon: #00f3ff; --purple: #bc13fe; --dark: #050505; }
        body { background: var(--dark); color: white; font-family: 'Orbitron', sans-serif; margin: 0; padding: 15px; }
        .container { max-width: 450px; margin: auto; border: 2px solid var(--purple); border-radius: 20px; background: #0f0f12; padding: 20px; box-shadow: 0 0 30px rgba(188, 19, 254, 0.4); border-bottom: 5px solid var(--neon); }
        h1 { color: var(--neon); text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 10px var(--neon); font-size: 1.4rem; text-align: center; }
        input { width: 100%; padding: 15px; border-radius: 10px; border: 1px solid var(--neon); background: #000; color: white; box-sizing: border-box; margin-bottom: 15px; text-align: center; font-size: 1rem; }
        button { width: 100%; padding: 15px; background: linear-gradient(45deg, var(--neon), var(--purple)); color: white; border: none; border-radius: 10px; cursor: pointer; font-weight: bold; text-transform: uppercase; font-size: 1rem; transition: 0.3s; }
        button:hover { transform: scale(1.02); box-shadow: 0 0 20px var(--neon); }
        
        .result-area { margin-top: 25px; display: none; animation: slideUp 0.6s ease; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 15px; }
        .item { background: #1a1a1f; padding: 12px; border-radius: 8px; border-bottom: 2px solid var(--purple); text-align: center; }
        .label { font-size: 0.65rem; color: #888; text-transform: uppercase; margin-bottom: 5px; }
        .value { font-size: 1.3rem; font-weight: bold; color: var(--neon); }
        
        .special-box { background: rgba(0, 243, 255, 0.1); border: 1px dashed var(--neon); border-radius: 10px; padding: 15px; margin-top: 15px; }
        .special-title { font-size: 0.8rem; color: var(--neon); font-weight: bold; border-bottom: 1px solid var(--neon); margin-bottom: 10px; padding-bottom: 5px; }
        .tips-list { text-align: left; font-size: 0.75rem; color: #ccc; line-height: 1.6; }
        
        @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .footer { font-size: 0.6rem; color: #444; margin-top: 20px; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <h1>OMEGA SENSI V5</h1>
        <p style="text-align:center; font-size:0.7rem; color:rgba(255,255,255,0.5); margin-top:-10px;">AUTHORIZED BY KAREEMXD</p>
        
        <input type="text" id="device" placeholder="MASUKKAN NAMA HP ANDA...">
        <button onclick="inject()">GENERATE FULL DATA</button>

        <div id="resultArea" class="result-area">
            <div class="grid">
                <div class="item"><div class="label">Lihat Sekeliling</div><div class="value" id="v1">0</div></div>
                <div class="item"><div class="label">Red Dot Sight</div><div class="value" id="v2">0</div></div>
                <div class="item"><div class="label">2X Scope</div><div class="value" id="v3">0</div></div>
                <div class="item"><div class="label">4X Scope</div><div class="value" id="v4">0</div></div>
                <div class="item"><div class="label">Sniper Scope</div><div class="value" id="v5">0</div></div>
                <div class="item"><div class="label">Free Look</div><div class="value" id="v6">0</div></div>
                <div class="item" style="border-color: var(--neon);"><div class="label">DPI HP</div><div class="value" id="v7">0</div></div>
                <div class="item" style="border-color: var(--neon);"><div class="label">Tombol Tembak</div><div class="value" id="v8">0</div></div>
            </div>

            <div class="special-box">
                <div class="special-title">SULTAN SECRET TIPS (LICIN MAX)</div>
                <div class="tips-list" id="tips"></div>
            </div>
            
            <p style="text-align:center; color:lime; font-size:0.8rem; margin-top:15px; text-shadow:0 0 5px lime;">● AIM LOCK 99.9% ACTIVE</p>
        </div>
        <div class="footer">SERVER STATUS: ENCRYPTED BY SUPREME AI</div>
    </div>

    <script>
        function inject() {
            const dev = document.getElementById('device').value;
            if(!dev) return alert('Nama HP-nya mana, Yang Mulia?');
            
            document.querySelector('button').innerText = "INJECTING SCRIPT...";
            
            setTimeout(() => {
                // Skala Dewa 170-200
                document.getElementById('v1').innerText = Math.floor(Math.random() * (200 - 188 + 1)) + 188;
                document.getElementById('v2').innerText = Math.floor(Math.random() * (195 - 180 + 1)) + 180;
                document.getElementById('v3').innerText = Math.floor(Math.random() * (190 - 175 + 1)) + 175;
                document.getElementById('v4').innerText = Math.floor(Math.random() * (185 - 170 + 1)) + 170;
                document.getElementById('v5').innerText = Math.floor(Math.random() * (120 - 90 + 1)) + 90;
                document.getElementById('v6').innerText = Math.floor(Math.random() * (200 - 180 + 1)) + 180;
                
                // DPI & Button
                document.getElementById('v7').innerText = Math.floor(Math.random() * (900 - 550 + 1)) + 550;
                document.getElementById('v8').innerText = Math.floor(Math.random() * (52 - 42 + 1)) + 42 + "%";
                
                document.getElementById('tips').innerHTML = `
                    • Gunakan <strong>U-Shape Drag</strong> untuk Shotgun.<br>
                    • <strong>Pointer Speed</strong> set ke FULL/Kanan.<br>
                    • Atur <strong>Skala Animasi</strong> ke 0.5x di Opsi Pengembang.<br>
                    • Pasang <strong>Bedak/Sarung Jempol</strong> biar Licin Enak!
                `;
                
                document.getElementById('resultArea').style.display = 'block';
                document.querySelector('button').innerText = "RE-GENERATE SCRIPT";
                window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
            }, 1200);
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return HTML_PAGE

app = app
