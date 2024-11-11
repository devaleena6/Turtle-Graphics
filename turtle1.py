Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import trutle
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import trutle
ModuleNotFoundError: No module named 'trutle'
import turtle
from turtle import *
b=turtle.Turtle()
b.shape(turtle)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b.shape(turtle)
  File "C:\Users\KIIT\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 2832, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named <module 'turtle' from 'C:\\Users\\KIIT\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\turtle.py'>
>>> b.shape("turtle")
>>> c=turtle.screen()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    c=turtle.screen()
AttributeError: module 'turtle' has no attribute 'screen'. Did you mean: 'Screen'?
>>> c=turtle.Screen()
>>> c.bgcolor("black")
>>> b.color("red")
>>> turtle.colormode(255)
>>> c.bgcolor(170,30,20)
>>> c.title("Turtle1")
