import random
from art import logo


EASY_ATTEMPTS=10
HARD_ATTEMPTS=5

def diff(difficulty):
  if difficulty == "easy":
    return EASY_ATTEMPTS
  else:
    return HARD_ATTEMPTS

def check_answer(computer_choice,guess_value,guess):
  if computer_choice > guess_value:
    print("Too Low")
    return guess-1
  elif computer_choice < guess_value:
    print("Too High ")
    return guess-1
  else:
    print(f"You got it! The answer was {computer_choice}.")


def game():
  print(logo)
  print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
  difficulty=input("Choose a diffuculty. Type 'easy' or 'hard': ")
  computer_choice= random.randint(1,100 )
  print(f"pssst,the correct answer is {computer_choice}")
  guess=diff(difficulty)
  guess_value=0
  while guess_value!=computer_choice:
    print(f"You have {guess} attempts remaining to guess the number ")
    guess_value=int(input("Make a guess: "))
    guess=check_answer(computer_choice,guess_value,guess)
    if guess == 0:
      print("You've run out of guesses,you lose")
      return
    elif guess_value != computer_choice:
      print("Guess again")

game()