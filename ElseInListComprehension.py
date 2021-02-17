'''
Else in List Comprehension
'''

# E.g 1),
list_ = [['A','B','C'],['D','E','F'],['G','E','F'],['G','H','I']]
list_s = []
for letter in list_:
    if 'G' not in letter:
        list_s.append(letter)
    else:
        list_s.append('Letter was skipped')

print(list_s)
# o/p [['A', 'B', 'C'], ['D', 'E', 'F'], 'Letter was skipped', 'Letter was skipped']

# E.g 2),
# List comprehesion else
list_sc = [letter if 'G' not in letter else 'Letter was skipped' for letter in list_]
print(list_sc)
# o/p [['A', 'B', 'C'], ['D', 'E', 'F'], 'Letter was skipped', 'Letter was skipped']
