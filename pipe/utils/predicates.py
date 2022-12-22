from .decorators import casc


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
