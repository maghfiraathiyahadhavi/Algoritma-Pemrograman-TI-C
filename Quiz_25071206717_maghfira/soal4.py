item = int(input("Jumlah item: "))
book = int(input("Jumlah book: "))

data = []

for i in range(item):
    baris = []
    print("item",i+1)
    for j in range(book):
        x = int(input("Item "+str(j+1)+": "))
        baris.append(x)
    data.append(baris)