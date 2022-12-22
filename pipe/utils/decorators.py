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
