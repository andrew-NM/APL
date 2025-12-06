class Positive:
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)
    
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            print(f"{self.name} must be a number")
        elif value < 0:
            print(f"{self.name} must be a non-negative number")
        else:
            instance.__dict__[self.name] = value


class BankAccount:
    balance = Positive()
    
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
        else:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            self.balance -= amount
    
    def __repr__(self):
        return f"BankAccount(balance={self.balance})"