# This is a Bill tip calculator Python script.
print("Welcome to the tip calculator.\n")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15?")
percentage = int(tip) / 100
actual_percentage = 1 + percentage
split = input("How many people to split the bill? ")
each_person_split = float(total_bill) / float(split) * actual_percentage
print(f"Each person should pay: ${each_person_split}")
