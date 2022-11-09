class Pipe:
    def __init__(self):
        self.__call_stack = []

    def __rshift__(self, next):
        self.__call_stack.append(next)
        return self

    @staticmethod
    def __apply_fn(fn, arg=None):
        if callable(fn):
            return fn(arg)()
        return fn

    @property
    def result(self):
        out = None
        for next in self.__call_stack:
            out = self.__apply_fn(next, out)
        return out

    @property
    def steps(self):
        out = None
        steps = []
        for next in self.__call_stack:
            out = self.__apply_fn(next, out)
            steps.append(out)
        return ' >> '.join(str(step) for step in steps)
