book = [
    ["Algoritma", 2000],
    ["Basis Data", 2500],
    ["Kalkulus", 3000],
    ["Aljabar linier", 3500],
    ["Srtuktur data", 4000]
]

print("Toko Buku Teknik")
for i in range(len(book)):
    print(i+1,".",book[i][0],"Rp",book[i][1])

pilih = int(input("Pilih buku: "))

if pilih >=1 and pilih <=5:
    print("book:",book[pilih-1][0])
    print("price:",book[pilih-1][1])
else:
    print("book not found")




    