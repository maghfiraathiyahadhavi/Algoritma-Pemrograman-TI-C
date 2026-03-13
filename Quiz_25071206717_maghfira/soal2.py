book = [
    ["Algoritma", 2000],
    ["Basis Data", 2500],
    ["Kalkulus", 3000],
    ["Aljabar linier", 3500],
    ["Srtuktur data", 4000]
]

pinjaman = []
title_book = []
how_long = []
members = 0

while True:
    for i in range(len(book)):
        print(i+1,book[i][0],book[i][1])
        pilih = int(input("pilih book (0 selesai): "))
        
        if pilih == 0:
            break

        title_book = int(input("title_book: "))
        how_long = int(input("how_long: "))

        denda = book[pilih-1][0]
        how_long = book[pilih-1][1]

        pinjaman.append([title_book,denda,how_long])

    if denda >1 :
        print("anda terkena denda")
    
    else:
        print("tidak terkena denda")
    


       




