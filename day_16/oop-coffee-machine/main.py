from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

while is_on:
    choices = menu.get_items()
    answer = input(f"What would you like? ({choices}): ")
    if answer == "off":
        is_on = False
    elif answer == "report":
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(answer)
        if drink:
            if machine.is_resource_sufficient(drink):
                if money.make_payment(drink.cost):
                    machine.make_coffee(drink)
