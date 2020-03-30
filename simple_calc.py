class SimpleCalc:
    def __init__(self, name):
        self.name = name
    def add(self, int1, int2):
        return int1 + int2
    def subtract(self, int1, int2):
        return int1 - int2
    def multiply(self, int1, int2):
        return int1 * int2
    def divide(self, int1, int2):
        return int1 / int2

calc = SimpleCalc("first")
calc2 = SimpleCalc("second")