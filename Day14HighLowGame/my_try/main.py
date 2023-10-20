# import art log
# import game_data contains list of dictionary entries
# need to prompt the user with a choice of 'A' or 'B' to see which his higher
# keep a running tally of correct guesses
# tell user whether they're correct, increment correct guess counter
# if wrong tell user and end game
# after every correct guess prompt the user with a new choice after clear()
import random
from art import logo, vs
from Day14HighLowGame.my_try.game_data import data
from replit import clear

def choose_data():
  choiceA = random.choice(data)
  A_name = choiceA["name"]
  A_count = choiceA["follower_count"]
  A_desc = choiceA["description"]
  A_country = choiceA["country"]
  choiceB = random.choice(data)
  B_name = choiceB["name"]
  B_count = choiceB["follower_count"]
  B_desc = choiceB["description"]
  B_country = choiceB["country"]
  return A_name, A_count, A_desc, A_country, B_name, B_count, B_desc, B_country

def compare_counts(aCount, bCount, choice):
  if aCount > bCount:
    if choice == 'A':
      return "Correct"
    else:
      return "Wrong"
  elif aCount < bCount:
    if choice == 'B':
      return "Correct"
    else:
      return "Wrong"
    return "bCount is higher"
  else:
    return "Tie"


score = 0
gameOver = False
while not gameOver:
  print(logo)
  print(f"Welcome! Current score is {score}")
  print("Who has more instagram followers? ")
  choice_data = choose_data()
  
  print(f"A. {choice_data[0]}, a {choice_data[2]} from {choice_data[3]}")
  print(vs)
  print(f"B. {choice_data[4]}, a {choice_data[6]} from {choice_data[7]}")
  player_choice = input("Choose 'A' or 'B'")
  result = compare_counts(aCount=choice_data[1], bCount=choice_data[5], choice=player_choice)
  if result == "Correct":
    clear()
    print(result) 
    score += 1
  elif result == "Wrong":
    clear()
    print(result)
    gameOver = True
  else:
    clear()
    print(result) 
    score += 1
    
    
  









