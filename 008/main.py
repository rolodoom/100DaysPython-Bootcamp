#######################################
# CLASS PROJECT
# Caesar Cipher
#######################################

# Day 8 - 🔄 Caesar Cipher 🔄 #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

from cypher_data import *


def caesar(start_text, shift_amount, cipher_direction):
    result_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char) + shift_amount
            result_text += alphabet[position]
        else:
            result_text += char

    print(f"Here's the {cipher_direction}d text: {result_text}\n")


end_program = False

while not end_program:

    print(logo)

    option = input(
        "What do you want to do? \n 1. Encrypt? \n 2. Decrypt?\n 3. Exit\nPick an option: "
    ).lower()
    if option == "1":
        direction = "encode"
    elif option == "2":
        direction = "decode"
    else:
        end_program = True

    if not end_program:
        text = input("\nType the message?\n - ")
        shift = int(input("Shift number?\n - "))
        shift = shift % 26

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        continue_program = input("Do you want to continue? [Y/n] ").lower()
        if continue_program == "n":
            end_program = True

print("\nBye!!!")
