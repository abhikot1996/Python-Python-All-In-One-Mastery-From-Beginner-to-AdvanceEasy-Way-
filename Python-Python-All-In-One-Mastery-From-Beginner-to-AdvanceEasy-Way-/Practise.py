# Calculate simple interest of given values
# pa = float(input("Enter principle amount: "))
# ri = float(input("Enter rate of interest: "))
# t  = float(input("Enter time: "))
# si = pa*ri*t/100
# print(si)

# Calculate volume of cuboid
# print("Enter lenth, bredth and hight: ")
# length, breadth, hight = float(input()), float(input()), float(input())
# # length  = float(input("Enter lenth of cuboid: "))
# # width   = float(input("Enter with of cuboid: "))
# # hight = float(input("Enter hight of cuboid: "))
# volume = length* breadth * hight
# print(volume)

# Program to Even or odd no
# d = int(input("Enter no: "))
# if d % 2 == 0  and d>=0:
#     print("Number is Even")
# else:
#     if d>=0:
#         print("Number is odd")
#     else:
#         print("Number is Negetive")

# No is Possitive or Negetive
# c = int(input("Enter no: "))
# if c>0:
#     print(f"{c} is positive no")
# elif c==0:
#     print(f"Number is 0")
# else:
#     print(f"{c} is negetive")

# Find greater no amongest three no
# print("Three numbers: ")
# c, d, e = int(input()), int(input()), int(input())
# if c > d and c > e:
#     print(f"{c} is greater number")
# elif d>e:
#     print(f"{d} is greater number")
# else:
#     print(f"{e} is greater number")

# Program to Leap year or not
# Year = int(input("Enter Year: "))
# if Year % 100 == 0:
#     if Year % 400 == 0:
#         print(f"{Year} is Leap Year")
#     else:
#         print(f"{Year} is not Leap Year")
# elif Year % 4 :
#     print(f"{Year}  Leap Year")
# else:
#     print(f"{Year} is not Leap Year")

# Program to find no of days in given month of year
# def days(days,month):
#     print(f"In month {month} days are {days}")
#
# print("Enter Year and Month: ")
# Year, Month  = int(input()), int(input())
# if Month == 1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12 :
#     days(31,Month)
#
# else:
#     if Month ==  4 or Month==6 or Month==9 or Month==11 :
#         days(30,Month)
#
#     else:
#         if Month == 2 :
#             if Year % 100==0:
#                 if Year % 400==0:
#                     days(29,Month)
#                 else:
#                     days(28,Month)
#             else:
#                 if Year % 4 == 0:
#                     days(29,Month)
#                 else:
#                     days(28,Month)

# Check if given no is prime or not
# no = int(input("Enter no: "))
# for i in range(2,no):
#     if no % i == 0:
#         print(f"{no} is not prime no")
#         break
#     else:
#         if i==no-1:
#             print(f"{no} is prime no")


# Find next prime no
# no = int(input("Enter no: "))
# j = 1
# while 1:
#     for i in range(2,no+j):
#         if(no+j)%i ==0:
#             j+=1
#             break
#     else:
#         if i == (no+j)-1:
#             print(f"Next Prime no is {i+1}")
#             break

# Check given number is Armstrong or not
# no = int(input("Enter no: "))
# # str1=len(str(no))
# temp = no, sum = 0
# while temp != 0:
#     digit = temp % 10
#     sum = digit ** 3 + sum
#     temp = temp // 10
#
# if no==sum:
#     print("Armstrog")
# else:
#     print("Not Armstrong")

# Armstrong number with in given number
# lower = int(input("Enter Lower limit: "))
# upper = int(input("Enter Upper limit: "))
# for num in range(lower, upper+1):
#     # Order of the number
#     order = len(str(num))
#     # Initialize sum
#     sum = 0
# #Find the sum of the cube of each digit
#     temp = num
#     while temp>0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //=10
# # Verify no is equeal to sum or not and print it
#     if num == sum:
#         print(num)


# Add two numbers
# print("Enter two numbers: ")
# a, b = int(input()), int(input())
# print(f"Addition of {a} and {b} is {a+b}")

