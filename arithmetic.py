''' Math functions for calculator '''


def add(num1,num2):
    ''' Return the sum of two arguments . '''

    return (num1 + num2)


def subtract(num1, num2):
    ''' Return the second argument subtracted form the first. '''

    return (num1 - num2)


def multiply(num1, num2):
    ''' Multiply the two arguments together '''
    return (num1 * num2)


def divide(num1, num2):
    ''' Divide the first argument by the second '''
    return (num1 / num2)

def square(num1):
    ''' Square the argument integer '''
    return (num1 ** 2)

def cube(num1):
    ''' Cube the argument '''
    return (num1 ** 3)

def power(num1, num2):
    ''' Raise the first argument to the power of the second and return the value '''
    return (num1 ** num2)

def mod(num1, num2):
    ''' Return the remainder of num1 divided by num2 '''
    return (num1 % num2)

def add_multi(num1, num2, num3):
    ''' Multiply the sum of the first two arguments by third argument '''
    return (multiply(add(num1, num2), num3))

def add_cubes(num1, num2):
    ''' The sum of both arguments' cube '''
    return (add(cube(num1), cube(num2)))







































"""Math functions for calculator."""


# def add(num1, num2):
#     """Return the sum of the two inputs."""

#     return num1 + num2


# def subtract(num1, num2):
#     """Return the second number subtracted from the first."""
#     return num1 - num2


# def multiply(num1, num2):
#     """Multiply the two inputs together."""
#     return num1 * num2

# def divide(num1, num2):
#     """Divide the first input by the second and return the result."""
#     return num1 / num2

# def square(num1):
#     """Return the square of the input."""
#     return num1 * num1

# def cube(num1):
#     """Return the cube of the input."""
#     return num1 * num1 * num1

# def power(num1, num2):
#     """Raise num1 to the power of num2 and return the value."""
#     return num1 ** num2

# def mod(num1, num2):
#     """Return the remainder of num1 / num2."""
#     return num1 % num2