"""
Boolean Datatype
    * Boolean Datatype returns either True or False
    * Boolean Datatype is used in Comparison Operators
        * Comparison Operators
            1) ==   2) !=   3) >    4) <    5) >=   6) <=
"""

a=1
b=3
# Comparison Operators
# E.g 1),
# type method is used to find which type of data is in program
print(type(True))
# o/p <class 'bool'>

# E.g 2),
# == operator is used to find if values are same or not
print(f'{a}=={b} is {a==b}')
# o/p 1==3 is False

# != operator is used to find if values different or not
print(f'{a}!={b} is {a!=b}')
# o/p 1!=3 is True

# > operator is used to find if vlaue is greater than second given value or not
print(f'{a}>{b} is {a>b}')
# o/p 1>3 is False

# < operator is used to find if value is less than second given value or not
print(f'{a}<{b} is {a<b}')
# o/p 1<3 is True

# >= operator is used to find value is greater than or equal to second given value or not
print(f'{a}>={b} is {a>=b}')
# o/p 1>=3 is False

# <= operator is used to find if value is less than or equal to second given value or not
print(f'{a}<={b} is {a<=b}')
# o/p 1<=3 is True

