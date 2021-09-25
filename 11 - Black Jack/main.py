from art import logo
from random import randint
import os

user_cards = []
user_sum = 0
dealer_cards = []
dealer_sum = 0
count = 0
play_again = 'y'

deck = {
  2 : 2,
  3 : 3,
  4 : 4,
  5 : 5,
  6 : 6,
  7 : 7,
  8 : 8,
  9 : 9,
  10 : [10, "Jack", "King", "Queen"],
  11 : "Ace"
}

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def random_card_assigner(app_card):
  card_no = randint(2,11)
  for card in deck:
    if card_no == 10:
      app_card.append(deck[card_no][randint(0,3)])
      return app_card
    elif card == card_no:
      app_card.append(deck[card])
      return app_card

def display_cards(count):
  print(f"\n\nUser cards : {user_cards}")
  if count == 0:
    print(f"Dealer cards : {dealer_cards[0]}\n\n")
    return 1
  else:
    print(f"Dealer cards : {dealer_cards}\n\n")

def check_sum(card_sum = 0, cards = []):
  card_sum = 0
  for card in cards:
    if card == "King" or card == "Queen" or card == "Jack":
      card_sum += 10
    elif card == "Ace":
      if card_sum + 11 <= 21:
        card_sum += 11
      else: 
        card_sum += 1
    else:
      card_sum += card

  return card_sum

while play_again == "y":

  cls()
  user_cards = []
  dealer_cards = []
  count = 0
  print(logo, "\n\n")

  for i in range(2):
    user_cards = random_card_assigner(user_cards)
    dealer_cards = random_card_assigner(dealer_cards)

  count = display_cards(count)

  choice = input("Press 'y' to add a card.\nPress 'n' to pass.\nEnter your choice : ")

  while choice == "y":
    user_cards = random_card_assigner(user_cards)
    user_sum = check_sum(user_sum, user_cards)
    print(f"\n{user_cards} User sum : {user_sum}\n")
    dealer_sum = check_sum(dealer_sum, dealer_cards)
    if user_sum > 21:
      display_cards(count)
      print(f"Dealer has won! Dealer points {dealer_sum}. User points {user_sum}.")
      break
    elif user_sum == 21:
      display_cards(count)
      print(f"User has won! User points {user_sum}. Dealer points {dealer_sum}.")
      break

    choice = input("Press 'y' to add a card.\nPress any key to pass.\nEnter your choice : ")  

  else:
    user_sum = check_sum(user_sum, user_cards)
    dealer_cards = random_card_assigner(dealer_cards)
    while dealer_sum < 17:
      dealer_cards = random_card_assigner(dealer_cards)
      dealer_sum = check_sum(dealer_sum, dealer_cards)
    
    if dealer_sum > 21:
      display_cards(count)
      print(f"\nUser has won. User points {user_sum}. Dealer points {dealer_sum}.")
    elif dealer_sum == 21:
      print(f"\nDealer has won! Dealer points {dealer_sum}. User sum {user_sum}.")
    elif dealer_sum > user_sum:
      display_cards(count)
      print(f"\nDealer has won! Dealer points {dealer_sum}. User sum {user_sum}.")
    elif dealer_sum == user_sum:
      display_cards(count)
      print(f"\nIt is a draw! User sum {user_sum}. Dealer points {dealer_sum}.")
    else:
      display_cards(count)
      print(f"\nUser has won. User points {user_sum}. Dealer points {dealer_sum}.")

  play_again = input("\n\n\nPress 'y' to play again.\nPress any key to exit.\nEnter your choice : ")