class Category():
  # ledger = list()
  # _category = ""
  def __init__(self, category):
    self._category = category
    self.ledger = list()
  
  def deposit(self, amount, description="") -> None:
    self.ledger.append({"amount": amount, "description": description})
    
  def withdraw(self, amount, description="") -> bool:
    if (self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False
    
  def get_balance(self) -> int:
    sum = 0
    for amount in self.ledger:
      sum += amount["amount"]
    return sum

  def transfer(self, amount, transfer) -> bool:
    if (self.check_funds(amount)):
      self.withdraw(amount, f"Transfer to {transfer._category}")
      transfer.deposit(amount, f"Transfer from {self._category}")
      return True
    return False
    
  def check_funds (self, amount) -> bool:
    if amount > self.get_balance():
      return False
    return True

  def __str__(self):
    header = f"{self._category:*^30}\n"

    lines = ""
    for item in self.ledger:
      description = item["description"]
      amount = item["amount"]
      lines += f"{description} {amount} \n"

    total = f"Total: {self.get_balance()}" 
    return header + lines + total
def create_spend_chart(categories):
  print("")