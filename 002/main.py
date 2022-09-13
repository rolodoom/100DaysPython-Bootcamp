########################################
# CLASS PROJECT
########################################

# 1. Greeting
print("-----------------------------------")
print("|          TIP CALCULATOR         |")
print("-----------------------------------\n")
# 2. Bill?
bill = float(input("How much is the bill? "))
# 3. Tip?
tip = int(input("Tip percentage? 10, 12 or 15? "))
# 4. How many people to split the bill?
people = int(input("How many people to split? "))
# 5. Process
person_pays = (bill + (bill * tip / 100)) / people
round_amount = "{:.2f}".format(person_pays)
# 6. Show the result
print(f"Each person should pay: ${round_amount}")
