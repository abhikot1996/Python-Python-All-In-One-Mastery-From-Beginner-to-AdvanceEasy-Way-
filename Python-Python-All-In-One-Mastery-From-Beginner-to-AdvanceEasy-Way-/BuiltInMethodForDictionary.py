"""
Builtin method in dictionary
"""

car = { 'model':'suzuki',
        'year' :[2006,2003,2006],
        'color':('black','red'),
        'docs' :{'original':'yes','duplicate':'no'}
      }

# E.g 1),
# print(car)
# print(car['model'])
# print(car['year'][1])
# print(car['color'][1])
# print(car['docs']['original'])


# E.g 2),
# To change value of key in dictionary
car['model']= 'toyota'
print (car)
# o/p {'model': 'toyota', 'year': [2006, 2003, 2006], 'color': ('black', 'red'),
#     'docs': {'original': 'yes', 'duplicate': 'no'}}

# E.g 3),
# To add new key and value
car['tyers'] = 'no'
print(car)
# o/p {'model': 'toyota', 'year': [2006, 2003, 2006], 'color': ('black', 'red'),
#      'docs': {'original': 'yes', 'duplicate': 'no'}, 'tyers': 'no'}

# E.g 4),
# 'items()' method is used to get all keys and values of Dictionary (Returns as a Tuple)
print(car.items())
# o/p dict_items([('model', 'toyota'), ('year', [2006, 2003, 2006]),
#     ('color', ('black', 'red')), ('docs', {'original': 'yes', 'duplicate': 'no'}),
#     ('tyers', 'no')])

# E.g 5),
# Unpacking dictionary (Returns as a Tuple)
a,b,c,d,e = car.items()
print(a) # o/p  ('model', 'toyota')
print(b) # o/p  ('year', [2006, 2003, 2006])
print(c) # o/p  ('color', ('black', 'red'))
print(d) # o/p  ('docs', {'original': 'yes', 'duplicate': 'no'})
print(e) # o/p  ('tyers', 'no')

# E.g 6),
# 'keys()' function is used to get only keys of dictionary (Returns as a list)
print(car.keys())
# o/p dict_keys(['model', 'year', 'color', 'docs', 'tyers'])

# E.g 7),
# To access specific item
a,b,c,d,e = car.keys()
print(a)  # o/p model
print(b)  # o/p year
print(c)  # o/p color
print(d)  # o/p docs
print(e)  # o/p tyers

# E.g 8),
# 'values()' method is used to get only values
print(car.values())
# o/p dict_values(['toyota', [2006, 2003, 2006], ('black', 'red'),
#       {'original': 'yes', 'duplicate': 'no'}, 'no'])

# E.g 9),
# Unpacking values
a,b,c,d,e = car.values()
print(a) # o/p toyota
print(b) # o/p [2006, 2003, 2006]
print(c) # o/p ('black', 'red')
print(d) # o/p {'original': 'yes', 'duplicate': 'no'}
print(e) # o/p no

# E,g 10),
# 'dict()' method to create dictionary
# Converting tuple to dictionary
new_dict = dict([('model','toyota'),('year',[2006,2003,2006]),('color',('black','red'))])
print(new_dict)
# o/p {'model': 'toyota', 'year': [2006, 2003, 2006], 'color': ('black', 'red')}
#     (Dictionary is cteated with the help of 'dict()' method)

# E.g 11),
# 'pop()' method is used to remove whole pair of key and value of the dictionary ( must give key as argument )
# to remove form list only not form memory
new_dict.pop('year')
print(new_dict)
# o/p {'model': 'toyota', 'color': ('black', 'red')}

# E.g 12),
# 'popitem()' to remove last pair of key and value
# to remove form list only not form memory
new_dict.popitem()
print(new_dict)
# o/p {'model': 'toyota'}

# E.g 13),
# 'del' method is used to delete element from dictionary (give key as a argument)
del new_dict['model'] # Give argument or whole dictionary will be deleted from memory
print(new_dict)
# o/p {'year': [2006, 2003, 2006], 'color': ('black', 'red')}



