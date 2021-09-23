import os
import art

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print(art.logo)

name_bid = {}
highest_bid = 0
bidder_name = ''

def append_name_bid():
  name = input("\nEnter your name : ")
  bid = int(input("Enter your bid : $"))
  name_bid[name] = bid

more_users = 1

while more_users == 1:
  append_name_bid()
  more_users = int(input("\nAre there more bidders?\nPress 1 for 'yes'\nPress 2 for 'no'\nEnter your answer : "))
  cls()
else:
  for names in name_bid:
    if name_bid[names] > highest_bid:
      bidder_name = names
      highest_bid = name_bid[names]
  
  print(f"\n\n\t\t\t\t\t{bidder_name} with winning bet of ${highest_bid}")