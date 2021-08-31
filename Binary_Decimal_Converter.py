
#Binary to Decimal and Back Converter - Develop a converter to convert a
#decimal number to binary or a binary number to its decimal equivalent.
choice = int(input("Press 1 for Binary to Decimal conversion\nPress 2 for Decimal to Binary conversion\n\nEnter your choice : "))


if choice == 1:
    binary = input("Enter a binary number : ")
    count = 0
    product = 0

    bin_list = []

    for i in binary:
        bin_list.append(int(i))

    bin_list.reverse()

    for i in range(len(binary)):
        if bin_list[count] == 1:
            product += 2 ** count
            count += 1
        else:
            count += 1

    print(f'\nDecimal number = {product}\n\n')
else:
    decimal = int(input("Enter a decimal number : "))

    decimal = bin(decimal)

    print(f'\nBinary number = {decimal}\n\n')