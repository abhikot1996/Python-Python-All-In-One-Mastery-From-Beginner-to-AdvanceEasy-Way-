'''
* '*args' exercise
        * if arguments are assigned to '*args' it take as a tuple.
'''


# E.g ,
# *args
def greet(*ola):
    print("Hello " +ola[0]+" how are you")
    # print("Hello " + args[1] + " I don't know you")
    # print("Hello " + args[2] + " I don't know you")

greet("Samy","John","Bally","Bob")

#o/p
# (1, 2, 3, 4, 5)
# 15
