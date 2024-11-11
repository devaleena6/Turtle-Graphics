import turtle

t=turtle.Turtle()
s=turtle.getscreen()
s.bgcolor("light blue")


def draw_circle(color,radius,x,y):
    t.fillcolor(color)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
draw_circle("white",30,0,-40)
draw_circle("white",40,0,-100)
draw_circle("white",60,0,-200)


draw_circle ("black", 2, -10, -10)  
draw_circle ("black", 2, 10, -10)   
draw_circle ("red", 3, 0, -15)

def hands(x,y,length,angle):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(angle)
    t.fd(length)
    t.setheading(angle+20)
    t.fd(20)
    t.penup()
    t.setheading(angle-20)
    t.fd(20)
    t.penup()
    t.home()
hands(-70,-50, 50, 160) 
hands(70,-50, 50, 20)    
    
