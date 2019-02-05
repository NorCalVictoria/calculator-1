''' A prefix-notation calculator '''

from arithmetic import *

while True:
    user_input = input("  >  ") 
    tokens = user_input.split(" ")

    if "q" in tokens:
        print(" Exiting ... ")
        break

    elif len(tokens) < 2:
        print("Need more inputs.")
        continue

    operator = tokens[0]
    num1 = tokens[1]

    if len (tokens) < 3:
        num2 = "0"

    else: 
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]




    # variable for result of function
    # location of result

    result = None

    if not num1.isdigit() or not num2.isdigit():
        print("Double check that they are numbers")
        continue

    # cast what is passed into the argument and convert into an integer.
    # edge-case float (use on all results)

    elif operator == " + " :
        resuilt = add(float(num1), float(num2))

    elif operator == " - " :
        result = subtract(float(num1), float(num2))

    elif operator = " * " :
        result multiply(float(num1), float(num2))

    elif operator == " / " :
        result = divide(float(num1), float(num2))

    elif operator == "square" :
        result = square(float(num1))

    elif operator == "cube" :
        result = cube(float(num1))

    elif operator "pow" :
        result power(float(num1), float(num2))

    elif operator == "mod" :
        result = mod(float(num1), float(num2))

    elif operator == "x+" :
        result = add_mult(float(num1), float(num2), float(num3))

    elif operator == "cubes+" :
        result add_cubes(float(num1), float(num2))
        
    else:
        result = "Please give an operator and two integers"

    print(result)
