'''
Appending File
'''

# Appending File
with open('newbucket.txt','a') as tem_bucket:
    for i in range(1,11):
         for j in range(1,11):
            print(f"{i} * {j} : {i*j}",file=tem_bucket)
         print("-"*15,file=tem_bucket)
