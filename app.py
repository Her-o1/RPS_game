import random
print("Welcome to the ROCK, PAPER, SCISSORS game. You will be competing against the CPU")
print("R for Rock")
print("P for Paper")
print("S for Scissors")

#list of possible choices
choices = ["R", "P", "S"]
#user input
Player = input("Select R (rock), P (paper) or S (scissors) : ").upper()
#CPU choosing at random
CPU = random.choice(choices).upper()
#What both players select
print(f'Player ({Player}) : CPU ({CPU})')

#Selecting a winner
while Player in choices:
    if Player == CPU:
        print("Tie, please play again")
        Player = input("Select R (rock), P (paper) or S (scissors) : ")
        continue
    elif Player == "R" and CPU == "P":
        print("CPU Won")
        break
    elif Player == "P" and CPU == "S":
        print("CPU Won")
        break
    elif Player == "S" and CPU == "R":
        print("CPU Won")
        break
    else:
        print("You Won !!")
        break
       
else:
    print("Invalid Choice!")
