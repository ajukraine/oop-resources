from enum import Enum

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BLACK = "\033[30m"
RESET = "\033[0m"  # Reset to default color

print("Pattern Chain of Responsibility")


class Level(Enum):
  DEBUG = 0
  INFO = 1
  WARNING = 2
  ERROR = 3

  def __str__(self):
    return self.name


class Message:
  def __init__(self, text, level: Level):
    self.text = text
    self.level = level


class MsgFormatter:
  def can_format(self, msg: Message):
    pass

  def format(self, msg: Message):
    pass


class DefaultMsgFormatter(MsgFormatter):
  def can_format(self, msg):
    return True

  def format(self, msg):
    return f"[{msg.level}] {msg.text}"


class WarningMsgFormatter(MsgFormatter):
  def can_format(self, msg):
    return msg.level == Level.WARNING

  def format(self, msg):
    return f"{YELLOW}[{msg.level}]{RESET} {msg.text}"


class ErrorMsgFormatter(MsgFormatter):
  def can_format(self, msg):
    return msg.level == Level.ERROR

  def format(self, msg):
    return f"{RED}[{msg.level}] {msg.text}{RESET}"


msg_formatters = [
  ErrorMsgFormatter(),
  WarningMsgFormatter(),
  DefaultMsgFormatter(),
]


def show(msg: Message):
  for formatter in msg_formatters:
    if formatter.can_format(msg):
      print(formatter.format(msg))
      break


messages = [
  Message("Hello", Level.INFO),
  Message("Pay attention!!!", Level.WARNING),
  Message("Some logic", Level.DEBUG),
  Message("Unknown problem occured", Level.ERROR),
]

for msg in messages:
  show(msg)
