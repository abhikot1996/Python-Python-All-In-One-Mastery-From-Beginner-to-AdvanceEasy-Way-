'''
Reading Data From File
    * Modes of file reading,
        * 'read()' method is used to read indivisual characters in file.
        * 'readline()' method is used to read single line at time in file.
        * 'readlines()' method is used to read all lines once in file.

'''

# E.g 1),
# 'r' mode
#'open()','r' methods are used to open and read file ('r' - read onley)
# file = open('Level 4.1.txt','r')
# for line in file :
#     print(line)
# file.close()

# E.g 2),
# To find any word and print that line from file even if it word is small letters or capital letters
# file = open('Data Mining and Data Ware Housing.txt','r')
# for line in file:
#     if 'data' in line.lower():
#         print(line)
# file.close()

# E.g 3),
# Accessing file from another folder or path
# file = open('E:\\Data Mining and Data Ware Housing.txt','r')
# for line in file:
#     print(line)
# file.close()

# E.g 4),
# 'with open()' if we use this method there is no need to use 'close()' method always
# file = open('Data Mining and Data Ware Housing.txt','r')
# with open('Data Mining and Data Ware Housing.txt','r') as file:
#     for line in file:
#         print(line)

# using 'readline()' built in method
# 'end =' method is used to deside the space of words
# file = open('Data Mining and Data Ware Housing.txt','r')
# with open('Data Mining and Data Ware Housing.txt','r') as file:
#     line = file.readline()
#     while line:
#         print(line,end='')
#         line = file.readline()

# E.g 5),
# 'readlines()' method is used to convert all lines in list
# with open('Data Mining and Data Ware Housing 1.txt','r') as file:
#     lines_list = file.readlines()
# print(lines_list)
# for line in lines_list[::-1]:
#     print(line,end='')
#
# print('x'* 100)

# with open ('Data Mining and Data Ware Housing 1.txt','r') as file:
#     characters = file.read()
#     print(characters)
# print('x'*100)
# for char in characters[::-1]:
#     print(char,end='')
# print('x'*100)








