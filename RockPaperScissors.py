# Rock, Paper & Scissors
import random
options = ["Rock","Paper","Scissors"]
options_len = len(options)
computer_choice = random.randint(0, options_len - 1)
computer = options[computer_choice]
choice = int(input("Type 0 for Rock, 1 for Paper and 2 for Scissors "))
if choice == 0:
    print("You chose Rock.")
    print(f"Computer chose {computer}")
    if computer == "Rock":
        print("Draw")
    elif computer == "Paper":
        print("You lose")
    else:
        print("You win")

elif choice == 1:
    print("You chose Paper.")
    print(f"Computer chose {computer}")
    if computer == "Paper":
        print("Draw")
    elif computer == "Rock":
        print("You win")
    else:
        print("You lose")
else:
    print("You chose Scissors")
    print(f"Computer chose {computer}")
    if computer == "Scissors":
        print("Draw")
    elif computer == "Paper":
        print("You win")
    else:
        print("You lose")
