import random

while True:
  print("Welcome to Rock 👊, Paper 📰 And Scissors ✂️  game!")
  print("Rules ✍️: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.\n")
  user_input = input("Enter a choice (r)ock, (p)aper, (s)cissors: \n")
  possible_choices = ["r", "p", "s"]
  possible_outcome = random.choice(possible_choices)

  print(f"You chose: {user_input} Computer chose: {possible_outcome}\n")

  if user_input == possible_outcome:
      print("It's a tie!\n")
  if user_input == "r" and possible_outcome == "s":
      print("Rock smashes Scissors. You win!\n")
  if user_input == "r" and possible_outcome == "p":
      print("Paper covers Rock. You lose!\n")
  if user_input == "p" and possible_outcome == "r":
      print("Paper covers Rock. You win!\n")
  if user_input == "p" and possible_outcome == "s":
      print("Scissors cuts paper. You lose!\n")
  if user_input == "s" and possible_outcome == "p":
      print("Scissors cuts paper. You win!\n")
  if user_input == "s" and possible_outcome == "r":
      print("Rock smashes Scissors. You lose!\n")
  if user_input not in possible_choices:
      print("Invalid input!")
      print("Please enter a valid choice!")
      print("(r)ock, (p)aper, (s)cissors\n")
      
      user_input = input("Do you want to play again? (y/n): ")
      if user_input == "y":   # if user_input == "y" or "Y":
        continue
      if user_input == "n":   # if user_input == "n" or "N":
        print("Thanks for playing!")
        break;
 
    