from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


turn_off = False
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_menu = Menu()

while not turn_off:
    options = coffee_menu.get_items()
    choice = input(f"   What would you like? ({options}): ").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        turn_off = True
    else:
        drink = coffee_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
