num = 0
import random
def generate_random_number():
  return random.randint(0,100)

def difference_from_answer(guess, answer):
  if guess == answer:
    return "Correct"
  elif guess > answer:
    return "Too high"
  elif guess < answer:
    return "Too low"

def make_a_guess (answer):
  guess = input("Guess a number between 0-100")
  difference_from_answer(guess, answer)
