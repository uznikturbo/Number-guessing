import os
import random

while True:
    random_num = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("Please select the difficulty level")
    print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        max_attempts = 10
        name = "Easy"
    elif choice == 2:
        max_attempts = 5
        name = "Medium"
    elif choice == 3:
        max_attempts = 3
        name = "Hard"
    else:
        os.system("cls")
        print("Invalid choice")
        continue

    print(f"Great! You have selected the {name} difficulty level.")
    attempts = 0

    while attempts <= max_attempts:
        player_num = int(input("Enter your guess: "))
        if player_num == random_num:
            os.system("cls")
            print(f"Congrats! You guessed the correct number in {attempts} attempts.")
            break
        elif player_num < random_num:
            print(f"Incorrect! The number is greater than {player_num}\n\n")
            attempts += 1
        elif player_num > random_num:
            print(f"Incorrect! The number is less than {player_num}\n\n")
            attempts += 1
    else:
        os.system("cls")
        print("Attempts are over!")
