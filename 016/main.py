#######################################
# CLASS PROJECT
# Coffee Machine - OOP
#######################################

# Day 16 - ☕ The Coffee Machine - #OOP ☕ #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp #ObjectOrientedProgramming

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from lib import logo, clear
from time import sleep

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:

    clear()
    logo()
    user_input = input(
        f"{menu.get_prices()}\nWhat drink do you like? ({menu.get_items()}): "
    ).lower()

    if user_input == "off":
        is_on = False
        clear()
        break
    elif user_input == "report":
        print("\n=== REPORT ===")
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)

    sleep(3)
