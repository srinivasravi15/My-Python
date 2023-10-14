# Coffee Machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
quarters = 0.25
dimes = 0.10
nickels = 0.05
pennies = 0.01
water_left = 0
milk_left = 0
coffee_left = 0
while is_on:
    choice = input("What would you like to have? (Espresso|Latte|Cappuccino): ").lower()
    if choice == "off":
        print("Turning the coffee machine off.")
        is_on = False
    elif choice == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]} ml")
    elif choice == "espresso":
        print(f"The cost of Espresso is ${MENU['espresso']['cost']}")
        cost = MENU['espresso']['cost']
        if MENU['espresso']['ingredients']['water'] < resources['water'] and MENU['espresso']['ingredients']['coffee'] < resources['coffee']:
            print("Please insert coins.")
            q = int(input("How many quarters? "))
            d = int(input("How many dimes? "))
            n = int(input("How many nickels? "))
            p = int(input("How many pennies? "))
            money_inserted = (q * quarters) + (d * dimes) + (n * nickels) + (p * pennies)
            if money_inserted < cost:
                print("Sorry, that's not enough money. Money refunded.")
            elif money_inserted > cost:
                change = money_inserted - cost
                print("Here's your Espresso.")
                resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
                print(f"Here is ${round(change, 2)} in change.")
            else:
                print("Here's your Espresso.")
                resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
        else:
            print("Sorry, there isn't enough resources for an Espresso. Please select a different option.")
    elif choice == "latte":
        print(f"The cost of Latte is ${MENU['latte']['cost']}")
        cost = MENU['latte']['cost']
        if MENU['latte']['ingredients']['water'] < resources['water'] and MENU['latte']['ingredients']['coffee'] < resources['coffee'] and MENU['latte']['ingredients']['milk'] < resources['milk']:
            print("Please insert coins.")
            q = int(input("How many quarters? "))
            d = int(input("How many dimes? "))
            n = int(input("How many nickels? "))
            p = int(input("How many pennies? "))
            money_inserted = (q * quarters) + (d * dimes) + (n * nickels) + (p * pennies)
            if money_inserted < cost:
                print("Sorry, that's not enough money. Money refunded.")
            elif money_inserted > cost:
                change = money_inserted - cost
                print("Here's your Latte.")
                resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
                resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
                print(f"Here is ${round(change, 2)} in change.")
            else:
                print("Here's your Latte.")
                resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
                resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
        else:
            print("Sorry, there isn't enough resources for a Latte. Please select a different option.")
    elif choice == "cappuccino":
        print(f"The cost of Latte is ${MENU['cappuccino']['cost']}")
        cost = MENU['cappuccino']['cost']
        if MENU['cappuccino']['ingredients']['water'] < resources['water'] and MENU['cappuccino']['ingredients']['coffee'] < resources['coffee'] and MENU['cappuccino']['ingredients']['milk'] < resources['milk']:
            print("Please insert coins.")
            q = int(input("How many quarters? "))
            d = int(input("How many dimes? "))
            n = int(input("How many nickels? "))
            p = int(input("How many pennies? "))
            money_inserted = (q * quarters) + (d * dimes) + (n * nickels) + (p * pennies)
            if money_inserted < cost:
                print("Sorry, that's not enough money. Money refunded.")
            elif money_inserted > cost:
                change = money_inserted - cost
                print("Here's your Cappuccino.")
                resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
                resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
                print(f"Here is ${round(change, 2)} in change.")
            else:
                print("Here's your Cappuccino.")
                resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
                resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
        else:
            print("Sorry, there isn't enough resources for a Cappuccino. Please select a different option.")

    else:
        print("Enter a valid option.")
