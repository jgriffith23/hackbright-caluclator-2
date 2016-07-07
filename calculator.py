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
        
        u0 = user_input[0]
        u1 = int(user_input[1])

        if len(user_input) == 3:
            u2 = int(user_input[2])
        #u0, u1, u2 = user_input

        result = None

        # if u0.lower() == "q":
        #     return 
        if u0 == "+":
            result = add(u1, u2)
        elif u0 == "-":
            result = subtract(u1, u2)
        elif u0 == "*":
            result = multiply(u1, u2)
        elif u0 == "/":
            result = divide(u1, u2)
        elif u0 == "square":
            result = square(u1)
        elif u0 == "cube":
            result = cube(u1)
        elif u0 == "power":
            result = power(u1, u2)
        elif u0 == "mod":
            result = mod(u1, u2)
        else:
            entered_string = raw_input("I don't understand. Please try again.\n> ")

        print result
    return

calculator()

