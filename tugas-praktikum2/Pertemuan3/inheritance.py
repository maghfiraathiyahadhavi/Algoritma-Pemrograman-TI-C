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

