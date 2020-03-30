#create a variable
'''
x = 1
name = 'John'
print(name)
a = 1
b = 2
c = 3
hi = 'Hello World'
print(hi)
'''

# firstname =input('What is your first name? ')
# lastname = input('What is your last name? ')
# age = input('What is your age? ')
# dob = input('What is your DOB? ')
# address = input('What is your address? Please include your house number. ')
#
# print('Your name is ' + firstname + ' ' + lastname + '. You are ' + age + ' years old, born on ' + dob + ', and you live in ' + address + '. ')

# float = 1.123
# int = 2
# print(float + int)
# name = 'xyz'
# print(str(int)+name)

# single_quotes = 'Look!'
# double_quotes = "Look!"
# print(single_quotes)
# print(double_quotes)
# example = "here's me"
# print(example.upper())
# print(example.capitalize())
# print(example.replace("me", "weiyee"))

# String methods
# white_space = "lots of space in the end       "
# print(len(white_space))
# print(len(white_space.strip()))

# Concatenation and casting
# a = "here "
# b = "more "
# c = "much more"
# d = 10
# print(a + b + c, d)

# String to numeric casting
# int_string = "6"
# print(int(int_string))
# print(type(int(int_string)))
# print(float(int_string))
# print(type(float(int_string)))

# Boolean and None
# a = True
# b = False
# print (a == b)
# print (a != b)
# print (a >= b)
# print (b >= a)
# print (True and False)

# Boolean methods with strings
# hi = 'Hello World'
# print(hi.isalpha())
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith('!'))
# print(hi.startswith('H'))

# Boolean values and numbers
# x = -1
# y = 2
# print(bool(x))
# print(bool(y))
# print(bool(None))

# test = "Hannah"
# rev_test = test[-1:-7:-1]
# rev_test2 = test[::-1]
# print(test)
# print(rev_test)
# print(test.upper() == rev_test.upper())

# Lists: ORDERED, CHANGABLE, ALLOWS DUBPLICATE MEMBERS, uses []
# shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[-1])
# shopping_list[1] = "roti"
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)
# shopping_list.pop(-2)
# print(shopping_list)
# print(len(shopping_list))
# shopping_list.append("ice cream")
# print(shopping_list)
# print(len(shopping_list))

# Mixed data type lists
# mixture = [1, 2, 3, "one", "two", "three"]
# print(mixture)
# List slicing
# print(mixture[1:3])
# print(mixture[-2::])
# print(mixture[-2::-1])

# Practice IF statements
# a = input("Give me a first number: ")
# b = input("Give me a second number: ")
# c = input("Give me a third number: ")
# if a>b and a>c:
#     print("{} is the biggest number.".format(a))
# elif b>c and b>a:
#     print("{} is the biggest number.".format(b))
# else:
#     print("{} is the biggest number.".format(c))

# a = int(input("Give me a number: "))
# if a % 2 == 0:
#     print("{} is an even number.".format(a))
# else:
#     print("{} is an odd number.".format(a))

# For loops
# list_data = [1,2,3,4,5]
# # variable num is defined by user
# for num in list_data:
#     print(num*2)

# Declare a list of 10 numbers, check condition if a<15, write to another list, print list
# list_1 = [1,2,4,5,6,8]
# new_list = []
# for num in list_1:
#     if num<5:
#         new_list.append(num)
#     else:
#         continue
# print(new_list)

def is_even_position(list_param, value):
    if list_param[value] % 2 == 0:
        return True
    else:
        return False
t = [9,8,7,6,5,4,3,2,1,6]
print(is_even_position(t,6))
print(is_even_position(t,3))
print(is_even_position(t,1))