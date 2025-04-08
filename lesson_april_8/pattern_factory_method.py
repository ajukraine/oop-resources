from enum import Enum


class Lab:
  pass


class Lab1(Lab):
  pass


class Lab2(Lab):
  pass


class NoLab(Lab):
  pass


class LabType(Enum):
  LAB1 = 1
  LAB2 = 2
  LAB3 = 3


class LabFactory:
  @staticmethod
  def create_lab(type):
    match type:
      case LabType.LAB1:
        return Lab1()
      case LabType.LAB2:
        return Lab2()
      case _:
        return NoLab()


lab_a = LabFactory.create_lab(LabType.LAB2)
lab_b = LabFactory.create_lab(LabType.LAB2)
lab_c = LabFactory.create_lab(LabType.LAB2)

print(type(lab_a))
print(type(lab_b))
print(type(lab_c))
