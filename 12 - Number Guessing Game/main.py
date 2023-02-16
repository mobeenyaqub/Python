import random


def playGame(attempts):
    number = random.randint(1, 100)

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}\n")
        guess = int(input("\n\nEnter a number: "))

        if guess > number:
            print("\nToo high!\n")
        elif guess < number:
            print("\nToo low!\n")
        else:
            print(f"\n{number} guessed correctly!!!\n")
            return

        attempts -= 1

    print(f"\nYou lose!!! Number was {number}\n")


print("I'm thinking of a number between 1 and 100.")

easyOrHard = input("Easy or hard?").lower()
if easyOrHard == "easy":
    playGame(10)
else:
    playGame(5)
