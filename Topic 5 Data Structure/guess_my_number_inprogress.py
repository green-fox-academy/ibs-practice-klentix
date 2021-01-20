#Write a program where the program chooses a number between 1 and 100.
#The player is then asked to enter a guess.
#If the player guesses wrong, then the program gives feedback and ask to enter an other guess until the guess is correct.

#Make the range customizable (ask for it before starting the guessing).
#You can add lives.
#I've the number between 1-100. You have 5 lives.
#> 20
#Too high. You have 4 lives left.
#> 10
#Too low. You have 3 lives left.
#> 15
#Congratulations. You won!



import random

def random_number():
    while True:
        try:
            num = int(input("range between 1 and  "))
        except ValueError:
            print("that s not a number")
            continue
        if num < 2 :
            print ("must be more than 2")
        else:
            print ("guess between 1 and" + str(num))
            guess_number = random.randrange(1,num,1)
            return guess_number
