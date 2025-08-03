# 🏆 Secret Auction Program (Python Console App)

This is a simple Python console program that simulates a **secret auction**. Each bidder enters their name and bid amount without seeing others’ bids. Once all bids are collected, the program determines the **highest bidder** and announces the winner.

## ✅ Features

* Accepts multiple bidders
* Clears the screen after each bid for secrecy
* Tracks all bids in a dictionary
* Determines and displays the highest bidder
* Uses ASCII logo (optional)

## 🧠 Program Flow

1. Each player is prompted for their name and bid.
2. The screen is cleared after every bid (for secrecy).
3. Once all bids are in (`'no'` entered), the highest bidder is announced.

## 📝 Notes

* `os.system('cls'/'clear')` is used to clear the screen and may behave differently on some systems (works best in a terminal).
* This program assumes valid numeric input for bids.
* Great starting point for learning dictionaries, conditionals, and loops in Python!
