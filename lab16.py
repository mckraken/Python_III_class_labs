#! /usr/bin/env python

class BankAccount(object): # Top tier class (super class) in Python 2 or 3
    # class BankAccount: works fine in Python 3. Parens not required

    acct_cntr = 0

    def __init__(self, name, initial_deposit=None):
        self.balance = 0  # instance variable
        self.acctname = name  # instance variable
        BankAccount.acct_cntr += 1

    def __str__(self):
        return '\n'.join([
            f'{"Account:":<25} {self.acctname:<}',
            f'{"Current balance:":<25} ${self.currentbalance():>10.2f}'
        ])

    def __eq__(self, other):
        if self.balance == other.balance:
            return True
        else:
            return False

    def __del__(self):
        BankAccount.acct_cntr -= 1

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


class BankAccountMinBal(BankAccount):

    def __init__(self, name, minimum_balance=0, initial_deposit=0):
        if initial_deposit < minimum_balance:
            raise ValueError(f'Initial deposit ({initial_deposit}) must be greater than minimum balance ({minimum_balance})')
        self.minbalance = minimum_balance
        self.balance = initial_deposit
        self.acctname = name
        BankAccount.acct_cntr += 1

    def __str__(self):
        return '\n'.join([
            f'{"Account:":<25} {self.acctname:<}',
            f'{"Minimum allowed balance:":<25} ${self.minbalance:>10.2f}',
            f'{"Current balance:":<25} ${self.currentbalance():>10.2f}'
        ])


    def withdrawal(self, amount):
        if self.balance - amount < self.minbalance:
            return 4
        self.balance -= amount
        return 0

def status(*args):
    for item in args:
        print(item)
    # print(f'Number of accounts: {BankAccount.acct_cntr}')
    print()

def getmoney(acct, amt):
    rc = acct.withdrawal(amt)
    if rc > 0:
        print(f'{"Invalid Withdrawal:":<25} ${amt:>10.2f}')
        status(acct)
    else:
        print(f'{"Amount withdrawn:":<25} ${amt:>10.2f}')
        status(acct)

def putmoney(acct, amt):
    rc = acct.deposit(amt)
    if rc > 0:
        print(f'{"Invalid Withdrawal:":<25} ${amt:>10.2f}')
        status(acct)
    else:
        print(f'{"Amount deposited:":<25} ${amt:>10.2f}')
        status(acct)


a = BankAccount('Monty Python')
print('Number of accounts -', BankAccount.acct_cntr)
b = BankAccount('Guido van Rossum')
print('Number of accounts -', BankAccount.acct_cntr)

putmoney(a, 100)
putmoney(b, 500)
status(a, b)
getmoney(a, 50)
getmoney(b, 4000)
status(a, b)


getmoney(a, 500)
getmoney(b, 50)
status(a, b)
del(a)
print('Number of accounts -', BankAccount.acct_cntr)
try:
    a = BankAccountMinBal(
        'Monty Python',
        minimum_balance=100
    )
except ValueError as e:
    print(e)
try:
    a = BankAccountMinBal(
        'Monty Python',
        minimum_balance=100,
        initial_deposit=100
    )
except ValueError as e:
    print(e)
try:
    c = BankAccountMinBal(
        'Monty Python',
        minimum_balance=100
    )
except ValueError as e:
    print(e)
putmoney(a, 100)
putmoney(b, 500)
getmoney(a, 50)
getmoney(b, 400)
getmoney(a, 500)
getmoney(b, 50)