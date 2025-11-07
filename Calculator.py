'''
Created on 05-Nov-2025

@author: HP
'''
# calculator.py

# Step 1: Show a welcome message
print("=== Simple Calculator ===")

# Step 2: Ask user to enter two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 3: Show available operations
print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Step 4: Get user's choice
choice = input("Enter your choice (1/2/3/4): ")

# Step 5: Perform the operation
if choice == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("❌ Error: Division by zero is not allowed.")
else:
    print("❌ Invalid choice! Please select 1, 2, 3, or 4.")
