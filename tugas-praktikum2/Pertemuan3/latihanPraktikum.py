class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk 
        self.tahun_rilis = tahun_rilis

    def sound(self):
        return ("suara")

 
class Car(Vehicle):
    def __init__(self, tahun_rilis, merek):
     self.__tahun_rilis = tahun_rilis

    def get_tahun_rilis(self):
        return self.__tahun_rilis
     
    def set_tahun_rilis(self):
        return self.__tahun_rilis
     
    def sound(self):
        return("Ngengggg")
     

class Motor(Vehicle):
    def __init__(self, tahun_rilis, merek):
     self.__tahun_rilis = tahun_rilis

    def get_tahun_rilis(self):
        return self.__tahun_rilis
     
    def set_tahun_rilis(self):
        return self.__tahun_rilis
     
    def sound(self):
        return("Titt")  
     
v1 = Vehicle("Bajai", 2011, "AZXX")
c1 = Car(2022, "Ford")
m1 = Motor(2024, "ZX")

print(m1.sound())
print(c1.get_tahun_rilis())

menu = [
    ["Nasi Goreng",15000],
    ["Mie Ayam",12000],
    ["Ayam Goreng",18000],
    ["Es Teh",5000],
    ["Jus Jeruk",8000]
]

print("Menu Warung Barokah")
for i in range(len(menu)):
    print(i+1,".",menu[i][0],"Rp",menu[i][1])

pilih = int(input("Pilih menu: "))

if pilih >=1 and pilih <=5:
    print("Menu:",menu[pilih-1][0])
    print("Harga:",menu[pilih-1][1])
else:
    print("menu tidak ada")