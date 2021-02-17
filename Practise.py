
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.''')
# x=5
# for i in range(1,11):
#     for j in range (1,11):
#         print(f"{i}*{j} : {i*j}")
#     print("x"*15)
#
# x = int(input("Enter first no: "))
# y = int(input("Enter second no: "))
#
# print(f"addition of {x} and {y}  is {x+y}")

# r = int(input("Enter radious : "))
# area = 3.14*r**2
# print(area)
# pa = float(input("Enter principle amount: "))
# ri = float(input("Enter rate of interest: "))
# t  = float(input("Enter time: "))
# si = pa*ri*t/100
# print(si)

print("Enter lenth, bredth and hight: ")
length, breadth, hight = float(input()), float(input()), float(input())
# length  = float(input("Enter lenth of cuboid: "))
# width   = float(input("Enter with of cuboid: "))
# hight = float(input("Enter hight of cuboid: "))
volume = length* breadth * hight
print(volume)