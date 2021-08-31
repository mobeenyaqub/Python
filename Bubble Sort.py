array = []
temp = 0
values = 0

while values != 'X' or values != 'x':
    values = input("Enter a positive number or press X or x to exit any time\n\nEnter a number : ")

    if values.isdigit():
        array.append(int(values))
    else:
        break

if len(array) > 0:
    print(f"\n\nUnsorted list {array}\n\n")

    for i in range(len(array)):
        for x in range(len(array) - 1):
            if array[x] > array[x + 1]:
                temp = array[x]
                array[x] = array[x + 1]
                array[x + 1] = temp


    print(f"\nSorted list {array}\n\n\n")
