#Dice Simulator
#Variables used ---> toRoll = to get the input of choice 
import random

while True:
    toRoll = str(input("Enter (y/n) to roll a dice = "))
    if toRoll in ["y", "Y"]:
        print("You rolled", random.randint(1, 6))
    elif toRoll in ["n", "N"]:
        print("You are being Exited")
        exit()
    else:
        print("Invalid input, please enter 'y' or 'n'.")
