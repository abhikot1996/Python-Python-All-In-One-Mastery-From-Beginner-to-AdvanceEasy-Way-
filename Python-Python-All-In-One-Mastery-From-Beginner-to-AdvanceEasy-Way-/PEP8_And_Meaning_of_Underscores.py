'''
PEP8 and meaning of Underscores
        * single Leading Underscore: _var :Private Method Attribute ( Programmer Requesting)
        * Single Trailing Underscore: var_ : avoid over shading
        * Double Leading Underscore: __var :Name Mingled to avoid Conflicts ( To force not to change/ Python Enforcing) )
        * Double Leading and Trailing Underscore: __var__ : Magic Methods
        * Only Underscore in python : _ : Unused variables

'''

# E.g 1),
# * single Leading Underscore: _var :Private Method Attribute
import datetime

class Account():

    @staticmethod
    def _current_time(self):   # Class Method / Static Method # _ This is private
        time = datetime.datetime.now()
        return time

    def __init__(self,name,balance): # Constructor / initializer
        self._name = name
        self.__balance = balance # __ Forcing to not change
        print(f'Account is cteated for {name}')
        self.trans_list = [(Account._current_time(self), balance)]
        self.show_tans()
        self.show()

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f'{amount}rs is deposited')
            self.show()
            self.trans_list.append((Account._current_time(self), amount))

    def withdraw(self,amount):
        if 0<amount <= self.__balance:
        # if amount > 0 and amount <= self.balance:
            self.__balance -= amount
            print(f'{amount}rs is debited')
            self.show()
            self.trans_list.append((Account._current_time(self), -amount))
        else:
            print(f"Your balance is les than {amount}")
    def show(self):
        print(f'{self._name} your balance is {self.__balance}')

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
print(Abhijit.__dict__) # (__dict__) Magic Methods
Abhijit.deposit(25000000)
print(Abhijit.__dict__)

# E.g 2),
# Only Underscore in python : _ : Unused variables
# for _ in range(10):
#     print('*')
