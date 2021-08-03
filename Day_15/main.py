# Contains all the items menu in the coffee machine
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
    }
}

# Contains the amount of resources it has
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Total amount of money it will have at the start
machine_money = 0

machine_off = False

def print_report():
    """
    Generates a report of resources
    """
    for item in resources:
        if(item == "water" or item == "milk"):
            print(f"{item}: {resources[item]}ml")
        else:
            print(f"{item}: {resources[item]}g")
    print(f"Money: ${machine_money}")

def check_resource(required_resources, resources_dict):
    """
    Checks required resources to make coffee against the inventory to see if 
    enough resource are present or not.
    """
    for item in required_resources:
        if required_resources[item] > resources_dict[item]:
            return item
        else:
            continue
    return True

def reduce_resources(resources_used):
    """Reduces the amount of resources used"""
    for item in resources_used:
        resources[item] -= resources_used[item]

def process_transaction(amount_needed):
    """Handles transaction"""
    print("Enter Coins: ")
    quaters = int(input("How many quaters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.1
    nickles = int(input("How many nickles?")) * 0.05
    pennies = int(input("How many pennies?")) * 0.01

    amount_given = round((quaters + dimes + nickles + pennies), 2)
    if amount_given >= amount_needed:
        change = round((amount_given - amount_needed), 2)
        if change != 0:
            print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded \n")
        return False

while not machine_off:
    user_input = input("​What would you like? (espresso/latte/cappuccino): ​").lower()
    if user_input == "off":
        machine_off = True
    elif user_input == "report":
        print_report()
    else:
        for menu_item in MENU:
            if user_input == menu_item:
                items_needed = MENU[user_input]["ingredients"]
                resource_check = check_resource(items_needed, resources)
                if resource_check == True:
                    coffee_price = MENU[user_input]["cost"]
                    transaction_success = process_transaction(coffee_price)
                    if transaction_success:
                        machine_money += coffee_price
                        reduce_resources(items_needed)
                        print(f"Here is your {user_input}. Enjoy! \n")
                        
                    else:
                        continue
                else:
                    print(f"Sorry there is not enough {resource_check} \n")
