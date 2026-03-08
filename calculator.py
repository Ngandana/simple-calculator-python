print("Simple Calculator")

# Ask for the first number
num1 = float(input("Enter first number: "))

# Ask for the operator
operator = input("Enter operator (+, -, *, /): ")

# Ask for the second number
num2 = float(input("Enter second number: "))

# Perform the calculation
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

else:
    print("Invalid operator")
    exit()

# Display the result
print("Result:", result)