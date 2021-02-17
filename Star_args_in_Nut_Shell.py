'''
Keyword Argument
'''

# E.g 1),
#*args
# def greet (name,*args,named_value):
#     print(f"Hello {name}")
#     print(args)
#     for i in args:
#         print(f"Hello {i}")
#     print(f"Hello {named_value}")
#
# greet("AK","AK1","AK2","AK3",named_value= "AKnamed")

# o/p
# Hello AK
# ('AK1', 'AK2', 'AK3')
# Hello AK1
# Hello AK2
# Hello AK3
# Hello AKnamed

# E.g 2),
#**kwargs
# def myfun(**kwargs):
#     print(kwargs['fname'])
#     print(kwargs['mname'])
#     print(kwargs['lname'])
#
# myfun(fname = "RanjanRaj", mname = "Gopal", lname = "Raj")
# o/p
# RanjanRaj
# Gopal
# Raj

# E.g 3),
# def myfun(**kwargs):
#     print(kwargs['fname'])
#     print(kwargs['mname'])
#     print(kwargs['lname'])
#
# a={"fname": "RanjanRaj", "mname":"Gopal","lname":"Raj"}
# myfun(**a)
# o/p
# RanjanRaj
# Gopal
# Raj

# E.g 4),
# Unpacking dictionary
# def myfun(**kwargs):
#     for key,value in kwargs.items():
#         print(f'key:{key} and value is {value}')
#
# a = {"fname":"RnajanRaj","mname":"Gopal","lname":"Raj"}
# myfun(**a)
# # o/p
# # key:fname and value is RnajanRaj
# # key:mname and value is Gopal
# # key:lname and value is Raj
