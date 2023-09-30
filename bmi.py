#BMI calculator
height = float(input("What is your height in metres? "))
weight = int(input("What is your weight in kg? "))
bmi = weight / height ** 2
rounded_bmi = round(bmi,2)
print(f"Your BMI is: {rounded_bmi}")
if rounded_bmi < 18.5:
    print("You're underweight.")
elif rounded_bmi < 25:
    print("You're normal weight.")
elif rounded_bmi < 30:
    print("You're slightly overweight.")
elif rounded_bmi < 35:
    print("You're obese.")
else:
    print("You're clinically obese")
