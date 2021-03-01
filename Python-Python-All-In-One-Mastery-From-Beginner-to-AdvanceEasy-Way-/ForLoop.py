"""
For Loop

"""

a = [1,2,3,4,5,6,7,8,9]

# E.g 1),
# Defining For Loop
for var_a in a:
    print(var_a)
print('x'*20)

# o/p
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# E.g 2),
for var_a in a:
    print(f'I am running for : {var_a}')

# o/p
# I am running for : 1
# I am running for : 2
# I am running for : 3
# I am running for : 4
# I am running for : 5
# I am running for : 6
# I am running for : 7
# I am running for : 8
# I am running for : 9

# E.g 3),
for i in range(11):
    print(f'2 * {i} : {i*2}')
# o/p
# 2 * 0 : 0
# 2 * 1 : 2
# 2 * 2 : 4
# 2 * 3 : 6
# 2 * 4 : 8
# 2 * 5 : 10
# 2 * 6 : 12
# 2 * 7 : 14
# 2 * 8 : 16
# 2 * 9 : 18
# 2 * 10 : 20

# E.g 4),
cupboard = ['shirt', 't-shirt','pant', 'jeans pant', 'chaddi', 'bunyan']
num=len(cupboard)
print(num)
for item in cupboard:
    print(item)
# o/p
# shirt
# t-shirt
# pant
# jeans pant
# chaddi
# bunyan

#E.g 5),
print('x'*30)
for i in range(len(cupboard)):
    print([i],cupboard[i])
# o/p
# [0] shirt
# [1] t-shirt
# [2] pant
# [3] jeans pant
# [4] chaddi
# [5] bunyan


