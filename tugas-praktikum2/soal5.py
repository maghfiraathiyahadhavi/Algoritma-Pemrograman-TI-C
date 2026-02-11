import math

def jarak(x1, y1, x2, y2):
    # Menghitung selisih koordinat
    dx = x2 - x1
    dy = y2 - y1
    
    # Rumus jarak dua titik
    d = math.sqrt(dx**2 + dy**2)
    return d

# Contoh pemanggilan
hasil = jarak(1, 1, 4, 5)
print("Jarak =", hasil)
