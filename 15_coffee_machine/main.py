from data import MENU


def check_resources(order_ingredients):
    """The function checks if there are enough resources in the coffee machine
    for making a certain drink and return 1 (True) or 0 (False)"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is no enough {item}.")
            return 0
    return 1


def process_coins():
    """The function process the inserted coins and returns the total."""
    print("Please, insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def check_drink_price(user_choice, data):
    """The function returns the cost of selected drink"""
    if user_choice == "espresso":
        return data["espresso"]["cost"]
    elif user_choice == "latte":
        return data["latte"]["cost"]
    else:
        return data["cappuccino"]["cost"]


def check_transaction(user_coins, drink_cost):
    """The function checks if there are enough money for making a drink and return 1 (True) or 0 (False)"""
    if user_coins >= drink_cost:
        change = round(user_coins - drink_price, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return 1
        # return machine_money
    # if user_coins > drink_cost:
    #     change = round(user_coins - drink_price)
    #     machine_money += drink_cost
    #     return machine_money
    #     #print(f"Here is ${change} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


# def check_change(user_coins, drink_price):
#     """The function counts and prints the amount of change"""
#     if user_coins > drink_price:
#         change = round(user_coins - drink_price)
#         print(f"Here is ${change} in change.")


def change_machine_resources(selected_drink, machine_resources, data):
    """The function updates the resources of machine after making a drink"""
    for item in data:
        machine_resources[item] -= data[item]
    print(f"Here is your {selected_drink}. Enjoy!")


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

    choice = input("   What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    elif choice == "off":
        turn_off = True
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]) == 1:
            user_payment = process_coins()
            drink_price = check_drink_price(choice, MENU)
            if check_transaction(user_payment, drink_price) > 0:
                #check_change(user_payment, drink_price)
                #money += check_transaction(user_payment, drink_price, money)
                change_machine_resources(choice, resources, drink["ingredients"])