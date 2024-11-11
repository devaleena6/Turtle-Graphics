'''
import math
class Calculator:
  def __init__(self,num):
    self.num=num
  @staticmethod
  def greet():
    print("Hello users")
  def square(self,num):
    return num**2
  def cube(self,num):
    return num**3
  def squareroot(self,num):
    if num<0:
      print("it will not work")
      return math.sqrt(num)
num1=int(input("Enter the number: "))
cal=Calculator(num1)
Calculator.greet()
print("The square of the number is",cal.square(num1))
print("The cube of the number is",cal.cube(num1))
print("The square root of the number is",cal.squareroot(num1))
'''

class Train:
  def __init__(self,name,fare,seats,totalseats):
    self.name=name
    self.fare=fare
    self.seats=seats
    self.available=totalseats
  def status(self):
    print("The name of the train is: ", self.name)
    print("The number of seats are: ", self.seats)
  def fare(self):
    print("The fare of the train is: ", self.fare)
  def booking(self, num_seats):
    if num_seats<= self.available:
      self.available=self.available-num_seats
      print("Your ticket has been booked")
      return true
    else:
      print("Your ticket has not been booked")
      return false

'''
name1=input("Enter the name of the train: ")
fare1=(input("Enter the fare of the train"))
seats1=(input("Enter the number of the seats"))
totalseats1=(input("Enter the total number of seats"))
train1=Train(name1,fare1,seats1,totalseats1)
print("The status of the train is",train1.status())
print("The fare of the train is",train1.fare())
print("The booking of the train is",train1.booking())
      
  '''


  
