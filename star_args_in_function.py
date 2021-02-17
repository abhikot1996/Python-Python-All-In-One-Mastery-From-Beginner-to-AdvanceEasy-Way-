'''
 *args in Function
        * '*args' is used in function when we want to assign argument as many as we want
          then *args is used in function definition.

        * '*ola' same as '*args'
'''

# E.g ,
# *args
def greet(*args):
    print("Hello " +args[0]+" how are you")
    print("Hello " + args[1] + " I don't know you")
    print("Hello " + args[2] + " I don't know you")

greet("Samy","John","Bally","Bob")

#o/p
# Hello Samy how are you
# Hello John I don't know you
# Hello Bally I don't know you
