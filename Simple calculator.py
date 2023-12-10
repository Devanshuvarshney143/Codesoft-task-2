# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b == 0:  
        return "Cannot divide by zero"
    return a / b

# Display the calculator's options
print("Simple Calculator")
print("Operations:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user input for operation choice and numbers
operation = input("Enter operation (choose 1, 2, 3, or 4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = 0 


if operation == '1':
    result = add(num1, num2)
elif operation == '2':
    result = subtract(num1, num2)
elif operation == '3':
    result = multiply(num1, num2)
elif operation == '4':
    result = divide(num1, num2)  
else:
    print("Invalid operation")  

# Display the result
print("Result:", result)
