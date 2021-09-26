from menu import resources
from menu import MENU

print(MENU["latte"]["ingredients"]["water"])
print("Enter 'report' to get details about resources.\nPress 'off' to turn off the machine.")

choice = input("\nWhat would you like? (espresso/latte/cappuccino) : ")

money = 0


def deduct_resources(coffee_name):
    count = 0
    for r in resources:
        if r in MENU[coffee_name]["ingredients"]:
            for y in MENU[coffee_name]["ingredients"].keys():
                if r == y:
                    resources[y] -= MENU[coffee_name]["ingredients"][y]
                    count += 1
                    if coffee_name == 'espresso' and count == 2:
                        return
                    elif count == 3:
                        return


def process_coins(coffee_name):
    print("Enter coins : ")
    quarters = int(input("\nEnter number of quarters : ")) * .25
    dimes = int(input("Enter number of dimes : ")) * .10
    nickles = int(input("Enter number of nickles : ")) * .05
    pennies = int(input("Enter number of pennies : ")) * .01
    total_amount = quarters + dimes + nickles + pennies
    menu_cost = MENU[coffee_name]["cost"]

    if total_amount > menu_cost:
        change = total_amount - menu_cost
        print(f"\nYour change : ${round(change, 2)}")
        return True
    elif total_amount < menu_cost:
        print(f"\nInsufficient funds.")
        return False
    else:
        return True


def check_resources(coffee_name):
    check = True
    for r in resources:
        if r in MENU[coffee_name]["ingredients"]:
            for y in MENU[coffee_name]["ingredients"].keys():
                if resources[y] >= MENU[coffee_name]["ingredients"][y]:
                    check = True
                else:
                    check = False
                    break
    if check:
        funds = process_coins(coffee_name)
        if funds:
            print(f"\nHere is your {coffee_name}. Enjoy!")
            deduct_resources(coffee_name)
    else:
        print(f"\nInsufficient resources available to make {coffee_name}.")


while choice != 'off':
    if choice == 'report':
        print("Resources : ")
        for res in resources:
            print(res, " : ", resources[res])
    elif choice == 'espresso':
        check_resources('espresso')
    elif choice == 'latte':
        check_resources('latte')
    elif choice == 'cappuccino':
        check_resources('cappuccino')

    choice = input("\nWhat would you like? (espresso/latte/cappuccino) : ")

print("\n\nMachine has been turned off.")
