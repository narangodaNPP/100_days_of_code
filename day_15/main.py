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

profit = 0
is_on = True


def check_resource(drink): ...
def get_coins(): ...


# TODO 1 : ask espresso/latter/cappuccino
while is_on:
    ans = input("What would you like? (espresso/latte/cappuccino):")
# TODO 2 : turn off machine
    if ans.lower() == "off":
        is_on = False
# TODO 3 : print report
    elif ans.lower() == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    check_resource(ans)
    get_coins()


# TODO 4 : check resources sufficient
def check_resource(drink):
    if resources['water'] < MENU[drink]['ingredients']['water']:
        print("Sorry there is not enough water.")
    if resources['milk'] < MENU[drink]['ingredients']['milk']:
        print("Sorry there is not enough milk.")
    if resources['water'] < MENU[drink]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")


# TODO 5 : process coins
def get_coins():
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))

# TODO 6 : check transaction successful

# TODO 7 : make coffee



