from datetime import datetime


class Singleton:
  def __init__(self):
    self._time = datetime.now().time()

  def show_time(self):
    print(self._time)

  _instance = None

  @staticmethod
  def get_instance():
    if Singleton._instance is None:
      Singleton._instance = Singleton()

    return Singleton._instance


for x in range(0, 10):
  s = Singleton.get_instance()
  s.show_time()
