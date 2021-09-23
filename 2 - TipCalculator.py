print("Welcome to tip calculator.")
total_bill = float(input("What was the total bill? "))

tip_pctg = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))

per_person = round((total_bill * (tip_pctg/100 + 1)) / people,2)

print(f"Each person should pay : ${per_person}")