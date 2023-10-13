import random
import time

#simple dice roll simulator that can take the number of dice to be rolled


while True:

    dice_number = int(input("Enter the dice number : "))
    counter = 1
    
    while dice_number > 0 :        
        
        
        print("dice number " + str(counter) + " is " + str(random.randint(1,6)))
        
        counter += 1
        dice_number = dice_number - 1
    
    flag = int(input("Enter 0 to exit or any other numbers to roll again \n"))
    
    if flag == 0:
        break
    
    