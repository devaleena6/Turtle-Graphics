Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
import Turtle
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import Turtle
ModuleNotFoundError: No module named 'Turtle'
import turtle
from turtle import *
a=turtle.Turtle()
a.shape()
'classic'
a.shape("turtle")
\
help(turtle.shape)
Help on function shape in module turtle:

shape(name=None)
    Set turtle shape to shape with given name / return current shapename.

    Optional argument:
    name -- a string, which is a valid shapename

    Set turtle shape to shape with given name or, if name is not given,
    return name of current shape.
    Shape with name must exist in the TurtleScreen's shape dictionary.
    Initially there are the following polygon shapes:
    'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'.
    To learn about how to deal with shapes see Screen-method register_shape.

    Example:
    >>> shape()
    'arrow'
    >>> shape("turtle")
    >>> shape()
    'turtle'

>>> a.color()
('black', 'black')
>>> a.forwrad(100)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.forwrad(100)
AttributeError: 'Turtle' object has no attribute 'forwrad'. Did you mean: 'forward'?
>>> a.forward(100)
>>> a.color(red)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.color(red)
NameError: name 'red' is not defined
>>> a.color("red")
>>> a.forward(100)
>>> a.color("blue","green")
>>> a.backward(100)
>>> a.color(120,40,50)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.color(120,40,50)
  File "C:\Users\KIIT\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 2215, in color
    pcolor = self._colorstr(pcolor)
  File "C:\Users\KIIT\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 2704, in _colorstr
    return self.screen._colorstr(args)
  File "C:\Users\KIIT\AppData\Local\Programs\Python\Python312\Lib\turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color sequence: %s" % str(color))
turtle.TurtleGraphicsError: bad color sequence: (120, 40, 50)
>>> turtle.colormode(255)
>>> a.color(120,40,50)
