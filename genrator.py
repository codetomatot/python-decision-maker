import random

choiceList = []

choice1 = str(input("Choice 1: "))
choice2 = str(input("choice 2: "))

if choice1 and choice2:
    choiceList.append(choice1)
    choiceList.append(choice2)
    #choiceList.append(choice3)

answer = random.choice(choiceList)
#print(choiceList)
print(answer)