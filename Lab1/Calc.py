def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number!")

num1 = get_number("a: ")
num2 = get_number("b: ")

oper = input("Enter the operation (+, -, *, /): ")

if oper == '+':
    result = num1 + num2

elif oper == '-':
    result = num1 - num2

elif oper == '*':
    result = num1 * num2

elif oper == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit()

print(f"Result: {result}")