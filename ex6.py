import random

i = 0
computer = 0
user = 0
while i < 10:

    lst = ["stone", "paper", "scissor"]
    rand = random.choice(lst)
    # print(rand)
    print("Enter value from "
          "Stone "
          "Paper "
          "Scissor:-")
    a = input()
    b = a.lower()

    # if b == "stone" or b == "paper" or b == "scissor":

    if rand == "stone" and b == "stone":
        print("Draw")
    elif rand == "stone" and b == "paper":
        print("User win")
        user += 1
    elif rand == "stone" and b == "scissor":
        print("Computer win")
        computer += 1
    elif rand == "paper" and b == "paper":
        print("Draw")
    elif rand == "paper" and b == "stone":
        print("computer win")
        computer += 1
    elif rand == "paper" and b == "scissor":
        print("USer win")
        user += 1
    elif rand == "scissor" and b == "scissor":
        print("Draw")
    elif rand == "scissor" and b == "stone":
        print("User win")
        user += 1
    elif rand == "scissor" and b == "paper":
        print("Computer win")
        computer += 1
    i += 1

print(computer)
print(user)

if computer > user:
    print("Computer win the game")
else:
    print("User win the game")
