'''
for and if together
'''

ip = input("Enter number: ")
cln_num=''
for i in range(0,len(ip)):
    if ip[i] in '0123456789':
        cln_num=cln_num+ip[i]
num_int=int(cln_num)
print(num_int)
