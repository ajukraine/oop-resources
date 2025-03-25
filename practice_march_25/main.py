from abc import ABC, abstractmethod
import random


class AccountingException(Exception):
  pass


class Transaction(ABC):
  def __init__(self, account, type):
    self._account = account
    self._type = type

  @abstractmethod
  def execute(self, amount):
    pass

  def __str__(self):
    return f"Transaction type: {self._type}"


class SalaryTransaction(Transaction):
  def __init__(self, account):
    super().__init__(account, "SALARY")

  def execute(self, amount):
    self._account.deposit(amount)


class PaymentTransaction(Transaction):
  def __init__(self, account):
    super().__init__(account, "PAYMENT")

  def execute(self, amount):
    self._account.credit(amount)


class Account(ABC):
  def __init__(self, accountNumber):
    self._balance = 0
    self._number = accountNumber

  def balance(self):
    return self._balance

  def credit(self, amount):
    self._validate(amount)
    self._balance -= amount

  def deposit(self, amount):
    self._balance += amount

  @abstractmethod
  def _validate(self, amount):
    pass

  def __str__(self):
    return self._number


class InterestTransaction(Transaction):
  def __init__(self, account):
    super().__init__(account, "INTEREST")

  def execute(self, amount):
    self._account.deposit(amount)


class DepositAccount(Account):
  def __init__(self, accountNumber, interestRate):
    super().__init__(accountNumber)
    self._interestRate = interestRate

  def deposit(self, amount):
    interestAmount = amount * self._interestRate
    super().deposit(amount + interestAmount)

  def _validate(self, amount):
    pass


class CreditAccount(Account):
  def _validate(self, amount):
    pass


class SavingsAccount(Account):
  def _validate(self, amount):
    if amount > self._balance:
      raise AccountingException("Cannot credit more than balance")


# Main code

# creditAccount = CreditAccount("0001")
# savingsAccount = SavingsAccount("0002")
depositAccount = DepositAccount("0003", 0.15)

interestTransaction = InterestTransaction(depositAccount)
interestTransaction.execute(100)

print(f"Balance: {depositAccount.balance()}")

# account = savingsAccount
#
# salary = SalaryTransaction(account)
# payment = PaymentTransaction(account)
#
# transactions = [(salary, 100), (payment, 120)]
#
# for tx, amount in transactions:
#   # amount = random.randint(1, 100)
#   print(f"Amount: {amount}")
#   try:
#     tx.execute(amount)
#   except AccountingException as e:
#     print(f"Cannot execute transaction. Reason: {e}")
#   except Exception as e:
#     print(f"Generic error: {e}")
#   finally:
#     print(tx)
#     print(f"Account1 balance: {account.balance()}")
