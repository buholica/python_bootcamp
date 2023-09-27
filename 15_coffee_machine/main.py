from data import MENU


def check_resources(machine_resources, data, selected_drink):
    """The function checks if there are enough resources in the coffee machine
    for making a certain drink and return 1 or 0"""
    drink = data[selected_drink]
    if selected_drink == "espresso":
        if (drink["ingredients"]["water"] <= machine_resources["water"] and
                drink["ingredients"]["coffee"] <= machine_resources["coffee"]):
            return 1
        elif drink["ingredients"]["water"] >= machine_resources["water"]:
            print("Sorry, there is no enough water.")
            return 0
        else:
            print("Sorry, there is no enough coffee.")
            return 0
    else:
        if (drink["ingredients"]["water"] <= machine_resources["water"] and
                drink["ingredients"]["milk"] <= machine_resources["milk"] and
                drink["ingredients"]["coffee"] <= machine_resources["coffee"]):
            return 1
        elif drink["ingredients"]["water"] >= machine_resources["water"]:
            print("Sorry, there is no enough water.")
            return 0
        elif drink["ingredients"]["milk"] >= machine_resources["milk"]:
            print("Sorry, there is no enough milk.")
            return 0
        else:
            print("Sorry, there is no enough coffee.")
            return 0


def check_drink_price(user_choice, data):
    """The function returns the cost of selected drink"""
    if user_choice == "espresso":
        return data["espresso"]["cost"]
    elif user_choice == "latte":
        return data["latte"]["cost"]
    else:
        return data["cappuccino"]["cost"]


def check_transaction(user_coins, drink_price, machine_money):
    """The function checks if there are enough money for making a drink"""
    if user_coins == drink_price:
        machine_money += user_coins
        return machine_money
    if user_coins > drink_price:
        #change = round(user_coins - drink_price)
        machine_money += drink_price
        return machine_money
        #print(f"Here is ${change} in change.")
    else:
        return 0


def check_change(user_coins, drink_price):
    """The function counts and prints the amount of change"""
    if user_coins > drink_price:
        change = round(user_coins - drink_price)
        print(f"Here is ${change} in change.")


def change_machine_resources(machine_resources, selected_drink, data):
    """The function updates the resources of machine after making a drink"""
    drink = data[selected_drink]
    if selected_drink == "espresso":
        machine_resources["water"] -= drink["ingredients"]["water"]
        machine_resources["coffee"] -= drink["ingredients"]["coffee"]
        return machine_resources
    else:
        machine_resources["water"] -= drink["ingredients"]["water"]
        machine_resources["milk"] -= drink["ingredients"]["milk"]
        machine_resources["coffee"] -= drink["ingredients"]["coffee"]
        return machine_resources


turn_off = False
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

while not turn_off:
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    prompt = input("   What would you like? (espresso/latte/cappuccino): ").lower()

    if prompt == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    elif prompt == "off":
        turn_off = True
    else:
        if check_resources(resources, MENU, prompt) == 1:
            print("Please, insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            drink_price = check_drink_price(prompt, MENU)
            if check_transaction(total, drink_price, money) > 0:
                check_change(total, drink_price)
                money += check_transaction(total, drink_price, money)
                change_machine_resources(resources, prompt, MENU)
                print(f"Here is your {prompt}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")