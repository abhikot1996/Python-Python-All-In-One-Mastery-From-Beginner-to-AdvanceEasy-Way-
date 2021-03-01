'''
Static Method With Phokat Bank Project
'''
"""
Phokat Bank Project
"""
import datetime

class Account():

    @staticmethod
    def current_time(self):   # Class Method / Static Method
        time = datetime.datetime.now()
        return time

    def __init__(self,name,balance): # Constructor / initializer
        self.name = name
        self.balance = balance
        print(f'Account is cteated for {name}')
        self.trans_list = [(Account.current_time(self),balance)]
        self.show_tans()
        self.show()

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f'{amount}rs is deposited')
            self.show()
            self.trans_list.append((Account.current_time(self),amount))

    def withdraw(self,amount):
        if 0<amount <= self.balance:
        # if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'{amount}rs is debited')
            self.show()
            self.trans_list.append((Account.current_time(self), -amount))
        else:
            print(f"Your balance is les than {amount}")
    def show(self):
        print(f'{self.name} your balance is {self.balance}')

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
    # Amount 300000000 rupes,Deposit on 2021-02-14 20:59:03.714630
    # Abhijit your balance is 300000000
    # 25000000rs is deposited
    # Abhijit your balance is 325000000
    # Amount 300000000 rupes,Deposit on 2021-02-14 20:59:03.714630
    # Amount 25000000 rupes,Deposit on 2021-02-14 20:59:03.714630
    # Account is cteated for Vishal
    # Amount 100 rupes,Deposit on 2021-02-14 20:59:03.714630
    # Vishal your balance is 100
    # 100rs is deposited
    # Vishal your balance is 200
    # Amount 100 rupes,Deposit on 2021-02-14 20:59:03.714630
    # Amount 100 rupes,Deposit on 2021-02-14 20:59:03.714630
    # Account is cteated for John
    # Amount 200 rupes,Deposit on 2021-02-14 20:59:03.714630
    # John your balance is 200
    # 100rs is deposited
    # John your balance is 300
    # Amount 200 rupes,Deposit on 2021-02-14 20:59:03.714630
    # Amount 100 rupes,Deposit on 2021-02-14 20:59:03.714630
    # 50rs is debited


