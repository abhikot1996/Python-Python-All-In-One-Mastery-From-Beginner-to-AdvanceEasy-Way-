"""
List Comprehension
"""

# E.g 1),
# square of given list
num = [1,2,3,4,5,6,7,8,9]
sqr_num1=[]
for i in num:
    sqr_num1.append(i**2)

print(sqr_num1)

print('-'*33)

# E.g 2),
# Using List Comprehension with int in list
# Square of given list
sqr_num2 = [x**2 for x in num] # syntax : list_name = [expression loop]
print(sqr_num2)

# E.g 3),
name1 = []
for letter in "Abhijit":
    name1.append(letter)
print(name1)

# List comprenesion with string in list
print("-"*35)
name1=[]
name1= [letter for letter in "Abhijit"]
print(name1)
