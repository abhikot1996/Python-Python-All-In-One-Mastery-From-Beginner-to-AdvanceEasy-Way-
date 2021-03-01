# """
# if and elif statement
#     *syntax
#         if condition:
#            block of code
#         elif condition:
#             block of code
#         else:
#             block of code
# """
#
# # E.g 1),
# # num = int(input("Enter no: "))
# # if num>0:
# #     print("Natural number")
# # else:
# #     print("Not natural number")
#
# # o/p
# # Enter no: 2
# # Natural number
# #Enter no: 0
# # Not natural number
#
#
# # E.g 2),
# num1=int(input("Enter number: "))
# if num1%4==0:
#     print(f'{num1} is  divisiable of 4')
# else:
#     print(f'{num1} is not divisiable of 4')
#
# # o/p
# # Enter number: 20
# # 20 is  divisiable of 4
# # Enter number: 21
# # 21 is not divisiable of 4
#
# E.g 3)
# marks = int(input("Please enter your marks: "))
# passing_marks = 50
#
# if marks>= passing_marks:
#     print("Your are Pass")
# else:
#     print("Your are Fail")

# o/p
# Please enter your marks: 51
# Your are Pass
# Please enter your marks: 49
# Your are Fail`
# Please enter your marks: 50
# Your are Pass

# E.g 4)
# elif statement
sound = input("What kind of sound do you like: ")
if sound == 'meo':
     print("You love cats, cat person")
elif sound == 'wuf':
     print("You love dogs, dog person")
else:
     print("You don't love cats or dog")

# o/p
# What kind of sound do you like: meo
# You love cats, cat person

# What kind of sound do you like: wuf
# You love dogs, dog person

# What kind of sound do you like: hup
# You don't love cats or dog


