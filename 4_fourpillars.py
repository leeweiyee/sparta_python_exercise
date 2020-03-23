# FOUR PILLARS of Object Oriented Programming

# Abstraction: displaying only essential information to the user and hiding the details from the user

# from animal import Animal # can use * as well which means fetch everything from animal.py
#                                 # this step hides all the class code from the users
# Dog1 = Animal("Nyme", 10)
# Dog2 = Animal("Mone", 5)
# print(Dog1.name)
# print("The first dog's name is ", Dog1.name)
# print(Dog1.age)
# print(Dog1.eat())
# print(Dog2.eat())

# Inheritance: a mechanism in which one class acquires the property of another class
# Allows you to call methods of the superclass in your subclass
# Primary use case of this is to extend the functionality of the inherited method

# from animal import Animal
# class Reptile(Animal): #the reptile class (child) inheriting from the animal class (parent)
#     def __init__(self, name, age):
#         super().__init__(name, age) # this super command is a must for inheritance such that everything from the
#                                     # parent (animal) is brought to the child (reptile)
#     def sleep(self):
#         return('zzzz I am sleeping')
#     def running(self, speed):
#         return('I am running at {} speed'.format(speed))
#
# Rept1 = Reptile("Lizzard", 5)
# Rept2 = Reptile("Mosy", 8)
# print(Rept1.eat())
# print(Rept1.running(10))

# Create a parent class person with the attributes (firstname, lastname) and method talk
# Create a child class student with the attributes (firstname, lastname) and add method enjoy and chill
# At least one method should get a value from the user

from person import Person
class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
    def enjoy(self):
        hobby = input('What is your hobby? ')
        return('{}\'s hobby is {}.'.format(self.firstname,hobby))
    def chill(self):
        return('{} enjoys chilling.'.format(self.firstname))

student1 = Student('Weiyee', 'Lee')
print(student1.talk())
print(student1.enjoy())
print(student1.chill())

# Encapsulation: restrict access to methods and variables to prevent data from being modified by accident

from reptile import *
class Snake(Reptile):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.name = name
        self.age = age
    def seek_heat(self):
        return("Let me see some sunshine")
    def sleep(self):
        return("Please leave me to sleep")


# Polymorphism