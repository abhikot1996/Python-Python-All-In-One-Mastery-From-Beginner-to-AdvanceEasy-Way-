"""
Phokat Bank Project
"""
import datetime

class Account():
    def __init__(self,name,balance): # Constructor / initializer
        self.name = name
        self.balance = balance
        print(f'Account is cteated for {name}')
        self.show()
        self.trans_list = []

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f'{amount}rs is deposited')
            self.show()
            self.trans_list.append((datetime.datetime.now(),amount))

    def withdraw(self,amount):
        if 0<amount <= self.balance:
        # if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'{amount}rs is debited')
            self.show()
        else:
            print(f"Your balance is les than {amount}")
    def show(self):
        print(f'{self.name} balance is {self.balance}')

    def show_tans(self):
        for date,amount in self.trans_list:
            if amount>0:
                trans_type = 'Deposit'
            else:
                trans_type = 'Withdraw'
                amount *=-1
            print(f'Amount {amount} rupes,{trans_type} on {date}')

Abhijit = Account("Abhijit",300000000)
Abhijit.deposit(25000000)
Abhijit.show_tans()

Vishal = Account("Vishal",100)
Vishal.deposit(100)
Vishal.show_tans()

John = Account('John',200)
John.deposit(100)
John.show_tans()
John.withdraw(50)
# o/p
# Account is cteated for Abhijit
# Abhijit balance is 300000000
# 25000000rs is deposited
# Abhijit balance is 325000000
# Amount 25000000 rupes,Deposit on 2021-02-14 20:08:21.892730
# Account is cteated for Vishal
# Vishal balance is 100
# 100rs is deposited
# Vishal balance is 200
# Amount 100 rupes,Deposit on 2021-02-14 20:08:21.892730
# Account is cteated for John
# John balance is 200
# 100rs is deposited
# John balance is 300
# Amount 100 rupes,Deposit on 2021-02-14 20:08:21.893730
# 50rs is debited
# John balance is 250


