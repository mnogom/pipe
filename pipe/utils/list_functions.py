from .decorators import casc


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
