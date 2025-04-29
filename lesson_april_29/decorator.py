print("Pattern Decorator")

# VAT: 20% from revenue
# Military Tax: 5% from revenue
# Tax for 1st group: 18%
# Tax for 2nd group: minimal salary
# Tax for 3rd group: 5%
# Return of VAT: -20%
# Tax for luxury: 10% (revenue > 100 000)


class VAT:
  def __init__(self, revenue):
    self.revenue = revenue

  def calculate(self):
    return self.revenue * 0.2


class MilitaryDecorator:
  def __init__(self, tax):
    self._tax = tax
    self.revenue = tax.revenue

  def calculate(self):
    amount = self._tax.calculate()
    return amount + self._tax.revenue * 0.05


class Group1Decorator:
  def __init__(self, tax):
    self._tax = tax

  def calculate(self):
    amount = self._tax.calculate()
    return amount + self._tax.revenue * 0.18


t = VAT(1000)
m = MilitaryDecorator(t)
g1 = Group1Decorator(m)

total_tax = g1.calculate()

print("Total tax amount:", total_tax)