# Prgram to Area of circle
# r = float(input("Enter radius of circle: "))
# A = 3.14 * r ** 2
# print(f"Area of circle is {A}")

# print("%d")
# a = int(input("a= "))
# b = int(input("b= "))
# print("Enter value of a and b ")

# Swaping two values
# a,b = int(input("a= ")), int(input("b= "))
# a = a+b
# b = a-b
# a = a-b
# print(f"a={a} and b={b}")

# Program to given value is divisible of 5 or not
# a = int(input("Enter value: "))
# if a % 5:
#     print(f"{a} is not divisiable of 5")
# else:
#     print(f"{a} is divisiable of 5")

# program to check given no is even or odd
# no = int(input("Enter number to check even or odd: "))
# if no<1:
#     print("Number should be natural number")
# elif no % 2 :
#     print(f"{no} is odd")
# else:
#     print(f"{no} is even")
#

# Program to find greater number between given two numbers
# no1, no2 = int(input("Enter first number: ")), int(input("Enter second number: "))
# if no1 > no2:
#     print(f"{no1} is greater than {no2}")
# elif no1<no2:
#     print(f"{no2} is greater than {no1}")
# else:
#     print("Both numbers are equal")

# Program to find greater no among three numbers
# print("Enter three numbers: ")
# no1,no2,no3=int(input()),int(input()),int(input())
# if no1>no2 and no1>no3:
#         print(f"{no1} is greater")
# else:
#     if no2>no3:
#         print(f"{no2} is greater")
#     else:
#         print(f"{no3} is greater")

# Program to check year is Leap year or not
# year = int(input("Enter year: "))
# if year % 100 == 0:
#     if year % 400 == 0:
#         print(f"{year} is Leap Year")
#     else:
#         print(f"{year} is not Leap Year")
#
# else:
#     if year % 4 == 0:
#         print(f"{year} is Leap Year")
#     else:
#         print(f"{year} is not Leap Year")

# print name five times using loop

# for _ in range(5):
#     print("Abhijit Kotkar  ")
# i=5
# while i>0:
#     print("Abhijit Kotkar")
#     i-=1

# Program to print first 10 natural numbers using loop
# for i in range(1,11):
#     print(i,end=" ")

# Program to print first n natural numbers
# no = int(input("Enter no: "))
# for i in range(1,no+1):
#     print(i,end=" ")

# Program to print first 10 natural numbers in reverse order
# i = 10
# for _ in range(10):
#     print(i,end=" ")
#     i-=1

# Program to print first n natural numbers in reverse order
# no = int(input("Enter no: "))
# for _ in range(1,no+1):
#     print(no,end=" ")
#     no-=1

# Program to print first 10 even natural numbers
# for i in range(1,11):
#     print(i*2,end=" ")

# Program to print first n even natural numbers
# no = int(input("Enter no: "))
# for i in range(1,no+1):
#     print(i*2,end=" ")

# Program to print user choice natural number
# print("Enter Upper and Lower limits of natural numbers: ")
# no1,no2 = int(input()),int(input())
# for i in range(no1,no2+1):
#     print(i,end=" ")

# Program to print user choice even natural numbers
# print("Enter Lower and Upper limits of even natural numbers: ")
# no1,no2 = int(input()), int(input())
# # j=0
# if no1%2:
#     no1+=1
#     j=no1
# else:
#     no1+=2
#     j=no1
# for _ in range(no1,no2+1):
#     if j<no2:
#         print(j,end=" ")
#         j+=2
#         if j==no2:
#             break

# program to print first n odd natural numbers
# no = int(input("Enter number: "))
# for i in range(no):
#     print(i*2+1,end=" ")

# program to print first n even natural numbers in reverse order
# no = int(input("Enter no: "))
# j = no*2
# for _ in range(no):
#     print(j,end=" ")
#     j-=2

# program to print first n odd natural numbers in reverse order
# no = int(input("Enter no: "))
# j= no*2-1
# for _ in range(no):
#     print(j,end=" ")
#     j-=2

