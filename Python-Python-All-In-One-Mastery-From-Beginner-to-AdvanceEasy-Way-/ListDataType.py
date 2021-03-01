"""
List Data Type
    * List is sequence of elements (Ordered set of element(any data type)/characters(Only string))
    * To define list is used to [,]
    * Defining list,
        list_one = [1,2,3,'d','t']

        list_two = [1,2,3,['Filmstar'],'d','t']
"""

# E.g 1),
list_one = [1,2,3,'d','t']
list_two = [1,2,3,['Filmstar'],'d','t']
print(list_one)
# o/p [1, 2, 3, 'd', 't']

print(list_two)
# o/p [1, 2, 3, ['Filmstar'], 'd', 't']

# E.g 2),
list_three = list((1,2,3,'d','t'))
print(list_three)
#o/p [1, 2, 3, 'd', 't']

# E.g 3),
print(list_one[0])
#o/p 1 (Element of index no which is mention above (0).)

print(list_one[1])
#o/p 2

print(list_two[-3])
#o/p ['Filmstar']

# E.g 4),

print(list_two[0:4])
# o/p [1, 2, 3, ['Filmstar']]

# E.g 5),

print(list_two[0::2])
#o/p [1, 3, 'd']

print(list_two[-4:-1:2])
# o/p [3, 'd']