import copy


class Person:
  def __init__(self):
    self.name = "N/A"
    self.age = 20

  def __str__(self):
    return "Person"

  def clone(self):
    return copy.deepcopy(self)


class Employee(Person):
  def __init__(self):
    super().__init__()
    self.title = "Developer"

  def __str__(self):
    return "Employee(Developer)"


class InfoPrinter:
  def print(self, person):
    print(f"{person}: {person.name}, of age {person.age}")


p = Person()
e = Employee()

p_copy = p.clone()
p_copy.age = 31

e_copy = e.clone()
e_copy.name = "Ivan"

printer = InfoPrinter()
printer.print(p)
printer.print(p_copy)
printer.print(e)
printer.print(e_copy)
