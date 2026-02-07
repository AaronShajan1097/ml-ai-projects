from calculator_art import logo

#Add
def add(x, y):
    return x + y

#Subtract
def subtract(x, y):
    return x - y

#Multiplication
def multiply(x, y):
    return x * y

#Division
def divide(x, y):
    return x / y

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():

    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    to_continue = True

    while to_continue:

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[f"{operation_symbol}"]
        
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_or_not = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_or_not == 'y':
            num1 = answer
        else:
            to_continue = False
            calculator()

calculator()