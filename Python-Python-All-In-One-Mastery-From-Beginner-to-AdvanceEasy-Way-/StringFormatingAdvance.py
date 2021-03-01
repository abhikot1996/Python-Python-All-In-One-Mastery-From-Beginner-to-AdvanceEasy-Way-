"""
String Formatting Advance
 Escape Characters,
    1) \ (To print ' in the output as usual)
    2) \t (To give tab in output)
    3) \n (To go next line)
    Link for more Escape Characters,
     (http://python-ds.com/python-3-escape-sequences )
"""
name= input('Enter your name : ')
age = input('Enter your age : ')

#E.g 1),
message=f'Hello {name}, Your\'s age is {age} years.'
print(message)
#O/p
# Enter your name : AK
# Enter your age : 24
# Hello AK, Your's age is 24 years.

#E.g 2),

name1 = input('Please enter your name : ')
age1 = int(input('Please enter your age : '))
message1 = f'Hello {name1} Welcome,  Your\'s age is {age1/2} years'
print(message1)
#o/p
# Please enter your name : AK
# Please enter your age : 24
# Hello AK Welcome,  Your's age is 12.0 years

#E.g 3),

name2 = input('Please enter your name : ')
age2 = int(input('Please enter your age : '))
message2 = f'Hello {name2} Welcome,  Your\ts age is {age2/2} years'
print(message2)
#O/p
# Please enter your name : Rohini
# Please enter your age : 20
# Hello AK Welcome,  Your	s age is 12.0 years

#E.g 4),
name3 = input("Please Enter your name : ")
age3 = int(input("Please Enter your age : "))
message3 = f'Hello {name3} Welcome,  Your\ns age is {age3/2} years'
print(message3)
#o/p
# Please Enter your name : AK
# Please Enter your age : 24
# Hello AK Welcome,  Your
# s age is 12.0 years

# For paragraph use Three double coute Start and end of the paragraph
#E.g 4),
print(""" E.g 1),
name = "Gangster "
job = " Play Cricket "

print(name+job)

(If values are intiger then o/p will be addition of the integers )
E.g 2),
a=1
b=1
print(a+b) #O/p 2

(If values are strings then o/p will be  Concatenation of the strings)
E.g 3),
c='1'
d='1'
print(c+d) #O/p 11
""")