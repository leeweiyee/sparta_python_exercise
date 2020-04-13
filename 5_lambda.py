# Lambda function
# A lambda function is a way of defining a function in a single line of code
# e.g. the following lambda function multiplies a number by 2 and then adds 3:
mylambda = lambda x: (x * 2) + 3

# e.g. this lambda function takes in a string, assigns it to the temporary variable x, and then converts it into lowercase:
stringlambda = lambda x: x.lower()
print(stringlambda("Oh Hi Mark!"))
# output:
# > "oh hi mark!"

# e.g. this function returns the first and last letters of a string:
mylambda = lambda x: x[0] + x[-1]

# e.g. this function will convert the number of hours into time-and-a-half hours using an if statement:
def myfunction(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x
# lambda function:
myfunction = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x
# lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]

# get_last_name  takes a string with someone’s first and last name and returns their last name:
get_last_name = lambda x: x.split(' ')[-1]

# addition function method:
def add(num1,num2):
    return num1+num2
# print(add(23,45))

# lambda addition function:
addition = lambda num1, num2:num1 + num2
# print(addition(23,45))

savings = [234,567,674,78]
bonus = list(map(lambda x: x * 1.1, savings))
print(bonus)

