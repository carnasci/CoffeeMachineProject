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

on = True
current_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

user_coins = {}

def generate_report(machine_resources):
    """Takes current resources in machine and formats it to generate a report."""
    for key, value in machine_resources.items():
        if key == "water" or key == "milk":
            print(f"{key.title()}: {value}ml")
        elif key == "coffee":
            print(f"{key.title()}: {value}g")
        else:
            print(f"{key.title()}: ${value}")

def check_if_resources_sufficient(drink, machine_resources):
    """Takes required resources and current resources and checks if drink is able to be made."""
    for key, value in drink.items():
        for k, v in machine_resources.items():
            if key == k and v > value:
                return True
            elif key == k and v < value:
                print(f"Sorry, not enough {key}.")
                return False

def tally_coins(coins):
    """Takes a dictionary of coins and returns the total monetary value."""
    total = 0
    total += coins["quarters"] * .25
    total += coins["dimes"] * .1
    total += coins["nickels"] * .05
    total += coins["pennies"] * .01
    return total

def check_price(inserted_money, drink_cost):
    if inserted_money < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = inserted_money - drink_cost
        print(f"Here is ${round(change, 2)} in change.")
        return True


# TODO#1 prompt user by asking "What would you like (espresso/latte/cappuccino)?"
# TODO#2 turn the machine off when given the prompt "off"
# TODO#3 generates a report of current resources when given the prompt "report"
# TODO#4 check if resources are sufficient
# TODO#5 if there is enough resources to make a drink ask the user for coins

while on:
    user_choice = input("What would you like (espresso/latte/cappuccino)? ").lower()

    if user_choice == "off":
        on = False
    elif user_choice == "report":
        generate_report(current_resources)
    elif user_choice in MENU:
        user_choice = MENU[user_choice]
        print(user_choice)

    if check_if_resources_sufficient(user_choice["ingredients"], current_resources):
        print("Please insert coins.")
        print(f"drink costs {user_choice["cost"]}")
        user_coins["quarters"] = int(input("how many quarters?: "))
        user_coins["dimes"] = int(input("how many dimes?: "))
        user_coins["nickels"] = int(input("how many nickels?: "))
        user_coins["pennies"] = int(input("how many pennies?: "))

    user_money = tally_coins(user_coins)
    if check_price(user_money, user_choice["cost"]):
        current_resources["money"] += user_choice["cost"]
    print(current_resources)
