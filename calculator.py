"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    user_input = input("Enter your equation or q to quit: ")
    tokens = user_input.split(" ")

    if "q" in user_input:
        print("Thanks for calculating with me. Isn't math fun!")
        #https://ascii.co.uk/art/math origin for math ASCII art
        print(""" mathemagician
 
     1+1=2    /\\
           \ c")
            ;-/\>
              ||
        """)
        break

    if len(tokens) < 2:
        print("Not enough inputs")
        continue

    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) > 3:
        num2 = tokens[2]
    else:
        num2 = 0

    if not num1.isdigit() or not num2.isdigit():
        print("Those are not number silly")
        continue

    if operator == "+":
        print(add(float(num1), float(num2)))
    elif operator == "-":
        print(subtract(float(num1), float(num2)))
    elif operator == "*":
        print(multiply(float(num1), float(num2)))
    elif operator == "/":
        print(divide(float(num1), float(num2)))
    elif operator == "square":
        print(square(float(num1)))
    elif operator == "cube":
        print(cube(float(num1)))
    elif operator == "pow":
        print(power(float(num1), float(num2)))
    elif operator == "mod":
        print(mod(float(num1), float(num2)))
    else:
        print("That's not a valid operation!")