class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def talk(self):
        age = input('How old are you? ')
        return("{} is {} years old.".format(self.firstname, age))