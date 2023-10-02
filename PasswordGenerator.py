# PyPassword Generator
import random
lower_case_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper_case_letters = []
for letter in lower_case_letters:
    upper_case_letters += letter.upper()
numbers = ["0","1","2","3","4","5","6","7","8","9"]
special_chars = ["!","@","#","$","%","&","?"]
print("Welcome to PyPassword Generator!")
num_lower_letters = int(input("How many lower case letters would you like in your password?\n"))
num_upper_letters = int(input("How many upper case letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_special_chars = int(input("How many special characters would you like in your password?\n"))
password = ""
for char in range(1, num_lower_letters + 1):
    password += random.choice(lower_case_letters)
for char in range(1, num_upper_letters + 1):
    password += random.choice(upper_case_letters)
for char in range(1, num_numbers + 1):
    password += random.choice(numbers)
for char in range(1, num_special_chars + 1):
    password += random.choice(special_chars)
print(f"Your new password is: {password}")
