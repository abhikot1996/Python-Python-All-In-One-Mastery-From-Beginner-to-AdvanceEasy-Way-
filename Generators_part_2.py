'''
Generators part 2
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
print(next(gen_list))
print(next(gen_list))
print(next(gen_list))
print(next(gen_list))
# to get memory size of list using 'yield'
print(f"This generator takes {sys.getsizeof(gen_list)} bytes")

print('x'*20)

itr_list = []
for val in gen_list:
    itr_list.append(val)
# to get memory size of list using 'return'
print(f"This normal list takes {sys.getsizeof(itr_list)} bytes")

print('x'*20)

itr_list = []
for val in gen_list:
    itr_list.append(val)
# to get memory size of list using 'return'
print(f"This normal list takes {sys.getsizeof(itr_list)} bytes")
print(itr_list)