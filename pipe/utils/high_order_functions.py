from .decorators import casc


@casc
def map(fn, items):
    return [fn(item)() for item in items]


@casc
def filter(fn, items):
    return [item for item in items if fn(item)()]


@casc
def reduce(fn, items, initial):
    result = fn(initial)
    for item in items:
        result = result(item)
    return result()
