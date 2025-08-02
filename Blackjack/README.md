# Blackjack 🃏 (Python Console Game)

This is a simple command-line version of the classic card game **Blackjack**, implemented in Python. The player competes against the computer (dealer) to get a score as close to 21 as possible, without going over.

## 🛠️ Features

* Simulates a deck of cards
* Follows standard Blackjack rules
* Allows the user to draw additional cards
* Dealer draws automatically until reaching at least 17
* Handles special cases like Blackjack and Ace value adjustment
* Replay option for continuous play
* Includes fun emoji-based feedback messages

## 🃎 Game Rules

* Each player (you and the dealer) starts with 2 cards.
* You can choose to draw more cards (`y`) or pass (`n`).
* Face cards (J, Q, K) are worth 10; Ace can be 11.
* If your total exceeds 21, you **bust** and lose.
* The dealer draws cards until their total is 17 or more.
* The winner is decided based on who has the higher score without exceeding 21.
