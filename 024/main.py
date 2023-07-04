#######################################
# CLASS PROJECT
# Mail Merge Challenge
#######################################

# Day 24 - Mail Merge Challenge  #100DaysOfCode #100DaysOfCodePython #Python #Bootcamp

PLACEHOLDER = "[name]"

# 1. Create a letter using starting_letter.txt for each name in invited_names.txt
# 1.1 Read the starting letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    starting_letter = letter_file.read()

# 1.2 Read the invited names
with open("./Input/Names/invited_names.txt") as names_file:
    # names = file.read()
    names = names_file.readlines()

for name in names:
    stripped_name = name.strip()
    # 2. Replaces the [name] placeholder with the actual name.
    new_letter = starting_letter.replace(PLACEHOLDER, stripped_name)
    # 3. Save the letters in the dolder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
        file.write(new_letter)
