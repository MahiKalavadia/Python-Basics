#Creating Variables : Variables are case sensitive
x = 5
y = "John"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

#Single or Double Quotes?(Both are same. Can use anyone)
x = "John"
# is the same as
x = 'John'

# Variable Names
  #Rules for Python variables:
      #A variable name must start with a letter or the underscore character
      #A variable name cannot start with a number
      #A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
      #Variable names are case-sensitive (age, Age and AGE are three different variables)
      #A variable name cannot be any of the Python keywords.

#Legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Multi Words Variable Names
 # 1 Camel Case :- Each word, except the first, starts with a capital letter:
 
myVariableName = "John"

 # 2 Pascal Case :- Each word starts with a capital letter:

MyVariableName = "John"

 # 3 Snake Case :- Each word is separated by an underscore character:

my_variable_name = "John"

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables
x = "Python is awesome"
print(x)

   #or 
        
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

   #or 

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

#Global Variables
  # Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
  # Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# The global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)