import random

max_attempts = 100

attempts = 0

numberguess = random.randint(1,100)

guess = 0

while attempts < max_attempts:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    
    if guess < numberguess:
        print("Too low, try again!")
    elif guess > numberguess:
        print("Too high, try again!")
    else:
        print("Congratulations, you guessed the number in", attempts, "attempts!")
        break