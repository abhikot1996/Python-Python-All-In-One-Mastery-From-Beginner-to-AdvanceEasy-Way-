'''
Generators part 1
        * Generators syntax same as function but it except of 'return' value 'yield' value
        * 'yield' in generators basically  on the get go it give you value and pause the function
           and wait for the call to we ask for the next value and it return us next value
           therefore 'yield' is consume less value thant 'return'
'''

import sys # to get memory size
# E.g 1),
# Generator
def my_gen(n:int):
    start = 0
    while start < n:
        print(f'My range is returning : {start}')
        yield start
        start += 1

gen_list = my_gen(10)
# to get memory size of list using 'yield'
print(f"This generator takes {sys.getsizeof(gen_list)} bytes")

print('x'*20)

itr_list = []
for val in gen_list:
    itr_list.append(val)
# to get memory size of list using 'return'
print(f"This normal list takes {sys.getsizeof(itr_list)} bytes")
