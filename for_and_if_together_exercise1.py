'''
for and if together exercise
'''

# continue
grocy_list1 = ['milk','pasta','eggs','cheez','bread','rice']
for i in grocy_list1:
    if i == 'cheez':
        print("I don't buy "+i )
        continue
    print("I buy "+i)


# Break
grocy_list = ['milk','pasta','eggs','cheez','bread','rice']
taken_items=input("Enter taken item: ")
for i in grocy_list:
    if taken_items in grocy_list:
        print(f'{taken_items} is in list buy it')
        break

    elif taken_items not in grocy_list:
        print(f"{taken_items} is not in list don't buy it ")
        break
