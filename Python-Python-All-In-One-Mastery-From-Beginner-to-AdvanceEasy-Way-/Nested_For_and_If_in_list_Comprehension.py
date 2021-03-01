"""
Nested For and If in List Comprehension
"""

# E.g 1),
my_list = []
for x in [2,4,6]:
    for y in [1,3,5]:
        my_list.append(x*y)

print(my_list)
# o/p [2, 6, 10, 4, 12, 20, 6, 18, 30]

# E.g 2),
# Using list Comprehension (Nested for)
my_list = [x*y for x in [2,4,6] for y in [1,3,5]]
print(my_list)
# o/p [2, 6, 10, 4, 12, 20, 6, 18, 30]

# E.g 3),
# Using list Comprehension (Nested if)
my_list = [x*y for x in [2,4,6] for y in [1,3,5] if x*y !=10 if x*y !=20]
print(my_list)
# o/p [2, 6, 4, 12, 6, 18, 30]