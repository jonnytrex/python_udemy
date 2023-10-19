#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
print("Welcome to the guessing game")
difficulty = input("Type 'hard' or 'easy' ")
if difficulty == "hard":
  number_of_guesses = 5
else: 
  number_of_guesses = 10

correct_number = random.choice(range(1,101))

def check_guess(guess,correct,guess_num):
  if guess == correct:
    return "Win"

  elif guess > correct: 
    return "High"
    
  else:
    return "Low"


for num in range(1,number_of_guesses+1):
  num_left = number_of_guesses - num
  guess = int(input("Guess a number between 1 and 100: "))
  checked_guess = check_guess(guess,correct=correct_number,guess_num = num)
  if checked_guess == "Win":
    print(f"You win! The correct number is {correct_number}")
    exit()
  elif checked_guess == "High":
    print("Too high.  Guess again. ")
    print(f"You have {num_left} attempts remaining")
  else:
    print("Too low. Guess again.")
    print(f"You have {num_left} attempts remaining")
  
  
  
  

  



