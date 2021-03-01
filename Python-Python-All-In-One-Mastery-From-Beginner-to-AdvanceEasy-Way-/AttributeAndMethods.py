"""
Attributes and Method
"""
# #E.g 1),
# # Attribute
# class map():
#     material = 'house'
#     print(f'I build {material}')
#
# house1 = map()
#
# house2 = map()
# house3 = map()
# house1.material = 'new_house' # adding new value to the existing attribute
# house1.material2 = 'Very Good house' # Creating new attribute in class map
# print(house1.material) # new added attribute
# print(house1.material2) # new created attribute
# o/p
# I build house
# new_house
# Very Good house

# E.g 2),
# method
# if in class 'self' keyword in function then it is not function it is method
class map():
    material = 'house'
    print(f'I build {material}')
    def adder(self):
        x=2+2
        return x

house = map()
print(house.material)
print(house.adder())
# o/p
# I build house
# house
# 4
