# Hangman Project
import random
word_list = ["roman","seth","dean"]
chosen_word = random.choice(word_list)
print("\nWelcome to HANGMAN game!\n\nLet's begin.\n")
print("You have 5 lives to win this game.\n")
stages = ["|||||","||||","|||","||","|"]
display = []
for letter in chosen_word:
    display += "_"
print(f"Your letter for the day is: {display}")
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        stages.pop(0)
        if len(stages) != 0:
            print("You lost a life! Be careful with your guess next time.")
            print(stages)
        else:
            end_of_game = True
            print("You lost all lives. Game Over!!")
    if "_" not in display:
        end_of_game = True
        print("Yay, you win!")
