import turtle
import random
'''
index_positions=[
for index in range(0,2)
'''
s=turtle.getscreen()
s.bgpic('road1.gif')
player1=turtle.Turtle()
player1.color("green")
player1.penup()
player1.goto(-200,100)

player2=turtle.Turtle()
player2.color("blue")
player2.penup()
player2.goto(-200,-100)

fl=turtle.Turtle()
fl.penup()
fl.goto(200,100)
fl.pendown()
fl.color("black")
fl.rt(90)
fl.fd(200)

dice=[1,2,3,4,5,6]


for i in range(20):
    if player1.pos()>=(400,100):
        print("player 1 wins")
    elif player2.pos()>=(400,-100):
        print("Player2 wins")
    else:
        turnplayer1=input("Press 'Enter' to roll the dice: ")
        dice_outcome=random.choice(dice)
        print("The result is: ")
        print(dice_outcome)
        print("The steps will be: ")
        print(20*dice_outcome)
        player1.fd=20*dice_outcome
        

        turnplayer2=input("Press 'Enter' to roll the dice: ")
        dice_outcome=random.choice(dice)
        print("The result is: ")
        print(dice_outcome)
        print("The steps will be: ")
        print(20*dice_outcome)
        player2.fd=20*dice_outcome

        





