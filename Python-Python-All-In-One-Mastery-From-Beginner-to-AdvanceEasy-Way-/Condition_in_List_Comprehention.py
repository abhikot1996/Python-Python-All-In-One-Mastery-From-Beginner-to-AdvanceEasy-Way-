"""
Condition in list comprehension
"""

# E.g 1),
# Even no
y=int(input("Enter no: "))
# even = []
# for i in range(y*2+1):
#     if i%2==0:
#         even.append(i)
# print(even)

# E.g 2),
# List comprehension
# Even no
# syntax
# a=[expression | loop | condition]
a=[i for i in range (y*2+1) if i%2==0]
print(a)