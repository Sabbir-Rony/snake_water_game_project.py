computer = 1
you = input("Enter your choice : ")
youDict = {"s":1, "w":-1, "g":0}

youStr = youDict[you]

if(computer == youStr):
    print("Its A Draw")

else:
    if(computer == -1 and youStr == 1):
        print("Your are win")
    elif(computer == -1 and youStr == 0):
        print("Your are Lose")
    elif(computer == 1 and youStr == -1):
        print("Your are Lose")
    elif(computer == 1 and youStr == 0):
        print("Your are win")
    elif(computer == -1 and youStr == 1):
        print("Your are Lose")
    elif(computer == 1 and youStr == 0):
        print("Your are Lose")
    elif (computer == 0 and youStr == -1):
        print("Your are win")
    elif (computer == 1 and youStr == 1):
        print("Your are Lose")
    elif (computer == 1 and youStr == -1):
        print("Your are Lose")
    else:
        print("Something is wrong")


