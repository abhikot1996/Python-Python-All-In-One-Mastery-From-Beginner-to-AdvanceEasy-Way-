"""
Some Famous Modules
    * if want to use another models which is not built in with python we can download
      them from Online pypi library (pypi.org)
    * if want to download
        steps,
            * in terminal of IDE type - pip install django

"""

# # E.g 1),
# # random module ( for the random numbers )
# import random
# x=random.randint(1,10)
# print(x)
#
# # E.g 2),
# # datetime module ( for the date and time )
# import datetime
# date = datetime.datetime.now()
# print(date)
#
# # to calculate dob
# dob = datetime.date(1996,9,26)
# today = datetime.date.today()
# age = today - dob
# print(age)
# print(180/363)

# E.g 2),
# timeit module (To get time of executing program)
import timeit
print('-'.join(str(n)for n in range(100)))
print(timeit.timeit("'-'.join(str(n)for n in range(100))",number=100))

# E.g 3),
# importing one file in to another file in the same folder
# use (from) keyword and (filename) and then (what you want to import)
from Functions import add3
print(add3(4)) # imported function called


