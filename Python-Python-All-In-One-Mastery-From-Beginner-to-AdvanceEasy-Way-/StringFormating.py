"""
String Formating
{} - place holder
"""
#E.g 1),

name = 'Abhi'
age = 24

message= f'Hello {name} Wellcome, Your {age} years old'
print(message)

#E.g 2),
message1=f'Hello {name} Wellcome, Your {age-4} years old'
print(message1)

#E.g 3),
message2='Hello {0} Wellcome, Your {1} years old'.format(name,age)
print(message2)