# '''
# For Loop Exercises
# '''
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
#
# # E.g 1),
# # Sum of all list's elements
# sum = 0
# for i in range(100):
#     sum = sum + i
# print(f'Sum of list is {sum}')
# # o/p Sum of list is 4950
#
# adj = ['red', 'big', 'tasty']
# fruits = ['apple', 'banana', 'cherry']
# for i in adj :
#     for j in fruits:
#         print(i,j)
# # o/p
# # red apple
# # red banana
# # red cherry
# # big apple
# # big banana
# # big cherry
# # tasty apple
# # tasty banana
# # tasty cherry
#
# # E.g 2),
# # 'else' in 'for' loop
# for i in range(10):
#     print(i)
# else:
#     print('List if finished')
# # o/p
# # 0
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9
# # List if finished
#
# # E.g 3),
# fruit = ['apple', 'banana','cherry']
# for i in fruit :
#     print(i)
# else:
#     print('List is finished')
# #o/p
# # apple
# # banana
# # cherry
# # List is finished
#
# # E.g 4),
# # To exicute multyple list simatenasly using 'zip()' method
#
# adj1 = ['red', 'big', 'tasty']
# fruits1 = ['apple', 'banana', 'cherry']
# for x,y in zip(adj1,fruits1):
#     print(x,y)
# # o/p
# # red apple
# # big banana
# # tasty cherry
#
# # E.g 5),
# # 'pass' method is used to stop executing code
# for x,y in zip(adj1,fruits1):
#     pass
#     print(x,y)
# # o/p (output won't be there)
#
# # E.g 6)
# # unpacking dictionary using for loop
# D={'name':'Bob','age':25}
# for key, value in D.items():
#     print(key,value)
# # o/p
# #     name Bob
# #     Bob  25

# E.g 7),
# To reverse list using for loop
D = {
    'key1':'This is values for key1',
    'key2':'This is values for key2',
    'key3':'This is values for key3',
    'key4':'This is values for key4',
    'key5':'This is values for key5',
    'key6':'This is values for key6',
    'key7':'This is values for key7',
}

# *
l=list(D.keys()) #(Dictionary is converted into list using 'list()' method)
print(l)
# o/p ['key1', 'key2', 'key3', 'key4', 'key5', 'key6', 'key7']

# *
l2=sorted(l,reverse=True)
print(l2)
# o/p ['key7', 'key6', 'key5', 'key4', 'key3', 'key2', 'key1']

# *
reversed_key = sorted(l,reverse=True)
for key in reversed_key:
    val = D[key]
    print(val)

# o/p
# This is values for key7
# This is values for key6
# This is values for key5
# This is values for key4
# This is values for key3
# This is values for key2
# This is values for key1

# *
for val in D.values():
    print(val)
# o/p
# This is values for key1
# This is values for key2
# This is values for key3
# This is values for key4
# This is values for key5
# This is values for key6
# This is values for key7

# *
for key in D.keys():
    print(key)
# o/p
# key1
# key2
# key3
# key4
# key5
# key6
# key7

# *
for key in D:
    print(D[key])
# o/p
# This is values for key1
# This is values for key2
# This is values for key3
# This is values for key4
# This is values for key5
# This is values for key6
# This is values for key7


