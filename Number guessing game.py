import random

end_of_game = False
print("Welcome to the Number Guessing Game!\nI,m thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} attempts to guess the number.")
else:
    attempts = 5
    print(f"You have {attempts} attempts to guess the number.")
number = random.randint(1, 101)

while not end_of_game:
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high")
        attempts -= 1
        print(f"Guess again\nYou have {attempts} attempts remaining to guess the number.")
    elif guess == number:
        print(f"You got it!.The answer was {number}")
        end_of_game = True
    else:
        print("Too low")
        attempts -= 1
        print(f"Guess again\nYou have {attempts} attempts remaining to guess the number.")
    if attempts == 0:
        print("You've run out of guesses, you lose")
        end_of_game = True
