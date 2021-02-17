"""
Boolean Datatype
    * Boolean Datatype returns either True or False
    * Boolean Datatype is used in Comparison Operators and Logical Operators (Keywords)
        * Logical Operators (Keywods)
            1) in   2) not  3) is   4) and  5) or

                4) 'and'
                    condition1 + condintion2  =  Result
                        True   +     True     =  True
                        True   +     False    =  False
                        False  +       -      =  False

                5) 'or'
                    condition1 + condintion2  =  Result
                        True   +     True     =  True
                        True   +     False    =  True
                        False  +     True     =  True
                        False  +     False    =  False

            * Identity Operators
                3) 'is'
                    'is' show if element is in the same memory or not,
                     if there is more than one variable has same value then
                    'is' create one one variable and uses value of that variable whenever need

                4) 'is not'
                    'is not' method returns apposite value of 'is' method


"""

a = 5
b = 5

# E.g 1),
# 'is' Method
print(a is b)
# o/p True

# E.g 2),
# 'id' Method is use to find the memory location of the variable
print(id(a)) 
# o/p 2030203005360

print(id(b))
# o/p 2030203005360

# Same memory address means only one variable is created by 'is' method and
# it refered by another variable because they has same value

# E.g 3),
# 'is not' method returns apposite result of the 'is' method
print(a is not b)
# o/p False
