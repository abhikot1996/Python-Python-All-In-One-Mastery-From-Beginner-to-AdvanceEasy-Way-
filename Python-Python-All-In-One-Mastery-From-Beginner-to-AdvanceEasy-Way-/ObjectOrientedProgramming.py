"""
Object Oriented Programming

Class
    * class is made of attribute(variable) method(function)
    * Class - Template for creating objects, All objects Created from
              same class will have same attributes

    * Object - Is Instance of a Class
    * Instentiate - Process of Creating Instance
    * Method _ A function Defined in Class
    * Attribute - A Variable bound to an instance of a class
"""

# E.g 1),
# function definition
def map():
    material = 'house'
    print(f'I build {material}')

# E.g 2),
# clss definition
class map():
    material = 'house'
    print(f'I build {material}')

# changing attribute value in class (object creation process or instaionshiyation process)
house =map()
house.material = 'new_house'
print(house.material)
# o/p
# I build house
# new_house


