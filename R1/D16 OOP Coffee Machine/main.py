from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

power_on = True
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while power_on:
    user_input = input(f"What would you like? ({menu.get_items()})")
    if user_input == "off":
        print("Powering down.  Goodbye.")
        power_on = False
    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if drink is not None:
            if coffee_machine.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)

