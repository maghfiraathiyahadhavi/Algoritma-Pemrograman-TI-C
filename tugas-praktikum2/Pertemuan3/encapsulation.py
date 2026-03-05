class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error


hari = int(input("Jumlah hari: "))
menu = int(input("Jumlah menu: "))

data = []

for i in range(hari):
    baris = []
    print("Hari",i+1)
    for j in range(menu):
        x = int(input("Menu "+str(j+1)+": "))
        baris.append(x)
    data.append(baris)

print("Data penjualan")
for i in range(hari):
    for j in range(menu):
        print(data[i][j], end=" ")
    print()

print("Total per hari")
for i in range(hari):
    print(sum(data[i]))

print("Total per menu")
for j in range(menu):
    t = 0
    for i in range(hari):
        t += data[i][j]
    print(t)