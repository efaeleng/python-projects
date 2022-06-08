import random

while True:
  print("Welcome to Rock 👊, Paper 📰 And Scissors ✂️  game!")
  print("Rules ✍️: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.\n")
  user_input = input("Enter a choice (R)ock, (P)aper, (S)cissors: \n")
  possible_choices = ["R", "P", "S"]
  possible_outcome = random.choice(possible_choices)

  print(f"Player: {user_input} CPU: {possible_outcome}\n")

  if user_input == possible_outcome:
      print("It's a tie!\n")
  if user_input == "R" and possible_outcome == "S":
      print("Rock smashes Scissors. You win!\n")
  if user_input == "R" and possible_outcome == "P":
      print("Paper covers Rock. You lose!\n")
  if user_input == "P" and possible_outcome == "R":
      print("Paper covers Rock. You win!\n")
  if user_input == "P" and possible_outcome == "S":
      print("Scissors cuts Paper. You lose!\n")
  if user_input == "S" and possible_outcome == "P":
      print("Scissors cuts Paper. You win!\n")
  if user_input == "S" and possible_outcome == "R":
      print("Rock smashes Scissors. You lose!\n")
  if user_input not in possible_choices:
      print("Invalid input!")
      print("Please enter a valid choice!")
      print("(R)ock, (P)aper, (S)cissors\n")
      
      user_input = input("Do you want to play again? (y/n): ")
      if user_input == "y":   # if user_input == "y" or "Y":
        continue
      if user_input == "n":   # if user_input == "n" or "N":
        print("Thanks for playing!")
        break;
 
    