from .decorators import casc


@casc
def add(*args):
    return sum(args)


@casc
def sub(minuend, *args):
    result = minuend
    for term in args:
        result -= term
    return result


@casc
def power(number, power):
    return number ** power


@casc
def multiply(multiplier, *args):
    result = multiplier
    for multiplicand in args:
        result *= multiplicand
    return result


@casc
def divide(dividend, *args):
    result = dividend
    for divisor in args:
        result /= divisor
    return result
