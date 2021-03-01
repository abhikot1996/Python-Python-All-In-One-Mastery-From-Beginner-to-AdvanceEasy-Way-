"""
Polymorphism

        * Poly - Many
        * morphism - Shapes
"""
# E.g 1),
# Polymorphism with Class
class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " Says Whuuuuff"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " Says Meeeeeeooooo"

my_tommy = Dog("Tommy")
my_sally = Cat("Sally")

print(my_tommy.speak())
print(my_sally.speak())
# o/p
# Tommy Says Whuuuuff
# Sally Says Meeeeeeooooo

print("X"*20)

# E.g 2),
# Polymorphism with for loop
for pet in [my_sally,my_tommy]:
    print(pet.speak())

# o/p
# Sally Says Meeeeeeooooo
# Tommy Says Whuuuuff

print("X"*20)

# E.g 3),
# Polymorphism with function
def my_pet_speak(pet):
    print(pet.speak())

my_pet_speak(my_tommy)
my_pet_speak(my_sally)
# o/p
# Tommy Says Whuuuuff
# Sally Says Meeeeeeooooo





