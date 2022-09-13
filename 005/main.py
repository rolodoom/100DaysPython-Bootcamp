#######################################
# CLASS PROJECT
# Password Generator Project
#######################################

# Day 5 - 🔒 Password Generator 🔒 #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

import random
from password_data import *

print("--------------------------------------")
print("        Password Generator")
print("--------------------------------------\n")


password_list = []
max_q_chars = 64
password = ""

letter_q = int(input("How many letters? "))
number_q = int(input("How many number? "))
symbol_q = int(input("How many symbols? "))
if (letter_q + number_q + symbol_q) > max_q_chars:
    print(f"The max amount of characters is {max_q_chars}")
else:
    for n in range(0, letter_q):
        password_list.append(random.choice(letters))
    for n in range(0, number_q):
        password_list.append(random.choice(numbers))
    for n in range(0, symbol_q):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)
    for char in password_list:
        password += char
    print(f"Your password: {password}")
