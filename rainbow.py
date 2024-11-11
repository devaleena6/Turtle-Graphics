import turtle

s=turtle.getscreen()
t=turtle.Turtle()
s.bgcolor("light blue")


def semi_circle(col,rad,val):
    t.color(col)
    t.circle(rad,-180)
    t.penup()
    t.setpos(val,0)
    t.pendown()
    t.right(180)
    
col=['violet','indigo','blue','green','yellow','orange','red']
t.right(90)
t.width(10)
t.speed(7)

for i in range(7):
    semi_circle(col[i],10*(i+8),-10*(i+1))
        
t.hideturtle()




