class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()



class Menu:
    def __init__(self,nama,harga):
        self.nama = nama
        self.harga = harga

    def tampilkan(self):
        print(self.nama,"Rp",self.harga)


class Transaksi:
    def __init__(self):
        self.total = 0

    def tambah(self,menu,jumlah):
        self.total = self.total + (menu.harga * jumlah)

    def struk(self):
        print("Total bayar:",self.total)


