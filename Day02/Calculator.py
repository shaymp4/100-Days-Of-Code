def calcMenu():
    while True:
        print('''\n**CALCULATOR**
1] Add +
2] Subtract -
3] Multiply ×
4] Divide ÷
5] Exit x''')

        try:
            userChoice = int(input('Enter option (1–5): '))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if userChoice == 1:
            print("You've chosen to add.")
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            print("Result:", add(num1, num2))
        elif userChoice == 2:
            print("You've chosen to subtract.")
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            print("Result:", subtract(num1, num2))
        elif userChoice == 3:
            print("You've chosen to multiply.")
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            print("Result:", multiply(num1, num2))
        elif userChoice == 4:
            print("You've chosen to divide.")
            num1 = float(input('Enter the first number: '))
            num2 = float(input('Enter the second number: '))
            print("Result:", divide(num1, num2))
        elif userChoice == 5:
            print('Program exiting... Goodbye!')
            break
        else:
            print('INVALID CHOICE. Please try again.')

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return 'Error: Division by Zero'

calcMenu()