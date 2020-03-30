# Lambda function

def add(num1,num2):
    return num1+num2
# print(add(23,45))

addition = lambda num1, num2:num1 + num2
print(addition(23,45))

savings = [234,567,674,78]
bonus = list(map(lambda x: x * 1.1, savings))
print(bonus)