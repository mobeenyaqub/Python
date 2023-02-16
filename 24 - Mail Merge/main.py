with open("./Input/Names/invited_names.txt") as names:
    name = names.readlines()

with open("././Input/Letters/starting_letter.txt") as letter:
    data = letter.read()

    for each in name:
        n = each.strip()
        new_letter = data.replace("[name]", n)
        with open(f"./Output/ReadyToSend/LetterFor{n}.txt", mode="w") as send:
            send.write(new_letter)



