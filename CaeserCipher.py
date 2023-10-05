def caeser_cipher(word, shift, encryption):
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    index = len(alphabets) - 1
    new_word = ""
    if encryption == "encode":
        for letter in word:
            position = alphabets.index(letter)
            position += shift
            if position > index:
                new_letter = alphabets[position - index - 1]
                new_word += new_letter
            else:
                new_letter = alphabets[position]
                new_word += new_letter
        print(f"The encoded word is: {new_word}")
    elif encryption == "decode":
        for letter in word:
            position = alphabets.index(letter)
            position -= shift
            new_letter = alphabets[position]
            new_word += new_letter
        print(f"The encoded word is: {new_word}")
    else:
        print("Please enter a valid encryption.")
        exit()

user_word = input("Enter a single word without any spaces: ").lower()
if " " in user_word:
    print("Please enter a word without any spaces.")
    exit()
enc = input("Enter the encryption mechanism. Enter 'encode' or 'decode': ").lower()
user_shift = int(input("Shift: "))
caeser_cipher(word=user_word,shift=user_shift,encryption=enc)
