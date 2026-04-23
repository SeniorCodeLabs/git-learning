#simple calculator in python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Simple Calculator")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Division:", divide(x, y))
print("Multiplication:", multiply(x, y))
print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))