#simple calculator in python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

print("Simple Calculator")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Multiplication:", multiply(x, y))
print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))