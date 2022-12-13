#guessing number (data 13/12/2022)
from art import logo
from random import randint
def compare(guess):
  
  print(f"You have {guess} attempts reamianing to guess the number.")
  while guess != 0:
    guess_num=int(input("Make a guess :"))
    if guess_num > random_num :
      print("Too high.")
      print("Guess agian.")
      guess-=1
      print(f"You have {guess} attempts reamianing to guess the number.")
    elif guess_num < random_num:
      print("Too Low.")
      print("Guess agian.")
      guess-=1
      print(f"You have {guess} attempts reamianing to guess the number.")
    else:
      print(f"You got it! ,The answer was {random_num} ")
      guess =0
  
  if guess_num >random_num :
    print("Too high.")
    print("You've ran out of guesses ,you lose.")
  elif guess_num< random_num:
    print("Too low.")
    print("You've ran out of guesses ,you lose.")  
#** function start  **     
print(logo)
print("Welcome to Number guessing game ")
print("I'm thinking of a number between 1 to 100")
random_num = randint(1,100)
choice=input("Choose a difficulty . Type 'easy' or 'hard' :")
print(random_num) 
if choice == "easy":
  guess=10
  compare(guess)
else:
  guess =5
  compare(guess)
