from __future__ import division


print("Hello World")

greeting = "hello world"

print(greeting)

# We created a variable called "greeting" and given it the value of a string "hello world". To access the data in the variable, we can just use the variable name

string  = "Represents characters"
integer = 10 # a whole number
float = 10.0 # a number with a decimal
none = None # a blank data type, useful as a placeholder
boolean = True
boolean = False # a true or false

# methods allow us to find out or change properties of our data
# we can use some methods with .notation
# object.method() - some methods will need parameters, some won't.

# variables are like boxes - we store data in them, and retrive the data by using the label we have given the box - the variable name

# the names should be logical - if someone handed you a box that says "shoe box" you would expect to see shoes in it. That might help you know what to do with the box, or how to treat the box, Variables are the same. If you name them logically, it will give you some indication or clue as to what the data inside is. The names should also use the snake_case convention

my_name="Klong"

# from the variable name, it's clear that the data will be a name, and a string. We don't know the name explicitly, but it gives us some context

# we can interpolate the variables and the data inside them with a number of methods

print("Hello", my_name) # parameters
print("Hello " + my_name) # concatenation
print("Hello {}".format(my_name))
print(f"Hello {my_name}") # interpolation

# variables are assigned to the value using an assignment operator  =
# we have many operators
# Arithmetic Operators
# + addition
# - subtraction
# * multiplication
# ** exponential
# / division
# % modulous

# we can combine assignment operators and arithmetic operators to do the sum and update the value of the variable

score = 0

print("You won! You gain ten points!")

score +=10

# it doesn't matter what score was in the first place - we're going to add ten to it, and update the variable to have that value

