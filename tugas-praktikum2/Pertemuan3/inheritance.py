class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

menu = [
    ["Nasi Goreng",15000],
    ["Mie Ayam",12000],
    ["Ayam Goreng",18000],
    ["Es Teh",5000],
    ["Jus Jeruk",8000]
]

pesanan = []
total = 0

while True:
    for i in range(len(menu)):
        print(i+1,menu[i][0],menu[i][1])

    pilih = int(input("pilih menu (0 selesai): "))

    if pilih == 0:
        break

    jumlah = int(input("jumlah: "))

    nama = menu[pilih-1][0]
    harga = menu[pilih-1][1]

    pesanan.append([nama,jumlah,harga])

print("Pesanan kamu")
for p in pesanan:
    sub = p[1]*p[2]
    total = total + sub
    print(p[0],"x",p[1],"=",sub)

print("Total:",total)