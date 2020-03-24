print ("Welcome to the guessing game. You will need to guess the number I am thinking of from one to twenty")
import random
value = random.randint(1, 20)
guessingnumber = value
for x in range(3):
    print ("Please input your guess")
    playerguess = input()
    if int(playerguess) > 20:
        print ("Enter a number below 20")
    if guessingnumber == int(playerguess):
        print ("Congratulations you botface you won!")
        break
    elif guessingnumber > int(playerguess):
        print ("Too low you dummy")
    elif guessingnumber <  int(playerguess):
        print ("too high")
   