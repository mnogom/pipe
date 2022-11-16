def casc(fn):
    """Make default function cascade-look."""

    def accumulator(*args):

        def executor(*new_arg):
            if len(new_arg) > 1:
                raise TypeError('Too many arguments. Expect only 1')
            if new_arg == ():
                return fn(*args)
            return accumulator(*args, *new_arg)

        return executor

    return accumulator()


def revargs(fn):
    def inner_1(arg1):
        def inner_2(arg2):
            return fn(arg2)(arg1)

        return inner_2

    return inner_1


def stt(position):
    """
    Set argument to any position
    'stt(0)(fn)(2)(3)(x)' place x to 1st position in fn call.
    """

    def hidden_casc(fn):
        def accumulator(*args):
            def executor(*new_arg):
                if new_arg == ():
                    updated_args = (
                        *args[:position],
                        args[-1],
                        *args[position:-1],
                    )
                    current_fn = fn
                    for arg in updated_args:
                        current_fn = current_fn(arg)
                    return current_fn()
                return accumulator(*args, *new_arg)

            return executor

        return accumulator

    return hidden_casc


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


@casc
def map(fn, items):
    return [fn(item)() for item in items]


# def map(fn):
#     def inner(items):
#         def executor():
#             return [fn(item)() for item in items]
#
#         return executor
#
#     return inner


@casc
def filter(fn, items):
    return [item for item in items if fn(item)()]


# def filter(fn):
#     def inner(items):
#         def executor():
#             return [item for item in items if fn(item)()]
#
#         return executor
#
#     return inner


@casc
def reduce(fn, items, initial):
    result = fn(initial)
    for item in items:
        result = result(item)
    return result()


# def reduce(fn):
#     def inner_1(items):
#         def inner_2(initial):
#             result = fn(initial)
#             for item in items:
#                 result = result(item)
#             return result
#
#         return inner_2
#
#     return inner_1


def iff(condition):
    def inner_true(t):
        def inner_false(f):
            return t if condition else f

        return inner_false

    return inner_true
