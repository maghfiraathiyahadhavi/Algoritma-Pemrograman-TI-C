class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()

total = int(input("Masukkan total belanja: "))

bayar = int(input("Uang dibayar: "))

while bayar < total:
    print("Uang kurang")
    bayar = int(input("Masukkan lagi: "))

kembalian = bayar - total

print("Total:",total)
print("Bayar:",bayar)

if kembalian == 0:
    print("Uang pas")
else:
    print("Kembalian:",kembalian)