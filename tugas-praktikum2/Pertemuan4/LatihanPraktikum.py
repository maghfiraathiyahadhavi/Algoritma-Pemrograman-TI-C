# Membuat program menghitung luas persegi

class KalkulatorLuas:
    def __init__(self):
        pass

    def hitung_luas(self):
        try:
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = sisi * sisi

            print("Luas persegi adalah:", luas)

        except ValueError:
            print("Input harus berupa angka. Silahkan coba lagi.")

        
        finally: 
            print("Program selesai di kerjakan.")


# buat menjalankan isi class

obj = KalkulatorLuas()
obj.hitung_luas()

