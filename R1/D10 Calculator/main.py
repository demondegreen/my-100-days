#Calculator
from art import logo
from replit import clear
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
}

def calculator():
    clear()
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print (symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start fresh.: ") == "y":
            num1 = result
        else:
            should_continue = False
            calculator()

calculator() # big bang
