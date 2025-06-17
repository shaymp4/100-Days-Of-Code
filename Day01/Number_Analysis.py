def startAnalysis():
    num = int(input('Enter a number for analysis: '))
    print(numAnalyser(num))

def positiveOrNegative(num):
    if num >= 0:
        return f'The number {num} is positive.'
    else:
        return f'The number {num} is negative.'

def evenOrOdd(num):
    if num % 2 == 0:
        return f'The number {num} is even.'
    else:
        return f'The number {num} is odd.'

def numAnalyser(num):
    return f'{evenOrOdd(num)}\n{positiveOrNegative(num)}'

startAnalysis()