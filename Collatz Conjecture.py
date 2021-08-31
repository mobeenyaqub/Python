number = 0
step_count = 0

while number <= 1:
    number = int(input("Enter a number > 1\n\nEnter your number : "))

actual_number = number

while number != 1:
    if number % 2 == 0:
        number = number / 2
        step_count +=1
    else:
        number = (number*3) + 1
        step_count +=1


print(f"\nIt took {actual_number} -> {step_count} steps to reach 1\n\n")