# Program to print table user's choice
# table=int(input("Enter table no: "))
# for i in range(1,11):
#     print(f"{table} * {i} = {table*i}")

# Program to print sum of N natural numbers
# no = int(input("Enter no: "))
# j=0
# for i in range(1,no+1):
#    j+=i
# print(j)

# Program to calculate product of N natural numbers
# no = int(input("Enter no: "))
# j=1
# for i in range(1,no+1):
#     j*=i
# print(j)

# print factorial of N natural numbers
# no = int(input("Enter no: "))
# j=no
# k = 1
# for _ in range(1,no+1):
#     k*=j
#     j-=1
# print(k)

# # program to calculate sum of first n even natural numbers
# no = int(input("Enter no: "))
# j=0
# for i in range(1,no+1):
#     m = i *2
#     j+=m
# print(j)

# program to calculate sum of first n odd natural numbers
# no = int(input("Enter no: "))
# j=0
# for i in range(1,no+1):
#     m = i * 2 - 1
#     j+=m
# print(j)

# Program to calculate x power y
# print("Enter values of x and y: ")
# x,y = int(input()), int(input())
# print(x**y)

# Program to calculate digits of number
# no = int(input("Enter no: "))
# # no1=str(no)
# print(len(str(no)))

# Program to calculate sum of digits of given number
# no = int(input("Enter no: "))
# y= 0
# while no!=0:
#     x = no % 10
#     y = x + y
#     no = no//10
# print(f" Sum of digits : {y}")

# Program to reverse number
# no = int(input("Enter no : "))
# no1=str(no)
# # no2=no1(reverse=True)
# print(no1[::-1])

# Program to print Armstrong numbers b/w 1 to 1000
# print("Upper and Lower limit: ")
# no1,no2 = int(input()),int(input())
# for i in range(no1,no2+1):
#     digit = len(str(i))
#     j=i
#     y=0
#     while j!=0:
#         x = j%10
#         y = x**digit+y
#         j = j//10
#     if y == i:
#             print(i,end=" ")

# Program to print Armstrong numbers b/w 1 to 1000 YouTube Logic
# lower = int(input("Enter Lower limit : "))
# upper = int(input("Enter Upper limit : "))
# for num in range(lower,upper+1):
#     order = len(str(num))
#     sum=0
#     temp=num
#     while temp !=0:
#         digit =temp%10
#         sum+=digit ** order
#         temp //=10
#     if num == sum:
#         print(num)

# Program to print LCM(List Common Multiple) of two numbers
# print("Enter two numbers: ")
# no1,no2 = int(input()), int(input())
# for i in range(1,no1*no2+1):
#     if i % no1 == 0 and i % no2 == 0:
#         print(i)
#         break

# Program to print HCF ( Highest Common Factor) of two numbers
# print("Enter two numbers: ")
# no1,no2 = int(input()), int(input())
# if no1<no2:
#     min = no1
# else:
#     min = no2
# for i in range(1,min+1):
#     if no1%min == 0 and no2%min == 0:
#         print(min)
#         break
#     min-=1

# Program to find given number is Prime or not
# no = int(input("Enter no : "))
# for i in range(2,no):
#     if no%i==0:
#         print(f"{no} is not Prime number")
#         break
# else:
#     print(f"{no} is Prime number")

# Program to print all prime numbers b/w two numbers
# no1,no2 = int(input("Enter Lower limit: ")), int(input("Enter Upper limit: "))
# if no1 < 2 or no1>no2 :
#     print('''Lower limit should be greater than 1
# or Upper limit shold be greater
# than Lower limit ''')
# else:
#     for i in range(no1,no2+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(f"{i}",end=" ")

# Program to find Prime Factor of given number
# no = int(input("Enter no: "))
# j = 2
# while no != 1:
#     for i in range(2,j):
#         if j % i ==0:
#             # j+=1
#             break
#     else:
#         while no%j==0:
#             print(f"{j}",end=" ")
#             no//=j
#         # j+=1
#     j+=1

