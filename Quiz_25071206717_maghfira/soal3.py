total = int(input("Masukkan total hari keterlambatan: "))

denda = int(input("Uang denda: "))

while denda < total:
    print("Error")
    denda = int(input("input lagi: "))

jumlah = denda + total

print("Total:",total)
print("Denda:",denda)

if jumlah == 0:
    print("Tidak ada denda")
else:
    print("Total denda anda:",jumlah)

