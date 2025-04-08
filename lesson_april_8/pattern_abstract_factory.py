class Chair:
  def __init__(self):
    print("Chair created")


class VictorianChair(Chair):
  pass


class ModernChair(Chair):
  pass


class ArtDecoChair(Chair):
  pass


class IndustrialChair(Chair):
  pass


class Sofa:
  def __init__(self):
    print("Sofa created")


class VictorianSofa(Sofa):
  pass


class ModernSofa(Sofa):
  pass


class ArtDecoSofa(Sofa):
  pass


class IndustrialSofa(Sofa):
  pass


class CoffeeTable:
  def __init__(self):
    print("CoffeeTable created")


class VictorianCoffeeTable(CoffeeTable):
  pass


class ModernCoffeeTable(CoffeeTable):
  pass


class ArtDecoCoffeeTable(CoffeeTable):
  pass


class IndustrialCoffeeTable(CoffeeTable):
  pass


class FurnitureFactory:
  def create_chair(self):
    pass

  def create_coffeetable(self):
    pass

  def create_sofa(self):
    pass


class ModernFurnitureFactory(FurnitureFactory):
  def create_chair(self):
    return ModernChair()

  def create_sofa(self):
    return ModernSofa()

  def create_coffeetable(self):
    return ModernCoffeeTable()


class IndustrialFurnitureFactory(FurnitureFactory):
  def create_sofa(self):
    return IndustrialSofa()

  def create_coffeetable(self):
    return IndustrialCoffeeTable()

  def create_chair(self):
    return IndustrialChair()


class VictorianFurnitureFactory(FurnitureFactory):
  pass


class ArtDecoFurnitureFactory(FurnitureFactory):
  pass


factory = IndustrialFurnitureFactory()

factory.create_chair()
factory.create_coffeetable()
factory.create_sofa()
