#######################################
# CLASS PROJECT
# The Coffee Machine
#######################################

# Day 15 - ☕ The Coffee Machine ☕  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

from art import *
from data import *
import platform
import os
from time import sleep


def clear():
    system = platform.system().lower()
    if system == "linux" or system == "darwin":
        os.system("clear")
    elif system == "windows":
        os.system("cls")


def print_report():
    """Prints the current value of the resources"""
    print(f"\n=== REPORT ===")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink_ingredients):
    """Returns a boolean indicating whether or not the order can be made"""
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] >= resources[ingredient]:
            print(f"\nSorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Returns the amount of money calculated from the inserted coins."""
    total_value = 0
    for coin in coins:
        if coin != "penny":
            total_value += int(input(f"How many {coin}s?: ")) * coins[coin]
        else:
            total_value += int(input(f"How many pennies?: ")) * coins[coin]
    return total_value


def transaction_ok(drink_cost, cash):
    """Returns a boolean that indicates if the transaction has been valid (the money is enough)"""
    if drink_cost > cash:
        print(f"\nSorry that's not enough money. Money refunded: ${round(cash, 2)}.")
        return False
    else:
        # Add money
        global money
        money += drink_cost

        # Give change if any
        change = round(cash - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        return True


def print_prices():
    """Print a formated string with the prices"""
    output = []
    for drink in MENU:
        output.append(f"{drink.capitalize()}: ${MENU[drink]['cost']}")
    print(" - ".join(output))


def get_menu_options():
    """Returns a formated string with the menu options"""
    output = []
    for drink in MENU:
        output.append(f"{drink}")
    return "/".join(output)


def make_drink(drink_name, drink_ingredients):
    """Takes the resources of the drink and deducts them from the resources of the machine."""
    global resources
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name.capitalize()}. Enjoy!")


money = 0
turn_off = False
while not turn_off:

    clear()
    print(logo)

    print_prices()
    # Prompt user about the drink
    user_input = input(f"What would you like? ({get_menu_options()}): ").lower()

    # Turn off the Coffee Machine by entering “​off​” to the prompt.
    if user_input == "off":
        turn_off = True
        break
    # Print report
    elif user_input == "report":
        print_report()

    # Valid user input
    elif (
        user_input == "espresso" or user_input == "latte" or user_input == "cappuccino"
    ):
        # Check resources sufficient
        # When the user chooses a drink, the program should check
        # if there are enough resources to make that drink.
        drink = MENU[user_input]
        if check_resources(drink["ingredients"]):
            print(
                f"\nYou've selected {user_input.capitalize()}. Cost: ${drink['cost']}"
            )
            # Process coins
            input_money = process_coins()

            # Check transaction successful?
            if transaction_ok(drink_cost=drink["cost"], cash=input_money):
                make_drink(user_input, drink["ingredients"])

    # No valid input
    else:
        print("\nI don't have that drink!")

    sleep(4)
