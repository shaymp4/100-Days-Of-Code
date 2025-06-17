def calculator(num1, num2, operation):
    operation = operation.lower()
    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by Zero'
    else:
        return 'Invalid Operation.'

print(calculator(5,6,'DIVIDE'))