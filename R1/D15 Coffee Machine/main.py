# coffee machine

from data import MENU, resources


def print_report():
    print(f"Water: {resources['water']}mL")
    print(f"Milk: {resources['milk']}mL")
    print(f"Coffee: {resources['coffee']}g")
    if 'money' in resources:
        print(f"Money: ${resources['money']:0.2f}")
    else:
        print("Money: $0")


def have_resources(_drink):
    if resources['water'] < _drink['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False
    elif resources['coffee'] < _drink['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    elif 'milk' in _drink['ingredients'] and resources['milk'] < _drink['ingredients']['milk']:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def bank_money(_cost):
    """
    Handle the fact that the source data does not have a 'money' key
    """
    if 'money' in resources:
        resources['money'] += _cost
    else:
        resources['money'] = _cost


def process_coins(_drink):
    print(f"That costs ${_drink['cost']:0.2f}.\nPlease insert coins.")
    quarters = int(input("How many quarters?: ")) * .25
    dimes = int(input("How many dimes?: ")) * .10
    nickels = int(input("How many nickels?: ")) * .05
    pennies = int(input("How many pennies?: ")) * .01
    coins_inserted = quarters + dimes + nickels + pennies

    if coins_inserted < _drink['cost']:
        print("Sorry that's not enough money.  Money refunded.")
        return False
    elif coins_inserted > _drink['cost']:
        change_amount = round(coins_inserted - _drink['cost'], 2)
        print(f"Here is ${change_amount:0.2f} in change.")
        bank_money(_drink['cost'])
        return True
    else:  # exact change, no refund no message
        bank_money(_drink['cost'])
        return True


def make_drink(_drink):
    resources['water'] -= _drink['ingredients']['water']
    resources['coffee'] -= _drink['ingredients']['coffee']
    if 'milk' in _drink['ingredients']:
        resources['milk'] -= _drink['ingredients']['milk']
    print(f"Here is your {_drink['nickname']}.")


def mainloop():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Power Off Sequence initiated.  Goodbye!")
    elif choice == "report":
        print_report()
        mainloop()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        chosen_drink = MENU[choice]
        chosen_drink['nickname'] = choice
        if have_resources(chosen_drink) and process_coins(chosen_drink):
            make_drink(chosen_drink)
        mainloop()  # transaction complete, recycle service loop
    else:  # invalid entry, just ignore and recycle
        mainloop()


mainloop()
