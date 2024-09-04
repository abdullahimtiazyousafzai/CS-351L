import random

high = 100

low = 0

max_attempts = 100

attempts = 0

while attempts < max_attempts:
    guess = low + high // 2 # guessing the middle element
    attempts += 1

    print(f"AI's guess is : {guess}")
    inpt = input("Is this number high, low or correct? : ")
    if inpt.lower() == "h":
        high = guess
    elif inpt.lower() == "l":
        low = guess
    elif inpt.lower() == "c":
        print(f"AI found the number in {attempts} attempts")
        break
    else:
        print("Invalid input. Please enter 'h' for high, 'l' for low or c for correct")
        
