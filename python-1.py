class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "+":
            return self.a + self.b
        elif self.operation == "-":
            return self.a - self.b
        elif self.operation == "*":
            return self.a * self.b
        elif self.operation == "/":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

c = Calculator(a, b, operation)
print("Result is:", c.calculate())
