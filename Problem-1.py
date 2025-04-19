#Create a small calculator which performs operations such as Addition,Subtraction, Multiplication and Division using classes and objects.

class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "addition":
            return self.a + self.b
        elif self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "division":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Enter operation (Addition, Subtraction, Multiplication, Division): ")

calc = Calculator(a, b, operation)
result = calc.calculate()
print("Result:", result)
