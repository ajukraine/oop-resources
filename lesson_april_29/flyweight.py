print("Pattern Flyweight")

num_of_trees = 1000
num_of_wells = 20
num_of_clouds = 2000
num_of_characters = 10


class GameObjectFactory:
  def __init__(self):
    self._cache = {}

  def get(self, type, state=None):
    if type == "tree":
      if type not in self._cache:
        self._cache[type] = Tree()
      return self._cache[type]
    elif type == "well":
      if type not in self._cache:
        self._cache[type] = Well()
      return self._cache[type]
    elif type == "cloud":
      if type not in self._cache:
        self._cache[type] = Cloud()
      return self._cache[type]
    elif type == "warrior":
      key = f"{type}-{state}"
      if key not in self._cache:
        self._cache[key] = Warrior(state)
      return self._cache[key]


class Tree:
  def __init__(self):
    print("Tree was created")


class Well:
  def __init__(self):
    print("Well was created")


class Cloud:
  def __init__(self):
    print("Cloud was created")


class Warrior:
  def __init__(self, name):
    print(f"Warrior '{name}' was created")


def start_game():
  factory = GameObjectFactory()

  for i in range(num_of_trees):
    factory.get("tree")

  for i in range(num_of_clouds):
    factory.get("cloud")

  for i in range(num_of_wells):
    factory.get("well")

  for i in range(num_of_characters):
    factory.get("warrior", f"{i+1}")


start_game()
