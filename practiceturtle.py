import turtle
s=turtle.getscreen()
t=turtle.Turtle()
'''
t.color("red","blue")
turtle.bgcolor("white")

t.shapesize(1,5,10)
t.shapesize(10,5,1)
t.shapesize(1,10,5)
t.shapesize(10,1,5)
'''

'''

t.shapesize(3,3,3)
t.pensize(5)
t.forward(100)
t.rt(90)
t.forward(100)
t.rt(90)
t.forward(100)
t.rt(90)
t.forward(100)
t.rt(90)

t.circle(40)
t.dot(40)

'''
'''
t.goto(20,20)
t.goto(-20,20)
t.goto(10,-30)
t.goto(-10,-30)

t.goto(0,0)
t.home()



turtle.title("My first turtle program")
'''

'''
import random
name = input("What is your name? ")
print("Good Luck ! ", name)
words = ['rainbow','computer','science','programming',
'python', 'mathematics', 'player', 'condition',  'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 12
while turns > 0:  
  failed = 0  
  for char in word:
    if char in guesses:
      print(char, end=" ")
    else:
      print("_")
      failed += 1

  if failed == 0:
    print("You Win")
    print("The word is: ", word)
    break
  print()
  guess = input("guess a character:")
  guesses += guess
  if guess not in word:
    turns -= 1
    print("Wrong")
    print("You have", + turns, 'more guesses')
    if turns == 0:
      print("You Loose")

'''
'''

A, B, C, D, E, F = map(int,input().split())
print(A, B, C, D, E, F)



import turtle
s=turtle.getscreen()
t=turtle.Turtle()
'''








