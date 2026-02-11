def rata_rata(nilai):
    # 1. Validasi jika list kosong
    if len(nilai) == 0:
        return "Data kosong"
    
    # 2. Hitung rata-rata
    total = sum(nilai)
    rata = total / len(nilai)
    return rata

# Panggil fungsi dengan list nilai
data_nilai = [80, 75, 90, 60, 85]
hasil = rata_rata(data_nilai)

# Tampilkan hasil
print("Hasil rata-rata:", hasil)
