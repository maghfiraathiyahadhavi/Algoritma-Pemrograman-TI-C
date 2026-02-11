def bilangan_prima(n):
    prima = []
    
    # Loop dari 2 sampai n (karena 1 bukan bilangan prima)
    for angka in range(2, n + 1):
        is_prima = True
        
        # Cek apakah angka memiliki pembagi selain 1 dan dirinya sendiri
        for pembagi in range(2, int(angka**0.5) + 1):
            if angka % pembagi == 0:
                is_prima = False
                break
        
        if is_prima:
            prima.append(angka)
    
    return prima

# Panggil fungsi untuk n = 50
hasil = bilangan_prima(50)

# Tampilkan hasil
print("Bilangan prima dari 1 sampai 50:", hasil)
