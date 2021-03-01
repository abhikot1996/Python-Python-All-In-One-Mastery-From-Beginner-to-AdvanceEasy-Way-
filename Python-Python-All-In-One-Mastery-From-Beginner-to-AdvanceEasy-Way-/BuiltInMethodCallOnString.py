"""
Built in Method call on string
    *To use built in function on string first type the name of variable and then
     type dot and function name.(Refere E.g 1, 2)
    * Press Ctrl and click on the function call to get all info of the function
"""

# E.g 1),
message= "Hello Python My name is Abhijit"
print(message.lower())
#O/p    hello python my name is abhijit

# E.g 2),
print(message.upper())
#o/p    HELLO PYTHON MY NAME IS ABHIJIT

# E.g 3),
# strip function use to remove unwanted spaces from string
print(message.strip())
# o/p Hello Python My name is Abhijit (Removed unwanted space)

# E.g 3),
# split function use to split string
print(message.split())
#o/p ['Hello', 'Python', 'My', 'name', 'is', 'Abhijit']

# E.g 4),
# find function is used to find indexing location of string which is mention in the find function
print(message.find('Hello'))
#o/p 24 (indexing location of 'is'.)

# E.g 5),
# replace method used to replace string (as a argument first argument is old string and second is new string )
print(message.replace('Hello','Hi'))
#o/p Hi Python My name is Abhijit

# E.g 6),
# startswith method is used to find the first character of the string
print(message.startswith('H'))
#O/p True (Returns true or false) have to give argument as a first character of the string

# E.g 7),
## endswith method is used to find the last character of the string
print(message.endswith('A'))
# O/p False (Returns true or false) have to give argument as a last character of the string