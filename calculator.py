"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():
    entered_string = None

    while (entered_string != "q"):
        entered_string = raw_input(">> ")
        user_input = entered_string.split(" ")

        try:
            operation = user_input[0]
            operand1 = int(user_input[1])
        except (IndexError, ValueError):
            if (operation != "q"):
                print "Invalid input. Check that your operator and operands are correct, and try again.\n"
            continue

        if len(user_input) == 3:
            operand2 = int(user_input[2])
            
        if operation == "+":
            result = add(operand1, operand2)
        elif operation == "-":
            result = subtract(operand1, operand2)
        elif operation == "*":
            result = multiply(operand1, operand2)
        elif operation == "/":
            result = divide(operand1, operand2)
        elif operation == "square":
            result = square(operand1)
        elif operation == "cube":
            result = cube(operand1)
        elif operation == "power":
            result = power(operand1, operand2)
        elif operation == "mod":
            result = mod(operand1, operand2)
        else:
            entered_string = raw_input("I don't understand. Please try again.\n>> ")

        print result
    return

calculator()

