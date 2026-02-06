from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100.")
import random
value = random.randint(1,100)
print(f"The values is {value}")

attempts = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def easy():    
    global attempts
    attempts = 10
    i = 0
    while i < attempts:
        guess = int(input("Make a guess: "))
        if guess > value:
            print("Too high")
            print("Guess again")
            attempts-=1
            print(f"You have {attempts} remaining to guess the number.")
        elif guess < value:
            print("Too low")
            print("Guess again")
            attempts-=1
            print(f"You have {attempts} remaining to guess the number.")
        elif guess == value:
            print(f"You got it! The answer was {value}")
            break
        elif attempts == 0:
            print("You've run out of guesses, you lose.")
            break


def hard():
    global attempts
    attempts = 5
    i = 0
    while i < attempts:
        guess = int(input("Make a guess: "))
        if guess > value:
            print("Too high")
            print("Guess again")
            attempts-=1
            print(f"You have {attempts} remaining to guess the number.")
        elif guess < value:
            print("Too low")
            print("Guess again")
            attempts-=1
            print(f"You have {attempts} remaining to guess the number.")
        elif guess == value:
            print(f"You got it! The answer was {value}")
            break
        elif attempts == 0:
            print("You've run out of guesses, you lose.")
            break

if difficulty.lower() == 'easy':
    print("You have 10 attempts remaining to guess the number.")
    easy()
elif difficulty.lower() == 'hard':
    print("You have 5 attempts remaining to guess the number.")
    hard()

    



