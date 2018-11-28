#! /usr/bin/env python


class BankAccount(object): # Top tier class (super class) in Python 2 or 3
    # class BankAccount: works fine in Python 3. Parens not required

    def __init__(self, name):  # This method runs during instantiation
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable

    def deposit(self, amount):  # another method
        if amount < 0:
            return 4  # Negative deposits are really withdrawals
        self.balance += amount
        return 0
        # Deposit successful

    def currentbalance(self):
        return self.balance

    def withdrawal(self, amount):
        if self.balance - amount < 0:
            return 4
        self.balance -= amount
        return 0


a = BankAccount('Monty Python')
b = BankAccount('Guido van Rossum')
a.deposit(100)
b.deposit(500)
print(a.acctname, a.currentbalance())
print(b.acctname, b.currentbalance())
a.withdrawal(50)
b.withdrawal(125)
print(a.acctname, a.currentbalance())
print(b.acctname, b.currentbalance())
a.withdrawal(500)
b.withdrawal(1250)
print(a.acctname, a.currentbalance())
print(b.acctname, b.currentbalance())
print(a)
