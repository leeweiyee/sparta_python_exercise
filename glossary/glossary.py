# My Python Glossary

# Python strings
example = "Hello, this is me."
print(example.lower()) # returns hello, this is me.
print(example.upper()) # returns HELLO, THIS IS ME.
print(example.capitalize()) # returns Hello, this is me.
print(example.replace("me", "Weiyee")) # returns Hello, this is weiyee.
print(example.split(",")) # returns ['Hello', ' this is me.']
white_space = "lots of space in the end       "
print(len(white_space.strip())) # returns lots of space in the end

# Strings in Python are arrays of bytes representing unicode characters
# String slicing:
test = "Hannah"
rev_test = test[-1:-7:-1]
rev_test2 = test[::-1]
print(len(test)) # returns 6
print(test[0:5]) # returns Hanna
print(rev_test) # returns hannaH
print(rev_test2) # returns hannaH
# Test for palindromes:
print(test.upper() == rev_test.upper()) # returns True

# Boolean methods with strings
greeting = 'Hello World'
print(greeting.isalpha()) # returns False
print(greeting.islower()) # returns False
print(greeting.isupper()) # returns False
print(greeting.endswith('!')) # returns False
print(greeting.startswith('H')) # returns True

# Boolean values and numbers
x = -1
y = 2
print(bool(x)) # returns True
print(bool(y)) # returns True
print(bool("abc")) # returns True
print(bool(123)) # returns True
print(bool(["apple", "cherry", "banana"])) # returns True
print(bool(None)) # returns False
print(bool(0)) # returns False
print(bool("")) # returns False
print(bool(())) # returns False
print(bool([])) # returns False
print(bool({})) # returns False

# Using .format() to insert arguments into strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Lists: ORDERED, CHANGABLE, ALLOWS DUBPLICATE MEMBERS, uses []
shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
print(shopping_list) # returns ['eggs', 'bread', 'bananas', 'biscuits', 'milk']
print(type(shopping_list)) # returns <class 'list'>
print(shopping_list[-1]) # returns milk
shopping_list[1] = "roti"
print(shopping_list) # returns ['eggs', 'roti', 'bananas', 'biscuits', 'milk']
shopping_list.pop()
print(shopping_list) # returns ['eggs', 'roti', 'bananas', 'biscuits']
shopping_list.pop(-2)
print(shopping_list) # returns ['eggs', 'roti', 'biscuits']
print(len(shopping_list)) # returns 3
shopping_list.append("ice cream")
print(shopping_list) # returns ['eggs', 'roti', 'biscuits', 'ice cream']
print(len(shopping_list)) # returns 4

# Tuples: ORDERED, UNCHANGABLE, ALLOWS DUPLICATE MEMBERS, uses ()
essentials = ('bread', 'eggs', 'milk')
print(essentials.count('bread')) # returns 1
essentials[0] = 'beans' # brings an error

# Dictionaries: UNORDERED, CHANGABLE, INDEXED, NO DUPLICATE MEMBERS, uses {}
student_1 = {
    'name': 'Susan',
    'stream': 'Tech',
    'completed lessons': 4,
    'completed lesson names': ['variables', 'data types', 'set up']
}
print(student_1) # returns the whole dictionary
print(student_1['completed lessons']) # returns 4
print(student_1.get('completed lessons')) # returns 4
print(student_1['completed lesson names'][1]) # returns data types
student_1['completed lesson names'].remove('data types')
print(student_1['completed lesson names']) # returns ['variables', 'set up']
student_1.pop('completed lessons') # .pop removes item with specific key name
print(student_1.keys()) # returns dict_keys(['name', 'stream', 'completed lesson names'])
print(student_1.values()) # returns dict_values(['Susan', 'Tech', ['variables', 'set up']])
print(student_1.items()) # returns dict_items([('name', 'Susan'), ('stream', 'Tech'), ('completed lesson names', ['variables', 'set up'])])

# Sets: UNORDERED, UNINDEXED, NO DUPLICATE MEMBERS; uses {}
car_parts = {'wheels', 'doors', 'exhaust'}
print(car_parts)
car_parts.add('windows')
print(car_parts)
car_parts.discard('doors')
print(car_parts)

# Frozen sets are immutable versions of sets similar to tuples
list = [1, 2, 3, 4]
x = frozenset(list)
print(type(x))

