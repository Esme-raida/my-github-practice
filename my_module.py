import random
import art12
print(art12.logo)

# Step 1: Welcome Message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100 ")

# Step 2: Global Variables
attempts = 0
game_on = True

# Step 3: Function to Set Difficulty
def set_difficulty(difficulty):
    global attempts
    if difficulty == 'hard':
        attempts = 5
    elif difficulty == 'easy':
        attempts = 10
    else:
        print("Enter a valid difficulty level")
        return set_difficulty(input("Choose a difficulty. Type 'easy' or 'hard': "))
    return attempts

# Step 4: Get Difficulty Input
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = set_difficulty(difficulty)

# Step 5: Generate Random Number
guess = random.randint(1, 100)

# Step 6: Function to Check the Guess
def check_guess():
    global attempts, game_on, guess  
    while game_on:
        try:
            user_guess = int(input("Make a guess: "))

            if user_guess > guess:
                print("Too high.")
            elif user_guess < guess:
                print("Too low.")
            else:
                print("Correct!")
                question = input("Do you want to play again? Type 'y' or 'n': ")
                if question == 'y':
                    attempts = set_difficulty(difficulty)  
                    guess = random.randint(1, 100)  
                    print(f"You have {attempts} attempts remaining.")
                    continue  
                else:
                    game_on = False
                    break

            attempts -= 1
            if attempts == 0:
                print(f"You ran out of attempts! The number was {guess}")
                game_on = False
                break
            else:
                print(f"You have {attempts} attempts remaining.")

        except ValueError:
            print("Invalid input! Please enter a number.")

# Step 7: Start the Game
check_guess()