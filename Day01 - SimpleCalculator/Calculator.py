def calculator(num1, num2, operation):
    if operation.lower() == "add":
        return num1 + num2
    elif operation.lower() == "subtract":
        return num1 - num2
    elif operation.lower() == "multiply":
        return num1 * num2
    elif operation.lower() == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by Zero'
    else:
        return 'Invalid Operation.'

print(calculator(5, 0, 'divide'))