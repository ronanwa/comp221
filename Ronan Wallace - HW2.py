## Author: Ronan Wallace
## Title: HW2
## Date: 02/28/19

import math

# User interface and calling of hanoi(); restarts games if user wants
def main():
    print("-"*50,"\nTower of Hanoi: Number of Moves to Solve\n"+"-"*50)
    x=1
    while(x==1):
        disks = input("\nHow many disks are there? ")
        try:
            disks=eval(disks)
            hanoi(disks)
            answer=input("Would you like to play another game? (y/n) ")
            if answer == "y":
                x=1
            elif answer == "n":
                x=0
        except:
            print("Input must be an integer.\n")
            
        
# Calculates the number of moves required to solve a Hanoi puzzle of n disks; catches input errors as well
def hanoi(disks):
    if disks < 0:
        print("Input must be a positive integer.\n")
    elif math.floor(disks)!=disks:
        print("Input must be a positive integer.\n")
    elif type(disks) != int:
        print("Disk input must be an integer.\n")
    else:
        moves=math.floor(math.pow(2,disks)-1)
        print(moves,"moves to complete a puzzle of",disks,"disks.\n")


main()


