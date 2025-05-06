import json

print("Pattern Command")


class User:
  def __init__(self, id, name):
    self.id = id
    self.name = name


class Chat:
  def __init__(self):
    self.users = []
    self.active = True

  def show_users(self):
    for user in self.users:
      print(user.id, user.name)


class Command:
  def execute():
    pass


class StopChatCommand(Command):
  def __init__(self, chat):
    self._chat = chat

  def execute(self):
    self._chat.active = False


class ResumeChatCommand(Command):
  def __init__(self, chat):
    self._chat = chat

  def execute(self):
    self._chat.active = True


class AddUserCommand(Command):
  def __init__(self, chat, user):
    self._chat = chat
    self._user = user

  def execute(self):
    self._chat.users.append(self._user)


class RemoveUserCommand(Command):
  def __init__(self, chat, user_id):
    self._chat = chat
    self._user_id = user_id

  def execute(self):
    self._chat.users = [user for user in self._chat.users if user.id != self._user_id]


class ActiveChatCommandDecorator(Command):
  def __init__(self, chat, chat_command):
    self._chat = chat
    self._chat_command = chat_command

  def execute(self):
    if self._chat.active or isinstance(self._chat_command, ResumeChatCommand):
      self._chat_command.execute()
    else:
      print(
        f"Cannot execute command {self._chat_command.__class__.__name__}, because chat is inactive"
      )


u1 = User(1, "Bohdan")
u2 = User(2, "Marta")
u3 = User(3, "Oleksii")
u4 = User(4, "Yulia")

chat = Chat()

commands = [
  AddUserCommand(chat, u1),
  AddUserCommand(chat, u2),
  StopChatCommand(chat),
  AddUserCommand(chat, u3),
  RemoveUserCommand(chat, 2),
  ResumeChatCommand(chat),
  AddUserCommand(chat, u4),
]

commands = [ActiveChatCommandDecorator(chat, command) for command in commands]

for command in commands:
  command.execute()
  print()
  print(f"Executed {command.__class__.__name__}")
  chat.show_users()
