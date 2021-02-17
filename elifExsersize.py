'''
elif Exercises
'''

amount = int(input("Enter amount: "))
if amount < 1000:
    discount = amount * 0.05
    print(f'Discount is {discount}')
elif amount < 5000:
    discount = amount * 0.10
    print(f'Discount is {discount}')
else:
    discount = amount * 0.15
    print(f'Discount is {discount}')

# o/p
# Enter amount: 999
# Discount is 49.95

# Enter amount: 2399
# Discount is 239.9

# Enter amount: 7000
# Discount is 1050.0

