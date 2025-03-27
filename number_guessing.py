# Code For the simple number guessing game(Wriiten by LK)

import random

print("Welcme to the number guessing Game!!")

are_play = input("Are you play game(yes or no): ")  # Checking the play game

if are_play.lower() != "yes":
    quit

# input higher number for range
number_range = input("Enter Your Top number: ")

# Cheking if a number is a digit
if number_range.isdigit():
    number_range = int(number_range)

    # checking value is larger than 0
    if number_range <= 0:
        print("Please Enter larger number than 0!!")
        quit()

else:
    print("Please Enter valid number!!")

random_number = random.randint(0, number_range)  # random number

guess_chance = 0

# while loop for check guess number
while True:
    guess_chance += 1

    guess_number = input("Please Enter Guess number: ")

    # Checking if a guessing number is digit
    if guess_number.isdigit():
        guess_number = int(guess_number)

    else:
        print("please Enter Valid Number!!")
        continue

    # checking guessing number equal to random nmber
    if guess_number == random_number:
        print("Congrates! You won!!")
        break

    elif guess_number > random_number:
        print("You are above the number!")

    else:
        print("You are belowe the number!")

print("You got it in " + str(guess_chance) + " guesses!")
