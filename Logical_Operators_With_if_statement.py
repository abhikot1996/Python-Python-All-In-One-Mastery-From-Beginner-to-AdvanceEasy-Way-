'''
Logical Operators with if statement
'''

# # E.g 1),
# num = int(input("Enter No: "))
# if (num>5 and num < 10):
#     print(f"{num} is in limit")
#
# # E.g 2),
# num = int(input("Enter No: "))
# if (num>5 or num < 10):
#     print(f"{num} is in limit")

# E.g 3),
sentence = "A quick brown fox jumps on the lazy dog"
string = input("Enter string: ")
if string in sentence:
    print(f"{string} does exist in the sentence ")
elif string not in sentence:
    print(f"{string} does not exist in sentence")

