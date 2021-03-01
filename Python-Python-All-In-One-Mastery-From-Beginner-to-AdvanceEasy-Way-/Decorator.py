'''
Decorator
        * Decorator takes function and returns function
'''

# E.g 1),
# def chees_and_buns(orogonal_fun): # Decorator
#     def wrap():
#         print("I am upper bread")
#         orogonal_fun()
#         print("I am lower bread")
#     return wrap()
#
# def chicken():
#     print("I am roasted chicken")
#
# burger = chees_and_buns(chicken)

# E.g 2),
# switching on or swithching of functionality of decorator
# Which you want to switch on the function type that function's on the above line '@' and call decorator,
def chees_and_buns(orogonal_fun): # Decorator
    def wrap():
        print("I am upper bread")
        orogonal_fun()
        print("I am lower bread")
    return wrap()

@chees_and_buns
def chicken():
    print("I am roasted chicken")

# burger = chees_and_buns(chicken)