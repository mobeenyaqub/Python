money = 0.0
milk = 300
coffee = 70
water = 500


def display_report():
    print(f"\n\nWater: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}\n\n")


def deduct_resources(mi, c, w, mo):
    global milk, coffee, water, money
    milk -= mi
    coffee -= c
    water -= w
    money += mo


def process_coins(cfe, payment):
    quarters = int(input("Enter quarters: ")) * 0.25
    dimes = int(input("Enter dimes: ")) * 0.10
    nickles = int(input("Enter nickles: ")) * 0.05
    pennies = int(input("Enter pennies: ")) * 0.01
    total = quarters + dimes + nickles + pennies

    if cfe == "e":
        cafe = "Espresso"
    elif cfe == "l":
        cafe = "Latte"
    else:
        cafe = "Cappuccino"

    if total == payment:
        print(f"Here is your Espresso. Enjoy!")
        print("\nBefore Report: ")
        display_report()
        return True
    elif total > payment:
        print(f"Here is your {cafe}. Enjoy!\n\n Change: ${round(total - payment, 2)}")
        print("\nBefore Report: ")
        display_report()
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def check_resources(coffeeChoice):
    if coffeeChoice == "e":
        if water >= 50 and coffee >= 18:
            check = process_coins(coffeeChoice, 1.5)
            if check:
                print("\nAfter Report: ")
                deduct_resources(0, 18, 50, 1.5)
                display_report()
        else:
            print("Sorry there are not enough resources.")
    elif coffeeChoice == "l":
        if water >= 200 and coffee >= 24 and milk >= 150:
            check = process_coins(coffeeChoice, 2.5)
            if check:
                print("\nAfter Report: ")
                deduct_resources(150, 24, 200, 2.5)
                display_report()
        else:
            print("Sorry there are not enough resources.")
    elif coffeeChoice == "c":
        if water >= 250 and coffee >= 24 and milk >= 100:
            check = process_coins(coffeeChoice, 3)
            if check:
                print("\nAfter Report: ")
                deduct_resources(100, 24, 250, 3)
                display_report()
        else:
            print("Sorry there are not enough resources.")


def take_input():
    coffee_choice = input("What would you like? (espresso(e)/latte(l)/cappuccino(c)):").lower()

    if coffee_choice in ["e", "l", "c"]:
        check_resources(coffee_choice)
    elif coffee_choice == "off":
        print("Machine turned off!")
        return False
    elif coffee_choice == "report":
        display_report()
    else:
        print("Invalid choice! Try again.")

    return True


while take_input():
    take_input()