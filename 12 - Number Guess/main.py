import art
from random import randint
print(art.logo)

random_number = randint(1,100)

difficulty = input("Press 1 for 'easy'\nPress any key for 'difficult'\nEnter your choice : ")

if difficulty == "1":
  lives = 10
else:
  lives = 5

while lives != 0:
  print(f"\nYou have {lives} lives left.")
  number = int(input("Enter a number : "))

  if number > random_number:
    print("\nToo high!")
    lives -= 1
  elif number == random_number:
    print(f"\nYour guess is right. Number is {number}.")
    break
  else:
    print("\nToo low!")
    lives -= 1

if lives == 0:
  print(art.you_lose)