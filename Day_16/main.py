# OOP - Object Oriented Programming

# Classes - These are basically blueprints that provide a structure and 
# functionality to objects that we create from these classes.

from turtle import Turtle, Screen


turtle1 = Turtle()

turtle1.shape("turtle")
turtle1.color("SeaGreen")
turtle1.fd(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Object created from classes get attributes and methods from the classes and 
# can be used 
