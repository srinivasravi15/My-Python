# Treasure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at crossroads. Type 'left' or 'right'? ").lower()
if choice1 == "left":
    choice2 = input("You see an island far away. Type 'swim' or 'wait' ").lower()
    if choice2 == "wait":
        choice3 = input("Which door? 'red', 'blue' or 'yellow'? ").lower()
        if choice3 == "red":
            print("Game Over!")
        elif choice3 == "blue":
            print("Game Over!")
        elif choice3 == "yellow":
            print("You win.")
        else:
            print("You've entered a wrong door. Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")
