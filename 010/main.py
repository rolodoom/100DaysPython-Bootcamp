#######################################
# CLASS PROJECT
# Calculator
#######################################

# Day 10 - 🔢 Calculator 🔢 #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

from art import *


def substraction(a, b):
    return a - b


def addition(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


operations = {
    "-": substraction,
    "+": addition,
    "*": multiplication,
    "/": division,
}

exit_program = False


def calculator():
    global exit_program

    if exit_program:
        return False

    print(logo)

    last_answer = float(input("Enter a number: "))
    ask_operation_string = ""
    for symbol in operations:
        ask_operation_string += "'" + symbol + "' "

    exit_calculator = False

    while not exit_calculator:

        operation_symbol = input(f"{ask_operation_string} Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        operation_function = operations[operation_symbol]
        current_answer = operation_function(last_answer, next_number)
        print(f"{last_answer} {operation_symbol} {next_number} = {current_answer}")

        menu_option = input(
            f"Type 'y' to continue with {current_answer}, 'n' to start new calculation, or 'q' to exit the program: "
        ).lower()

        if menu_option == "y":
            last_answer = current_answer
        elif menu_option == "n":
            exit_calculator = True
            calculator()
        else:
            exit_calculator = True
            exit_program = True


calculator()

print("\nBye! :)")
