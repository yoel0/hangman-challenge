# print("Hello World")
from random import random
from math import floor
# Initialize game
secret_word = ""
letters_left = 0
hangman_guesses_left = 6
letters_guessed = []
errors = 0
underscored_secret_word = ""
secret_words = ["development", "random", "postman", "mountain", "python", "wrong"]
# visual variables
hangman1 = '''
______
|    |
|    O
|
|
|__________
'''
hangman2 = '''
______
|    |
|    O
|    |
|
|__________
'''
hangman3 = '''
______
|    |
|    O
|   /|
|
|__________
'''
hangman4 = '''
______
|    |
|    O
|   /|\\
|
|__________
'''
hangman5 = '''
______
|    |
|    O
|   /|\\
|   /
|__________
'''
hangman6 = '''
______
|    |
|    O
|   /|\\
|   / \\
|__________
'''
hangman_table = [
  f'\n{hangman6}\n',
  f'\n{hangman5}\n',
  f'\n{hangman4}\n',
  f'\n{hangman3}\n',
  f'\n{hangman2}\n',
  f'\n{hangman1}\n'
]
# -----------------------------PLANNING------------------------------
# global variables up above
# functions
  # game_init
  # win, lose
  # add_to_guesses
  # success
  # print_hangman
  # failure
  # continue_game
# game loop
def game_init():
  global secret_word
  global letters_left
  global hangman_guesses_left
  global letters_guessed
  global errors
  global underscored_secret_word
  random_index = floor(random() * 6)
  secret_word = secret_words[random_index]
  letters_left = len(secret_word)
  hangman_guesses_left = 6
  letters_guessed = []
  errors = 0
  # print(secret_word) # For use testing
  underscored_secret_word = ""
  i = 0
  while i < len(secret_word):
    underscored_secret_word = underscored_secret_word + "_ "
    i += 1
def lose():
  print("HANGMAN :(")
  print(f"The word was {secret_word}.")
def win():
  print("You won!")
  print(f"The word was {secret_word}.")
def add_to_guesses(guess):
  letters_guessed.append(guess)
def success(guess):
  global underscored_secret_word
  global win
  print("Correct")
  add_to_guesses(guess)
  index = 0
  for letter in secret_word:
    if letter == guess:
      # handles the case for when the first letter in the secret word is the guess
      if index == 0:
        underscored_secret_word = guess + underscored_secret_word[1:] # apple -> a _ _ _ _
      # handles the case for when the guessed letter is not the first or the last letter
      elif index < (len(secret_word) - 1):
        underscored_secret_word = underscored_secret_word[0:((index * 2))] + guess + " " + underscored_secret_word[(index * 2 + 2):]
      # handles the case for when the guessed letter is the last letter in the secret word
      else:
        underscored_secret_word = underscored_secret_word[:-2] + guess
    index += 1
  # check if all letters have been guessed, and if so run win() otherwise we'll continue the game
  for letter in underscored_secret_word:
    if letter == "_":
      continue_game()
      return
  win()
def print_hangman(incorrect_guesses_left):
  print(hangman_table[incorrect_guesses_left])
def failure(guess):
  global hangman_guesses_left
  add_to_guesses(guess)
  hangman_guesses_left -= 1
  print_hangman(hangman_guesses_left)
  continue_game()
def already_guessed():
  print("You already guessed that.")
  continue_game()
def continue_game():
  global errors
  print(f"You have {hangman_guesses_left} guesses left.")
  print(f"You have guessed: {letters_guessed}")
  print(f"The word you need: {underscored_secret_word}")
  # can the user continue to make guesses or is the game over?
  if hangman_guesses_left > 0:
    guess = input("Guess a letter:\n").lower()
    if guess == secret_word:
      win()
      return
    # we could handle special cases here - so if the user guessed a non letter character or multiple letters
    # we could allow one error before counting that against the user
    if len(guess) > 1 and errors < 1:
      print("It looks like you accidentally entered more than one character or guessed the wrong word.")
      errors += 1
      continue_game()
      return
    try:
      int(guess)
      if errors < 1:
        print("It looks like you accidentally entered a number.")
        errors += 1
        continue_game()
        return
    except ValueError:
      pass
    if guess in letters_guessed:
      already_guessed()
      return
    for letter in secret_word:
      if letter == guess:
        success(guess)
        return
    failure(guess)
    return
  else:
    lose()
# our game loop that is going to continue running the game
# it will call our game_init() function and initially run the continue_game() function
# I also want it to prompt the user to see if the user wants to continue playing or not
looping = True
game_init()
continue_game()
while looping:
  should_continue = input("Would you like to play again? yes or no\n").lower()
  if should_continue == "yes" or should_continue == "y":
    game_init()
    continue_game()
  elif should_continue == "no" or should_continue == "n":
    print("Thanks for playing!")
    looping = False
  else:
    print("I'm not sure whether that means yes or no.\n")