#***NumGussr*** - A simple guess the number game
#The number is between 1 and 10
#the game asks for a hint every 5 turns
#there are two difficulties of hints, first hint is difficult, second hint is easier
#LICENSE: https://github.com/SpaceRanger21/number-guessing-game/blob/master/LICENSE
#© Made by SpaceRanger21 (https://github.com/SpaceRanger21/) ©

import random

#first and difficult hint
def hint1():
    print(f"The number is between {num-2} and {num+4}")

#second and easier hint
def hint2():
    print(f"The number is between {num-1} and {num+2}")

#the number which is to be guessed
num = random.randint(0,10)

#-----GAME STARTS-----
print("GUESS THE NUMBER GAME!! DO YOU WANT TO CONTINUE?")
input("Press Enter to continue...\n")

#variable responsible for hints
turns = 1
#statistical variables used at the end of the game
total_turns = 1
total_hints = 0

#first guess of the player
guess = int(input("Enter your guess: "))

#loop if first guess is not correct
while guess != num:
    print("\nIncorrect guess!")
    
    #hint determiner
    if turns == 5:
        confirmation = input("\nDo you want a hint? enter <yes> or <no>\n")
        #resets the variable responsible for hints
        turns = 0
        if confirmation == "yes":
            #hint difficulty determiner
            if total_hints == 0:
                hint1()
            else:
                hint2()
            
            total_hints += 1
   
    guess = int(input("Enter your guess: "))
    
    total_turns += 1
    turns += 1

print(f"\nCORRECT GUESS! YOU WON! You completed the game in {total_turns} turn(s) and used {total_hints} hint(s)")
#-----GAME ENDS-----
