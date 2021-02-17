'''
Nested if else
'''

x = input("Enter your first location : ")
y = input("Enter your second location : ")

if x == "Right":
    if y == "Up":
        print(f'You are at the {x} and {y} loction')
    else:
        print(f'You are at the {x} and {y} location')
else:
    if y == "Up":
        print(f'You are at the {x} and {y} location')
    else:
        print(f"You are at the {x} and {y} location")

# o/p
# Enter your first location : Right
# Enter your second location : Up
# You are at the Right and Up location

# Enter your first location : Right
# Enter your second location : Left
# You are at the Right and Left location

# Enter your first location : Left
# Enter your second location : Up
# You are at the Left and Up location

# Enter your first location : Left
# Enter your second location : Down
# You are at the Left and Down location












