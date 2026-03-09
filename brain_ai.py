import random

def calculate_unique_sensi(device_name):
    # Menggunakan nama HP sebagai 'seed' agar hasilnya konsisten tapi unik tiap model
    random.seed(hash(device_name.lower())) 
    
    # Logika Dasar Sensi Sultan
    gen = random.randint(95, 100)
    red = gen - random.randint(3, 7)
    
    # Penyesuaian khusus Flagship (S25 Ultra, iPhone 16 Pro Max, dsb)
    if any(x in device_name.lower() for x in ["ultra", "iphone", "pro max"]):
        gen = random.randint(92, 98) # Layar dewa tak perlu sensi mentok
        dpi = random.randint(410, 480)
    else:
        dpi = random.randint(500, 720) # HP seri menengah butuh DPI lebih tinggi
        
    return {
        "general": gen,
        "red_dot": red,
        "scope2x": random.randint(85, 95),
        "scope4x": random.randint(80, 90),
        "dpi": dpi,
        "button_size": f"{random.randint(42, 52)}%",
        "accuracy": "91.4% Headshot Rate"
    }
