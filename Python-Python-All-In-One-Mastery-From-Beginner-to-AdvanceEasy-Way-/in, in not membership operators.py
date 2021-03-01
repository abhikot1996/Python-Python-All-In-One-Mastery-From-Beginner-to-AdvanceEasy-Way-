"""
'in' and 'not in' Membership operators
    * 'in'
        'in' method check if given value is member of any data or that variable

    * 'not in'
        'not in' return apposite value of 'in' method



"""
string=['a','b','c','d','e']
quote = 'A quick brown fox jumps ovcer the lazy dog'
word = input('Enter string : ')

# E.g 1),
# 'in' method
# print( 'a' in string )
# o/p True

# E.g 2),

print(f'{word} does exist in quote: {word in quote}')
# o/p Enter string : fox
#     fox does exist in quote: True

# E.g 3),
# 'not in'

print(f'{word} does not exist in quote : {word not in quote}')
# o/p Enter string : fox
#     fox does not exist in quote : False


