# 1. Makes 3 hot flavours
#   - Expresso
#       - $1.50
#       - 50ml water, 18g coffee
#   - Latte
#       - $2.50
#       - 200ml water, 24g coffee, 150ml milk
#   - Capuccino
#       - $3.00
#       - 250ml water, 24g coffee, 100ml milk
#
#   - Machine Resources
#       - 300ml water
#       - 200ml mil
#       - 100g coffee
#
# 2. Coin operated
#   - Penny (1 cent) -> $0.01
#   - Nickel (5 cent) -> $0.05
#   - Dime (10 cents) -> $0.10
#   - Quarter (25 cents) -> $0.25

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
    },
}

resources = {
    "water": 1000,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}
