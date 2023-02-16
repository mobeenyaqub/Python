import random, art, game_data

print(art.logo)

first = ""
second = ""
i = 0
score = 0


def assignRandom():
    global first, second, i
    if i == 0:
        first = random.choice(game_data.data)
        i += 1
    else:
        first = second

    second = random.choice(game_data.data)
    while first == second:
        second = random.choice(game_data.data)


def printChoices():
    global first, second
    assignRandom()
    print(f"\n{first['name']} a/an {first['description']} from {first['country']}.")
    print(f"\n\n{art.vs}\n\n")
    print(f"{second['name']} a/an {second['description']} from {second['country']}.\n")


while True:
    printChoices()

    guess = input("Enter A or B: ").upper()

    if guess == "A":
        if first["follower_count"] > second["follower_count"]:
            score += 1
        else:
            print("\n\nYou lose!\n\n")
            break
    elif guess == "B":
        if second["follower_count"] > first["follower_count"]:
            score += 1
        else:
            print("\n\nYou lose!\n\n")
            break
    else:
        print("\n\nYou lose!\n\n")
        break

    print(f"\n\nScore: {score}\n\n")
