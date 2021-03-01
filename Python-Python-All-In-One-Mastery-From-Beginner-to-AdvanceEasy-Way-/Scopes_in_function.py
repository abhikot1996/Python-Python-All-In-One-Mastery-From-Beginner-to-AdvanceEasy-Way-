'''
Python Scope
    * Local scope in Function
          Code can't be access outside of the function

    * Global scope
          Code can be access anywhere in the program
          even outside of the function (use global keyword)
'''
man ='man'
# E.g 1),
# Local scope
# def fun():
#     x=1
#     def fun2():
#         x=2
#         print(x)
#
# fun2()
# # o/p NameError: name 'fun2' is not defined

# E.g 2),
#Global Scope
# def fun():
#     global x
#     x=1
#     def fun2():
#         print(x)
#     fun2()
# fun()
# print(x)

# E.g 3),
# Global Scope exercises
clothes = 'dirty_clothes'

def washing_machine(clean_clothes):
    global clothes
    clothes = clean_clothes
    print(clothes)

print(clothes)
washing_machine("Clean Clothes")
print(clothes)



