import random

while True:
    try:
        #Input
        lev = input("Level: ")
        #Check if level is a number
        if lev.isnumeric():
            lev = int(lev)
        else:
            raise Exception
        #Check if level positive, break if it is
        if lev > 0:
            break
        else:
            raise Exception
    except:
        pass

n = random.randint(1,lev)
guess=0

while guess != n:
    guess = input('Guess: ')
    #Check if input is numer
    if guess.isnumeric():
        guess= int(guess)
    else:
        continue
    if guess > n:
        print('Too large!')
    elif guess < n:
        print('Too small!')
    else:
        print('Just right!')
        break