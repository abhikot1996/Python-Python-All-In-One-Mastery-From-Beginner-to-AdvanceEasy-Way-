# """
# List Data Type
#
# """

a = [1,1,2,3,'a','b','b','c']
b = [4,5,6,['Filmstar'],'d','e','f']

# E.g 1),
# Concatenate of list
c = a+b
print(c)
# o/p [1, 2, 3, 'a', 'b', 'c', 4, 5, 6, 'd', 'e', 'f']

# E.g 2),
# extend method of list (Same as concatenate)
a.extend(b)
print(a)
# o/p [1, 2, 3, 'a', 'b','c', 4, 5, 6, 'd', 'e', 'f']

# E.g 3),
# append method (to add elements in list)
a.append('d')
print(a)
# o/p [1, 2, 3, 'a', 'b', 'c', 4, 5, 6, 'd', 'e', 'f', 'd']

# E.g 4),
# extend method is also used to append element in list
a.extend('e')
print(a)
# o/p  [1, 2, 3, 'a', 'b', 'c', 4, 5, 6, 'd', 'e', 'f', 'd', 'g']

# E.g 5),
# pop method is used to remove last element  from the list
a.pop()
print(a)
# o/p [1, 2, 3, 'a', 'b', 'c', 4, 5, 6, 'd', 'e', 'f', 'd'] ('e' is removed from list a)

# E.g 6),
# remove method is used to remove specific element of the list.
b.remove('e')
print(b)
# o/p [4, 5, 6, 'd', 'f'] ('e' is removed from list b)

# To remove hole list
b.remove(['Filmstar'])
print(b)
# o/p [4, 5, 6, 'd', 'f'] ('e' and ['Filmstar'] are removed from list b)

# E.g 7),
# To count elements of the list
print(a.count(1))
# o/p 2 (Two times 1 element in list a)

# E.g 8),
# sort method is used to sort the elements of list in assending order
d = [4,5,10,7,99,75,69,44,13,27,36]
e = ['Fruit', 'Apple', 'Flower', 'Lotas','Water', 'Food', 'Shelter']
d.sort()
print(d)
#o/p [4, 5, 7, 10, 13, 27, 36, 44, 69, 75, 99] (Assending order)

e.sort()
print(e)
#o/p ['Apple', 'Flower', 'Food', 'Fruit', 'Lotas', 'Shelter', 'Water']

# To reverse order of list elements
d.sort(reverse=True)
print(d)
# o/p [99, 75, 69, 44, 36, 27, 13, 10, 7, 5, 4] (Decending Order)

e.sort(reverse=True)
print(e)
# o/p ['Water', 'Shelter', 'Lotas', 'Fruit', 'Food', 'Flower', 'Apple']

# E.g 9),
# reverse method is used to reverse the elements of list
f=[5,10,7,99,75,4,69,44,13,27,36]
f.reverse()
print(f)
# o/p [36, 27, 13, 44, 69, 75, 99, 7, 10, 5, 4]

# E.g 10),
# min method is used to find minimum element of list
g=min(f)
print(g)
# o/p 4

# E.g 11),
# max method is used to find maximum element of the list
h=max(f)
print(h)
# o/p 99

# E.g 12),
# sum to sum all elements of the list
i=sum(f)
print(i)
# o/p 389

#E.g 13),
# Mutebality is the changing elements of the list
j = [1,2,3,'a','b','c']
print(j[0])
# o/p 1 (0th position element)

j[3] = 'b'
print(j)
# o/p [1, 2, 3, 'b', 'b', 'c']





