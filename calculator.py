# Calculator
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
def calc():
    operations = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}
    print("The available operations are: ")
    for key in operations:
        print(key)
    type_of_operation = input("Please enter the operator: ")
    num2 = int(input("What's your second number?: "))
    final_value = 0
    if type_of_operation == "+":
        if not end_of_calc:
            return add(num1, num2)
    elif type_of_operation == "-":
        if not end_of_calc:
            return subtract(num1, num2)
    elif type_of_operation == "*":
        if not end_of_calc:
            return multiply(num1, num2)
    else:
        if not end_of_calc:
            return divide(num1, num2)

end_of_calc = False
print("Welcome to Python Calculator. Let's do some math!")
num1 = int(input("What's your first number?: "))
out = calc()
print(f"The current value is {out}")
stop_flag = False
while not stop_flag:
    cont = input("Do you want to continue or end the calculation here. Type 'yes' or 'no'.")
    if cont == "yes":
        num1 = out
        newout = calc()
        print(f"The value is {newout}")
        out = newout
    else:
        stop_flag = True
        end_of_calc = True
        print(f"The final value is {out}")
        print("Thank you for using the Python calculator.")
        exit()
