'''
Prime no
        * Number which can divide only itself
'''

num = int(input("Enter no: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime no")
            break
    else:
        print(f"{num} is prime no")
else:
    print(f"{num} is not prime no")