from art import logo
from random import randint

print(logo, "\n\n")

user_cards = []
user_sum = 0
dealer_cards = []
dealer_sum = 0
count = 0

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

  choice = input("Press 'y' to add a card.\nPress 'n' to pass.\nEnter your choice : ")  

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




















##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.