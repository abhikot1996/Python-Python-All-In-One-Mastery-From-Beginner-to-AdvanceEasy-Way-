"""
Range Method to Create Automatic Lists
 * syntax of range method in list
    print(list(range(Start Point,End Point,Step Size)
"""

# E.g 1),
# To print natural numbers
print(list(range(10)))
# o/p [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(1,10)))
# O/p [1, 2, 3, 4, 5, 6, 7, 8, 9]

# E.g 2),
# To print Even natural numbers
print(list(range(0,10,2)))
# o/p [0, 2, 4, 6, 8]

# To print Odd natural numbers
print(list(range(1,10,2)))
# o/p [1, 3, 5, 7, 9]

# E.g 3),
# To access elements of list
even = list(range(0,20,2))
print(even)
# o/p 10

# E.g 4),
# index method is used to find index no of elements
print(even.index(16))
# o/p 8