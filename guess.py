# Guess
import random
def num_check(g,num):
    if g > num:
        print("Too High.")
    else:
        print("Too Low.")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number = random.randint(1,100)
if level == "easy":
    print("You have 10 attempts.")
    attempts = 10
    for i in range(1,11):
        guess = int(input("Enter your guess in the range 1 - 100: "))
        if guess not in range(1,101):
            print("Guess the number in the range 1 - 100!")
            exit()
        if guess != number:
            num_check(guess,number)
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left")
            if attempts == 0:
                print(f"You lost as you've ran out of guesses. The number is {number}")
                exit()
        else:
            print(f"You guessed it right. The number is {guess}")
elif level == "hard":
    print("You have 5 attempts.")
    attempts = 5
    for i in range(1,6):
        guess = int(input("Enter your guess in the range 1 - 100: "))
        if guess != number:
            num_check(guess, number)
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left")
            if attempts == 0:
                print(f"You lost as you've ran out of guesses. The number is {number}")
                exit()
        else:
            print(f"You guessed it right. The number is {guess}")
else:
    print("The difficulty can only be 'easy' or 'hard'.")
    exit()
