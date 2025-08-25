from art import logo
import os 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

player_details={}
should_continue=True

def highest_bid(bids):
  highest_amount=0
  winner=""
  for bidder in bids:
    if bids[bidder]>highest_amount:
      highest_amount=bids[bidder]
      winner = bidder

  print(f"The winner is {winner} with a bid amount of ${highest_amount}")

while should_continue:
  player_name=input("What is your name?: ")
  player_bid=int(input("What is your bid?: $"))
  player_details[player_name]=player_bid
  decision=input("Are there any other bidders? Type 'yes' or 'no.\n").lower()
  if decision == "no":
    should_continue=False
    highest_bid(player_details)
  else:
    clear()

