'''
Jungle Rescuer Challenge Game
'''

avaiable_exit = "UpRight"
choosen_exit = " "
while choosen_exit not in avaiable_exit:
    choosen_exit = input("Where are you: ")
    if choosen_exit == avaiable_exit:
        print("You are saved from Lion King")
        print("Game Over")
        break
else:
    print("You got out on first try")
