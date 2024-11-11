'''
import random
class guess:
  def __init__(self, number):
    self.number = number
    self.guess = 0
  def  number_guessing_number(attempt,self_number):
    self_number=random.randint(1,100)
    attempt=0
    while True:
      guess=int(input("Enter your guess: "))
      attempt+=1
      if guess == self_number:
        print("You have the guessed the correct number {self_number} in {attempt} attempts")
      elif guess<self_number:
        print("Too high, try again")
      else:
        print("Too low,try again")
      break

n=int(input("Enter the number of attempts you want to take: "))
m=int(input("Enter the number for guessing: "))
guess.number_guessing_number(m,n)
'''