# Program to print n Fibonacci series
# no = int(input("Enter no: "))
# a = -1
# b = 1
# c = 0
# for i in range(1,no+1):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")

# Program to check given two numbers Co-Prime or not
# print("Enter no: ")
# no1, no2 = int(input()), int(input())
# if no1<no2:
#     min=no1
# else:
#     min=no2
# for i in range(2, min + 1):
#     if no1%i==0 and no2%i==0:
#         print(f"{no1} and {no2} are not Co-Prime numbers")
#         break
# else:
#     print(f"{no1} and {no2} are Co-Prime numbers")

# Program to print N Co-Prime numbers
# no = int(input("Enter no: "))
# a=2
# b=3
# index=1
# if a<b: min = a
# else: min = b
# while no!=0:
#     for i in range(2,min+1):
#         if a%i==0 and b%i==0:
#             if b<10:
#                 b+=1
#             else:
#                 a+=1
#                 b=2
#             break
#     else:
#             print(f"{index}. <{a},{b}>")
#             if b<10: b+=1
#             else:
#                 a+=1
#                 b=2
#             no-=1
#             index+=1

# Star Pattern
# 1)
# for r in range (1,6):
#     for c in range(1,6):
#         if c<=r:
#             print("*", end=" ")
#     print(end=" ""\n")

#  o/p
#  *
#  * *
#  * * *
#  * * * *
#  * * * * *

# 2)
# for rows in range(1,6):
#     for coloumn in range(1,6):
#         if coloumn>5-rows:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(end=" ""\n")

#  o/p
#          *
#        * *
#      * * *
#    * * * *
#  * * * * *

# 3)
# for r in range(1,6):
#     for c in range(1,6):
#         if c>=r:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(end=" " "\n")

# o/p
#  * * * * *
#    * * * *
#      * * *
#        * *
#          *

# 4) program to print following start pattern taking user input row numbers
# r1=int(input("Enter no of rows: "))
# c1=r1
# m=r1+1
# for r in range(1,r1+1):
#     for c in range(1,c1+1):
#         if c<=m-r:
#             print("*",end=" ")
#     print(end="" "\n")

#  o/p
#  Enter no of rows: 6
#  * * * * * *
#  * * * * *
#  * * * *
#  * * *
#  * *
#  *

# 5)
# for r in range(1,6):
#     for c in range(1,10):
#         if c>=6-r and c<=4+r: print(c,end=" ")
#         else: print(" ",end=" ")
#     print(end=" ""\n")

#  o/p
#          *
#        * * *
#      * * * * *
#    * * * * * * *
#  * * * * * * * * *

# 6)
# for r in range(1,6):
#     for c in range(1,10):
#         if r % 2:
#             if c>=6-r and c<=4+r:
#                 if c%2:
#                     print("*",end=" ")
#                 else:
#                     print(" ", end=" ")
#             else:
#                print(" ",end=" ")
#         else:
#             if c>=6-r and c<=4+r:
#                 if c%2==0:
#                     print("*",end=" ")
#                 else:
#                     print(" ", end=" ")
#
#             else:
#                 print(" ",end=" ")
#     print(end=" ""\n")

# o/p
#          *
#        *   *
#      *   *   *
#    *   *   *   *
#  *   *   *   *   *

# # 7)
# for r in range(1,6):
#     for c in range(1,10):
#         if c<=6-r or c>=4+r:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print(end=" ""\n")

# o/p
#   * * * * * * * * *
#   * * * *   * * * *
#   * * *       * * *
#   * *           * *
#   *               *

# 8)
# for r in range(1,5):
#     a=1
#     for c in range(1,8):
#         if c>=5-r and c<= 3+r:
#             if c<=4:
#                 print(a,end=" ")
#                 if c<4: a+=1
#             else:
#                 a-=1
#                 print(a,end=" ")
#         else: print(" ",end=" ")
#     print(end="\n")

# o/p
#        1        
#      1 2 1      
#    1 2 3 2 1    
#  1 2 3 4 3 2 1

