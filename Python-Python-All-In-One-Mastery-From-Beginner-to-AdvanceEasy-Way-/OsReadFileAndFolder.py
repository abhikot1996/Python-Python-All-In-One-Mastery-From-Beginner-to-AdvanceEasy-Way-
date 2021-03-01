"""
Os read file and folder
"""
# Reading files and folders with the help of built in function
# E.g 1),
# import os
# list_os = os.walk('E:\\AK\\Study\\Programming Languages\\Programming Languages in Hindi videos\\2021\\01.Python All In One Mastery From Beginner to AdvanceEasy Way\Python Programs')
# for root, direct, files in list_os:
#     print(root)
#     for i in direct:
#         print(i)
#     for j in files:
#         print(j)

# E.g 2),
# Searching files or folders
import os
search = input("Enter name of file which you want to find: ")
list_os = os.walk('E:\\AK\\Study\\Programming Languages\\Programming Languages in Hindi videos\\2021\\01.Python All In One Mastery From Beginner to AdvanceEasy Way\Python Programs')
for root, direct, files in list_os:
    # print(root)
    # for i in direct:
    #     print(i)
    for j in files:
        if search in j:
            print(j)

# User defind function to read folder and files
