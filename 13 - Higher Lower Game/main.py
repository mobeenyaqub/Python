import art
from random import randint
from game_data import data

print(art.logo)

score = 0
winning = True
choice = ''

while winning:
  random_num1 = randint(0,49)
  random_num2 = randint(0,49)
  while random_num1 == random_num2:
    random_num2 = randint(0,49)

  choice_A = data[random_num1]['follower_count']
  choice_B = data[random_num2]['follower_count']

  print(f"\n\nCompare A : {data[random_num1]['name']}, a {data[random_num1]['description']}, from {data[random_num1]['country']}")

  print(art.vs)

  print(f"Compare B : {data[random_num2]['name']}, a {data[random_num2]['description']}, from {data[random_num2]['country']}")

  choice = input("\nWho has more followers? Type 'A' or 'B' : ").upper()

  if choice == "A":
    if choice_A > choice_B:
      winning = True
      score +=1
    else:
      winning = False
  elif choice == "B":
    if choice_B > choice_A:
      winning = True
      score +=1
    else:
      winning = False


print(f"\n\n\nYour score {score}")