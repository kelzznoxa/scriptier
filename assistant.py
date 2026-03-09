def get_assistant_advice(device):
    advice_list = [
        "Gunakan teknik 'U-Shape Drag' untuk respon maksimal.",
        "Pastikan layar bersih dari minyak agar licin saat Jumpshot.",
        "Aktifkan 'Pointer Speed' maksimal di pengaturan sistem.",
        "Tarik tombol tembak sedikit ke arah kiri sebelum ke atas."
    ]
    random_advice = advice_list[hash(device) % len(advice_list)]
    return f"Sultan Choice: {random_advice}"