# 9)
# for r in range(1,5):
#     a=1
#     for c in range(1,8):
#         if c<=5-r or c>=3+r:
#             if c<=4:
#                 print(a,end=" ")
#                 if c<4:
#                     a+=1
#             else:
#                 a-=1
#                 print(a,end=" ")
#         else:
#             print(" ",end=" ")
#     print(end="\n")

#  o/p
#  1 2 3 4 3 2 1
#  1 2 3   3 2 1
#  1 2       2 1
#  1           1

# 10)
# for r in range(1,8):
#     for c in range(1,8):
#         if r<5:
#             if c>=5-r and c<=3+r:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             if c>=r-3 and c<=11-r:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print(end="\n")

# o/p
#       *
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *

# 11)
# i=3
# for r in range(1,8):
#     for c in range(1,5):
#         if r<=4:
#             if c<=r:
#                 print("*",end="")
#         else:
#             if c<=i:
#                 print("*",end="")
#     if r>4:
#         i-=1
#     print(end="\n")

#  o/p
#  *
#  **
#  ***
#  ****
#  ***
#  **
#  *

# 12)
# i=7
# for r in range(1,5):
#     for c in range(1,8):
#         if c>=r and c<=i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     i-=1
#     print(end="\n")

# 13)
# length = 4
# for pos in range(1,length+1):
#     print("*"*pos)
# for pos in range(length-1,0,-1):
#     print("*"*pos)

# o/p
# *
# **
# ***
# ****
# ***
# **
# *

# 14)
# for r in range(1,5):
#     i=r
#     for c in range(1,8):
#         if c>=5-r and c<=3+r:
#             if c<=4:
#                 print(i,end=" ")
#                 if c<4:
#                     i+=1
#             else:
#                 i-=1
#                 print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print(end="\n")

#  o/p
#      1
#     2 3 2
#   3 4 5 4 3
# 4 5 6 7 6 5 4

# 15)
# for r in range(1,8):
#     i=7-r
#     for c in range(1,8):
#         if c<=8-r:
#             print(i,end=" ")
#             i-=1
#     print(end="\n")

# o/p
# 6 5 4 3 2 1 0
# 5 4 3 2 1 0
# 4 3 2 1 0 
# 3 2 1 0
# 2 1 0
# 1 0
# 0

# 16)
# for r in range(1,10):
#     i=1
#     for c in range(1,6):
#         if r<=5:
#             if c>=6-r:
#                 print(i,end=" ")
#                 i+=1
#             else:
#                 print(" ",end=" ")
#         else:
#             if c>=r-4:
#                 print(i,end=" ")
#                 i+=1
#             else:
#                 print(" ",end=" ")
#     print(end="\n")

# o/p
#          1
#        1 2
#      1 2 3
#    1 2 3 4
#  1 2 3 4 5
#    1 2 3 4
#      1 2 3
#        1 2
#          1

# 17)
# for r in range(1,8):
#     for c in range(1,8):
#         if c==r:
#             print("\\",end="")
#         elif c== 8-r:
#             print("/",end="")
#         else:
#             print("*",end="")
#     print(end="\n")

# o/p
# \*****/
# *\***/*
# **\*/**
# ***\***
# **/*\**
# */***\*
# /*****\

# 18)
# i=8
# for r in range(1,10):
#     for c in range(1,10):
#         if r<=5:
#             if c<=6-r or c>=4+r:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             if c<=r-4 or c>=i:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#     print(end="\n")
#     if r>5:
#         i-=1

#  o/p
#  * * * * * * * * *
#  * * * *   * * * *
#  * * *       * * *
#  * *           * *
#  *               *
#  * *           * *
#  * * *       * * *
#  * * * *   * * * *
#  * * * * * * * * *

# 19)
# for r in range(1,6):
#     for c in range(1,10):
#         if c>=r and c<=10-r:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print(end="\n")

# o/p
# *********
#  *******
#   *****
#    ***
#     *

# 20)
# for r in range(1,5):
#     for c in range(1,9):
#         if c>=5-r and c<=9-r:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print(end="\n")
#
#  o/p
#    *****
#   *****
#  *****
# *****   
