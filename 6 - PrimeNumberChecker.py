def prime_checker(number):
    check = False
    if number in [0, 1, 2, 3]:
        print(f"{number} is prime")
    else:
        for x in range(2, number):
            if number % x == 0:
                check = True
                break
            else:
                check = False
        if not check:
            print(f"{number} is prime")
        else:
            print(f"{number} is not prime")

n = int(input("Check this number: "))
prime_checker(number=n)