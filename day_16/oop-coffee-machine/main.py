from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

while is_on:
    answer = input(f"What would you like? ({menu.get_items()}): ")
    if answer == "off":
        is_on = False
        break
    elif answer == "report":
        machine.report()
        money.report()
    else:
        if menu.find_drink(answer):
            drink = menu.find_drink(answer)
            print(drink)
        else:
            pass

