# Number Guessing Game
# User gets 7 chances to correctly guess a number between '0' and '9'

import random

while True:
    welcome = input(f"\nWelcome to the number guessing game.\nType 'yes' and press 'Enter' key to play or press 'Enter' key to exit. : ").upper()  

    if welcome == 'YES':
        random_num = random.randint(0,9)
        count = 0
        while count < 7:
            try:
                user_num = int(input("\nPlease guess a number between '0' and '9' : "))
                if user_num in range(10):         
                    if random_num == user_num:
                        print(f"\nYou Win. You guessed the correct no '{user_num}'")
                        break
                    else:
                        print(f"\n'{user_num}': You guessed the wrong number")
                        count += 1
                        chances = (7 - count)
                        print(f"You have {chances} chances left")
                    if chances == 0:
                        print("\nYou Lost!! You have exhausted all your chances")
                else:
                    print("Only numbers between '0' and '9' are allowed")
            except ValueError:
                print("Incorrect value entered. Try again.")
    else:
        if welcome != 'YES':
            print("You chose to exit the game")
            break