#Importing required modules
import random
import os
import time
from termcolor import colored

#Function for clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

#For starting the stimulator
print(colored("This is a dice stimulator...", 'green', attrs=['bold']))
time.sleep(2)

a = input(colored("\nEnter 'roll' to start the simulator: ", 'blue', attrs=['bold']))

if a == 'roll':
    pass

else:
    print(colored("Wrong input!", 'red', attrs=['bold']))
    exit()

#While loop to do the stimulation again and again
while True:
    
    #For randomly selecting between the different faces of the dice
    number = random.randint(1,6)

    #Conditions for the different faces of a dice
    if number == 1:
        
        print()
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
        
    if number == 2:
        
        print()
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
        
    if number == 3:
        
        print()
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
        
    if number == 4:
        
        print()
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
        
    if number == 5:
        
        print()
        print("----------")
        print("| O    O |")
        print("|    0   |")
        print("| O    O |")
        print("----------")
        
    if number == 6:
        
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
        

    #Condition for doing the stimulation again
    x = input(colored("\nDo You want to roll again(y/n): ", 'green', attrs=['bold']))
    
    if x == "y":
        pass
    
    elif x == "n":
        print(colored("\nThank You!", 'yellow', attrs=['bold']))
        exit()
        
    else:
        print(colored("\nWrong Input!", 'red', attrs=['bold']))
        exit()

