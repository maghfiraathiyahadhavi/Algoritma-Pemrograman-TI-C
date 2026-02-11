def jumlah_digit(n):
    # Ubah ke nilai positif jika ada tanda minus
    n = abs(n)

    # Basis rekursi: jika tinggal satu digit
    if n < 10:
        return n
    
    # Rekursi: ambil digit terakhir + jumlah digit sisanya
    return (n % 10) + jumlah_digit(n // 10)

# Contoh pemanggilan
print(jumlah_digit(1234))  
