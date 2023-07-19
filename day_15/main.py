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
profit = 0


def is_resources_enough(drink):
    """Return True when order can be supplied, False when resources are insufficient"""
    for item in drink:
        if drink[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def get_coins():
    """Returns total calculated from inserted coins"""
    print("Please insert coins")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickles = int(input("Nickles: "))
    pennies = int(input("Pennies: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def is_transaction_successful(payment_recv, drink_cost):
    """Return True when received payment is enough, False if it insufficient"""
    global profit
    if payment_recv >= drink_cost:
        change = round(payment_recv - drink_cost, 2)
        print(f"Here is ${change} change!")
        profit += drink_cost
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


def make_drink(drink):
    """Return updated resources after drink is made"""
    for item in drink:
        resources[item] -= drink[item]
    return resources


if __name__ == '__main__':
    while is_on:
        answer = input("What would you like? (espresso/latte/cappuccino): ")
        if answer.lower() == 'off':
            is_on = False
            break
        elif answer.lower() == 'report':
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}ml")
            print(f"Money: ${profit}")
        else:
            if is_resources_enough(MENU[answer]['ingredients']):
                payment = get_coins()
                if is_transaction_successful(payment, MENU[answer]['cost']):
                    resources = make_drink(MENU[answer]['ingredients'])
                    print(f"Here is your {answer} ☕")