# Three Types of Control Flow
# 1. If statement
# 2. For loop
# 3. While loop

# If statement: execute a statement if a condition is true
# The following statement tests whether b is greater than a
a = 33
b = 200
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")
# returns b is greater than a

# For loop: execute a statement while iterating items in a list/string
# The following statement iterates over a sequence (a list in this case) and prints the value x 2
list_data = [1, 2, 3, 4, 5]
for num in list_data:
    print(num * 2)
# returns 2, 4, 6, 8, 10

# Break: stop the loop before it has looped through all the items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
# returns apple

# Continue: stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# returns apple, cherry

# While loop: execute a set of statements as long as a condition is true
# The following statement prints i as long as i is less than 6
i = 1
while i < 6:
    print(i)
    i += 1
# returns 1 2 3 4 5

# Exit the loop when i is 3:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# returns 1 2 3

# Continue to the next iteration if i is 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# returns 1 2 4 5 6

# Function: a block of code which only runs when it is called
# You can pass data, known as parameters, into a function
# A function can return data as a result
# A function is defined using the def keyword
# A parameter is the variable listed inside the parentheses in the function definition
# An argument is the value that is sent to the function when it is called
# To avoid getting an error in an empty function, use the pass statement
def myfunction():
  pass
# To let a function return a value, use the return statement
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
# A default value can be assigned to a parameter
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Lambda function: small anonymous function
# A lambda function can take any number of arguments, but can only have one expression
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Lambda functions can be used as an anonymous function inside another function
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11)) # returns 22
print(mytripler(11)) # returns 33

# Object-oriented programming (OOP) organizes software design around real-world objects
# A Class is like an object constructor, or a "blueprint" for creating objects
# All classes have a function called __init__(), which is always executed when the class is being initiated
# The __init__() function is used to assign values to object properties
# Objects can also contain methods. Methods in objects are functions that belong to the object
# The self parameter is a reference to the current instance of the class; used to access variables that belongs to the class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
# create an instance
p1 = Person("John", "Doe")
# call the instance variable
print(p1.firstname) # returns John
print(p1.lastname) # returns Doe
# call the method
p1.printname() # returns John Doe


# Four pillars of OOP:
# 1) Abstraction: to display only essential information to the user and hide the details
from animal import Animal # this step hides all the class code from the users
Dog1 = Animal("Nyme", 10)
Dog2 = Animal("Mone", 5)
print(Dog1.name)
print("The first dog's name is ", Dog1.name)
print(Dog1.age)
print(Dog1.eat())
print(Dog2.eat())

# 2) Encapsulation: to restrict access to methods and variables to prevent data from being modified by accident
# e.g. private methods
class Car:
    def __init__(self):
        self.__updateSoftware()
    def drive(self):
        print('driving')
    def __updateSoftware(self):
        print('updating software')
redcar = Car()
redcar.drive()
# redcar.__updateSoftware() is not accesible from object
# returns updating software, driving

# e.g. private variables
class Car:
    __maxspeed = 0
    __name = ""
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))
redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private
redcar.drive()

# 3) Inheritance: a class that inherits all the methods and properties from another class
# Parent class is the class being inherited from, also called base class
# Child class is the class that inherits from another class, also called derived class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
# The child's __init__() function overrides the inheritance of the parent's __init__() function
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()
# super() function  will make the child class inherit all the methods and properties from its parent
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# 4) Polymorphism: methods in child class that have the same name as the methods in the parent class
class Document:
    def __init__(self, name):
        self.name = name
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'
class Word(Document):
    def show(self):
        return 'Show word contents!'

documents = [Pdf('Document1'),
             Pdf('Document2'),
             Word('Document3')]
for document in documents:
    print(document.name + ': ' + document.show())
# returns:
# Document1: Show pdf contents!
# Document2: Show pdf contents!
# Document3: Show word contents!

# Method overloading: define a method in such a way that there are multiple ways to call it
class Human:
    def sayHello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
# create an instance
obj = Human()
# call the method
obj.sayHello()
# call the method with a parameter
obj.sayHello('Guido')
# returns:
# Hello
# Hello Guido

# Method overriding: modify a method in a child class that it inherited from the parent class
class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ' says Woof!'
class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ' says Meow!'
niko = Dog('Niko')
felix = Cat('Felix')
print(niko.speak())
print(felix.speak())
# returns:
# Niko says Woof!
# Felix says Meow!