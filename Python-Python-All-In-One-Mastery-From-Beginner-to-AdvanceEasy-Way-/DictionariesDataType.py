"""
Dictionaries Data Type
        * 'set' data type (sub datatype of dictionaries)
        * Unordered set of key value pare data type therefore
          we use the key to access the date
        * Dictionaries is used to find meaning of any keyword
        * syntax of dictionaries
            dictionary name = {'kay' : 'value'}
        * We can store any data in value of dictionaries
          (list, tuple, string, Dictionary)
        * key is immutable because key is identifiable
          object, we can't change key,
          we can't give data type to the key which is
          variable can be changed, also we can't give
          list because it is fix
        * Key must be Immutable

"""
# E.g 1),
# Defining dictionaries
dict_a={'key1':'value1',
        'key2':'value2',
        'key3':'value3',
        'key4':'value4',
        'key5':'value5'}
print(dict_a)
# o/p {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}

# E.g 2),
# Accessing value from dictionary 1
print(dict_a['key1'])
# o/p value1

# E.g 3),
# 'get' method is used to find value
print(dict_a.get('key6'))
# o/p None

# E.g 4),
# Accessing data from dictionary 2
car = {
    'model':'suzuki',
    'year' :[2006,2003,2006],
    'color':('black','red'),
    'docs' :{'original':'yes','duplicate':'No'}
}
print(car['model'])
# o/p suzuki

print(car['year'])
# o/p [2006, 2003, 2006]

print(car['color'])
# o/p ('black', 'red')

print(car['docs'])
# o/p {'original': 'yes', 'duplicate': 'No'}

# E.g 5),
# Accessing elements from dictionary with the indexing (if value is list or string or tuple)
print(car['year'][0])
# o/p 2006

# E.g 6),
# Accessing elements from dictionary with the indexing (if value is list or string or tuple)
print(car['color'][0])
# o/p black

# E.g 7),
# Accessing elements from dictionary with the indexing (if value is list or string or tuple)
print(car['docs']['duplicate'])
# o/p No

    