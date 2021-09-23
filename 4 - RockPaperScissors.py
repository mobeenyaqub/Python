import random

choice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors."))

computer = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

if choice == computer:
    print("It's a draw!")
elif choice == 0 and computer == 1 or choice == 1 and computer == 2 or choice == 2 and computer == 0:
    print("You lose!")
else:
    print("You Win!")

