#simple calculator in python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Simple Calculator")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))