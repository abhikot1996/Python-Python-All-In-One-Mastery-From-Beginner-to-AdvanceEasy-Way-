'''
Nested For Loop
'''

# E.g 1),
# num1 =int(input('Enter which table you want : '))
# for i in range(1,11):
#     print(f'{num1} * {i} =  {num1 * i}')
# # o/p
# # Enter which table you want : 2
# # 2 * 1 =  2
# # 2 * 2 =  4
# # 2 * 3 =  6
# # 2 * 4 =  8
# # 2 * 5 =  10
# # 2 * 6 =  12
# # 2 * 7 =  14
# # 2 * 8 =  16
# # 2 * 9 =  18
# # 2 * 10 =  20


# E.g 2),
# Tables of 1 to 10
num = int(input("Enter no of table : "))
for i in range (1,num+1):
   print(f'This is table of {i}')
   for j in range (1,11):
       print(f'    {i} * {j} : {i*j}')
   print('x' * 20)

# o/p
# This is table of 1
#     1 * 1 : 1
#     1 * 2 : 2
#     1 * 3 : 3
#     1 * 4 : 4
#     1 * 5 : 5
#     1 * 6 : 6
#     1 * 7 : 7
#     1 * 8 : 8
#     1 * 9 : 9
#     1 * 10 : 10
# xxxxxxxxxxxxxxxxxxxx
# This is table of 2
#     2 * 1 : 2
#     2 * 2 : 4
#     2 * 3 : 6
#     2 * 4 : 8
#     2 * 5 : 10
#     2 * 6 : 12
#     2 * 7 : 14
#     2 * 8 : 16
#     2 * 9 : 18
#     2 * 10 : 20
# xxxxxxxxxxxxxxxxxxxx
# This is table of 3
#     3 * 1 : 3
#     3 * 2 : 6
#     3 * 3 : 9
#     3 * 4 : 12
#     3 * 5 : 15
#     3 * 6 : 18
#     3 * 7 : 21
#     3 * 8 : 24
#     3 * 9 : 27
#     3 * 10 : 30
# xxxxxxxxxxxxxxxxxxxx
# This is table of 4
#     4 * 1 : 4
#     4 * 2 : 8
#     4 * 3 : 12
#     4 * 4 : 16
#     4 * 5 : 20
#     4 * 6 : 24
#     4 * 7 : 28
#     4 * 8 : 32
#     4 * 9 : 36
#     4 * 10 : 40
# xxxxxxxxxxxxxxxxxxxx
# This is table of 5
#     5 * 1 : 5
#     5 * 2 : 10
#     5 * 3 : 15
#     5 * 4 : 20
#     5 * 5 : 25
#     5 * 6 : 30
#     5 * 7 : 35
#     5 * 8 : 40
#     5 * 9 : 45
#     5 * 10 : 50
# xxxxxxxxxxxxxxxxxxxx
# This is table of 6
#     6 * 1 : 6
#     6 * 2 : 12
#     6 * 3 : 18
#     6 * 4 : 24
#     6 * 5 : 30
#     6 * 6 : 36
#     6 * 7 : 42
#     6 * 8 : 48
#     6 * 9 : 54
#     6 * 10 : 60
# xxxxxxxxxxxxxxxxxxxx
# This is table of 7
#     7 * 1 : 7
#     7 * 2 : 14
#     7 * 3 : 21
#     7 * 4 : 28
#     7 * 5 : 35
#     7 * 6 : 42
#     7 * 7 : 49
#     7 * 8 : 56
#     7 * 9 : 63
#     7 * 10 : 70
# xxxxxxxxxxxxxxxxxxxx
# This is table of 8
#     8 * 1 : 8
#     8 * 2 : 16
#     8 * 3 : 24
#     8 * 4 : 32
#     8 * 5 : 40
#     8 * 6 : 48
#     8 * 7 : 56
#     8 * 8 : 64
#     8 * 9 : 72
#     8 * 10 : 80
# xxxxxxxxxxxxxxxxxxxx
# This is table of 9
#     9 * 1 : 9
#     9 * 2 : 18
#     9 * 3 : 27
#     9 * 4 : 36
#     9 * 5 : 45
#     9 * 6 : 54
#     9 * 7 : 63
#     9 * 8 : 72
#     9 * 9 : 81
#     9 * 10 : 90
# xxxxxxxxxxxxxxxxxxxx
# This is table of 10
#     10 * 1 : 10
#     10 * 2 : 20
#     10 * 3 : 30
#     10 * 4 : 40
#     10 * 5 : 50
#     10 * 6 : 60
#     10 * 7 : 70
#     10 * 8 : 80
#     10 * 9 : 90
#     10 * 10 : 100
# xxxxxxxxxxxxxxxxxxxx

