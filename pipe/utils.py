def casc(fn):
    def accumulator(*args):
        def executor(*new_arg):
            if new_arg == ():
                return fn(*args)
            return accumulator(*args, *new_arg)

        return executor

    return accumulator


@casc
def is_even(num):
    return num % 2 == 0


@casc
def is_gt(num_1, num_2):
    return num_1 > num_2


@casc
def is_lt(x, y):
    return x < y


@casc
def is_eq(x, y):
    return x == y


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


@casc
def concat(array: list, *args):
    result = array.copy()
    for additional_values in args:
        result.extend(additional_values)
    return result


@casc
def push(array: list, *args):
    for element in args:
        array.append(element)


def map(fn):
    def inner(items):
        def executor():
            return [fn(item)() for item in items]

        return executor

    return inner


def filter(fn):
    def inner(items):
        def executor():
            return [item for item in items if fn(item)()]

        return executor

    return inner


def iff(condition):
    def inner_true(fn):
        def inner_false(gn):
            return fn if condition else gn

        return inner_false

    return inner_true


def revargs(fn):
    def inner_1(arg1):
        def inner_2(arg2):
            return fn(arg2)(arg1)

        return inner_2

    return inner_1
