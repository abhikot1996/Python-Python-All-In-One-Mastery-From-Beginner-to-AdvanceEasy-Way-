# '''
# Recursive function
#     * Calling function into function
#
# '''
#
# # E.g 1),
# # def fact_fun(n):
# #     result = 1
# #     for n in range(2,n+1):
# #         result =result * n
# #     return result
# #
# # for i in range(1,10):
# #     print(i,fact_fun(i))
#
# # E.g 2),
# # Recursive function
# # def recursivefun(n):
# #     if n<=1:
# #         return 1
# #     else:
# #         a= n*recursivefun(n-1)
# #         return a
# #
# # for i in range(1,10):
# #     print(i,recursivefun(i))

# def fun_name(x,y):
#     print(x * y)
#     fun_name(x,y)
# fun_name(2,3)

# E.g 3),
def table (num,i):
    result = num*i
    print(f'{i}X{num}={result}')
    i+=1
    while i !=11:
        table(num,i)
        break
table(17,1)