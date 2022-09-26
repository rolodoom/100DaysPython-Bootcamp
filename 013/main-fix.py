#######################################
# CLASS PROJECT
# Debugging
#######################################

# Day 13 - Debugging #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp


# DETECT ODD EVEN NUMBER
# BUG: Can't run the code
# FIX: Conditional must use == instead of =
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")


# LEAP YEAR
# BUG: TypeError: not all arguments converted during string formatting
# FIX: Convert input to int
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


# Fizz Buzz game
# BUG:
# - Brackets around number.
# - FizzBuzz is being printed on 3 and 5.
# - Numbers are being duplicated
# FIX: Must change 'or' with 'and'
# - Remove brackets
# - Replace 'or' with 'and'
# - change intermediate 'if' with 'elif'
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
