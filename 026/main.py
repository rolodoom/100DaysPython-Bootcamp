#######################################
# CLASS PROJECT
# NATO Alphabet
#######################################

# Day 26 - NATO Alphabet #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

import pandas
from lib import logo, clear

# Display Logo
clear()
logo()

# Initialize variables
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for index, row in data.iterrows()}
end_program = False

# Program loop
while not end_program:
    word = input("Enter a word: ").upper()
    output = [phonetic_dict[letter] for letter in word]
    print(f"---> NATO: {output}")

    if input("\nDo you want to enter another word? type 'Y' or 'N': ").lower() == "n":
        end_program = True
    else:
        clear()
        logo()

clear()
