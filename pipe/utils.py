def casc(fn):
    def accumulator(*args):
        def executor(*new_arg):
            if new_arg == ():
                return fn(*args)
            return accumulator(*args, *new_arg)

        return executor

    return accumulator


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


def mapf(fn):
    def inner(items):
        def executor():
            return [fn(item)() for item in items]

        return executor

    return inner


def filterf(fn):
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


def reverse_args(fn):
    def inner_1(arg1):
        def inner_2(arg2):
            return fn(arg2)(arg1)

        return inner_2

    return inner_1
