"""
Class Exercise with initialization function
    * Universal attribute
"""

# E.g 1),
class kattle():
    # To assign automatic attribute in class
    # Universal or class attribute
    power_str = "Electricity"   # Universal attribute
    # To assign automatic attribute whenever object is cteated
    def __init__(self,make,price):
        self.make = make
        self.price = price
        self.on = False

    def switch(self):
        self.on = True

kenwood = kattle("Kenwood",10)
hamilton = kattle("Hamilton",20)

print(kenwood.make)
print(kenwood.on)
kenwood.switch()
print(kenwood.on)
print(hamilton.power_str)
print(kenwood.power_str)

# o/p
# Kenwood
# False
# True
# Electricity
# Electricity
# E.g 2),

