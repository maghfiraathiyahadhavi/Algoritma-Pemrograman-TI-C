def pangkat_rekursif(a, b):
    # Basis rekursi: pangkat 0 = 1
    if b == 0:
        return 1
    
    # Rekursi: a^b = a * a^(b-1)
    return a * pangkat_rekursif(a, b - 1)

# Contoh pemanggilan
print(pangkat_rekursif(2, 5)) 

