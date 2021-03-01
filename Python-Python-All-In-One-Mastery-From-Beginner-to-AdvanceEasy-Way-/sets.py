"""
Sets
    * sets is unordered data tyape
    * sets holds only unique elements
    * sets remove same date from the set(refere E.g 1)
"""

# Defining sets
A = {'A','B','B','D','A'}
B = {'X','V','C','X','B'}

# E.g 1),
#
print(A)
# o/p {'A', 'D', 'B'}

print(B)
# o/p {'C', 'X', 'V', 'B'}

# E.g 2),
# 'intersection()' method is used to find common elements of two or multiple sets
C=A.intersection(B)
print(C)
# o/p {'B'}

# E.g 3),
# 'union()' method is used to merge sets
D= A.union(B)
print(D)
# o/p {'D', 'C', 'X', 'V', 'A', 'B'}

# E.g 4),
# 'add()' method is used to add element in set
A.add('John sena')
print(A)
# o/p {'John sena', 'B', 'D', 'A'}

# E.g 5),
# 'update()' method is used update element of the set ( argument must be list)
A.update(['John2'])
print(A)
# o/p {'A', 'John2', 'B', 'D', 'John sena'}

# E.g 6),
# 'remove()' method is used to remove element of the set ( argument must in string)
A.remove('John2')
print(A)
# o/p {'John sena', 'B', 'D', 'A'}

# E.g 7),
# 'len()' method is used to know the length of the set of elements
print(len(A))
# o/p 4

# E.g 8),
# 'del' method is used to delete whole set we can't delete specific element of the set using 'del' fun
del A
print(A)
# o/p NameError: name 'A' is not defined


