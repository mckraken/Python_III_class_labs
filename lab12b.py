#! /usr/bin/env python

import json

class BankAccount(object): # Top tier class (super class) in Python 2 or 3
    # class BankAccount: works fine in Python 3. Parens not required


    def __init__(self, name):  # This method runs during instantiation
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable

    def __str__(self):
        return (f'Account "{self.acctname}" has a balance of: ${self.balance}.')

    def __eq__(self, other):
        if self.balance == other.balance:
            return True
        else:
            return False

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
print(a, b)
print(a == b)
print(b == a)
a.deposit(100)
b.deposit(500)
print(a, b)
print(a == b)
print(b == a)
a.withdrawal(50)
b.withdrawal(400)
print(a, b)
print(a == b)
print(b == a)
a.withdrawal(500)
b.withdrawal(50)
print(a, b)
print(a == b)
print(b == a)