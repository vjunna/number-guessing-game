# Number Guessing Game
# User gets 7 chances to correctly guess a number between '0' and '9'

import random

while True:
    welcome = input("Welcome to the number guessing game. Please type 'yes' to start or press any key to exit. : ").upper()  

    if welcome == 'YES':
        random_num = random.randint(0,9)
        count = 0
        while count < 7:
            try:
                user_num = int(input("Please guess a number between '0' and '9' : "))
                if user_num in range(10):         
                    if random_num == user_num:
                        print(f"You Win. You guessed the correct no '{user_num}'")
                        break
                    else:
                        print(f"'{user_num}': You guessed the wrong number")
                        count += 1
                        print(f"You have {7 - count} chances left")
                    if 7 - count == 0:
                        print("You Lost!! You have exhausted all your chances")
                else:
                    print("Only numbers between '0' and '9' are allowed")
            except ValueError:
                print("Incorrect value entered. Try again.")
    else:
        print("You chose to exit the game")
        break