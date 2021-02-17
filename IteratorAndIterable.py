"""
Iterable data type
    * Iterable data type -  Data type should be able to return element one by one
    * Iterator functions -  Method which is used to get element one by one
    * We can perform same operations which is given below (in {dictionary},{set},(tuple),'string')
    * limitations,
            * We can't perform these operations on the big data
            * and if we give any element that does not exist in set then there will be error

"""
a=[1,2,3,4,5,6,7,8,9]

# E.g 1),
# 'iter()' method is used to convert any element in to iterator
var_a = iter(a)
print(var_a)
# # o/p <list_iterator object at 0x0000029B4CCC0E50> (converted in to 'iterator'
#
# # E.g 2),
# # 'next()' method is used to get iterable value
# var_b = iter(a)
# print(next(var_b))
# # o/p 1 (value of first iterable element)
#
# # To perform any operation
# t=next(var_a)+2.5
# print(t)
# # 3.5

# getting all values of elements which is given
print(next(var_a)) # o/p 1
print(next(var_a)) # o/p 2
print(next(var_a)) # o/p 3
print(next(var_a)) # o/p 4
print(next(var_a)) # o/p 5
print(next(var_a)) # o/p 6
print(next(var_a)) # o/p 7
print(next(var_a)) # o/p 8
print(next(var_a)) # o/p 9


