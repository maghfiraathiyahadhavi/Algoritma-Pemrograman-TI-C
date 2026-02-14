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

