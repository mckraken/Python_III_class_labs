#! /usr/bin/env python

import os
import sys

sys.path.append(
    '/'.join([
        os.getcwd(),
        "modules"
    ]))

from bankAccounts import BankAccount, BankAccountMinBal


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