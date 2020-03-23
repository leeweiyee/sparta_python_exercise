# list = [10,111,24, 56, 78, 75, 65, 80]
# even_list = []
# odd_list = []
# for num in list:
#     if num % 2 == 0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)
# print(list)
# print(even_list)
# print(odd_list)

# Tuples: ORDERED, UNCHANGABLE, ALLOWS DUPLICATE MEMBERS, uses ()
# essentials = ('bread', 'eggs', 'milk')
# print(essentials)
# print(essentials.count('bread'))
# essentials[0] = 'beans' # brings an error

# Dictionaries: UNORDERED, CHANGABLE, INDEXED, NO DUPLICATE MEMBERS, uses {}
# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# print(thisdict)
# student_1 = {
#     'name': 'Susan',
#     'stream': 'Tech',
#     'completed lessons': 4,
#     'completed lesson names': ['variables', 'data types', 'set up']
# }
# print(student_1)
# print(student_1['completed lessons'])
# print(student_1['completed lesson names'][1])
# student_1['completed lesson names'].remove('data types')
# print(student_1['completed lesson names'])

# Sets: UNORDERED, UNINDEXED, NO DUPLICATE MEMBERS; uses {}
# car_parts = {'wheels', 'doors', 'exhaust'}
# print(car_parts)
# car_parts.add('windows')
# print(car_parts)
# car_parts.discard('doors')
# print(car_parts)

# Frozen sets are immutable versions of sets similar to tuples
# list = [1, 2, 3, 4]
# x = frozenset(list)
# print(type(x))

# Three Types of Control Flow
# 1. If statements
# 2. For statements
# 3. While loop

# age = 25
# if age < 19:
#     print("You are note eligible to watch this film.") #indentation is very important
# else:
#     print("You are good to go.")

# film_rating = input("What is the film rating? ")
# if film_rating.lower() == "universal":
# 	print("all age groups can watch this film")
# elif film_rating.lower() == "pg":
# 	print("General viewing, but some scenes may be unsuitable for young children.")
# elif film_rating.lower() == "12" or film_rating == "12a":
# 	print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
# elif film_rating.lower() == "15":
# 	print("No one younger than 15 may see a 15 film in a cinema.")
# elif film_rating.lower() == "18":
# 	print("No one younger than 18 may see an 18 film in a cinema.")
# else:
# 	print("this is not a correct rating, please use unniversal, pg, 12, 12a, 15, 18")

# Exercise FizzBuzz
# for number in range(51):
# 	if number % 3 == 0:
# 		print("Fizz")
# 	elif number % 5 == 0:
# 		print("Buzz")
# 	elif number % 3 == 0 and number % 5 == 0:
# 		print('Fizzbuzz')
# 	else:
# 		print(number)
# number = int(input('Please enter a number: '))
# number_range = list(range(1, number+1))
# for number in number_range(51):
# 	if number % 3 == 0:
# 		print("Fizz")
# 	elif number % 5 == 0:
# 		print("Buzz")
# 	elif number % 3 == 0 and number % 5 == 0:
# 		print('Fizzbuzz')
# 	else:
# 		print(number)
# For loops
# fruits = ['apple', 'bananas', 'cherry']
# for x in fruits:
# 	print(x)
# 	if x == 'banana'
# 		break

# for x in range(6):
# 	print (x)
# else:
# 	print("Finally Finished")

# adj = ['red', 'big', 'tasty']
# fruits = ['apple', 'bananas', 'cherry']
# for x in adj:
# 	for y in fruits:
# 		print(x, y)

# list_data = [1,2,3,4,5,6]
# embedded_list = [[1,2,3],[4,5,6]]
#
# for x in embedded_list:
# 	print(x)
# 	for y in x:
# 		print(y)

# dict_data = {1: {"name":"Bronson","money": "$0.55"},
# 			 2: {"name":"Masha","money": "$3.66"},
# 			 3: {"name":"Roscoe","money": "$1.14"}}
#
# for key in dict_data:
# 	print(key, " -->", dict_data[key])
#
# for value in dict_data:
# 	print(value)
# 	for item in dict_data.values():
# 		print(item)
# print(dict_data[1]['name'])


# for item in dict_data.values():
# 	for embed_value in item.values():
# 		print(embed_value)

# While loop
# x = 0
# while x < 10:
# 	print(f"It is working --> {x}")
# 	x = x+1
# while x<10:
# 	print(f"It is working --> {x}")
# 	if x==4:
# 		break
# 	x = x + 1