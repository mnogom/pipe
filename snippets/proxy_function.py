class Proxy:
    def __init__(self, fn):
        self.fn = fn
        self.args = []
        self.kwargs = {}

    def __call__(self, *args, **kwargs):
        if not args and not kwargs:
            return self.fn(*self.args, **self.kwargs)
        if len(args) + len(kwargs) > 1:
            raise TypeError('Too many args')
        if args:
            self.args.append(*args)
        if kwargs:
            self.kwargs.update(kwargs)
        return self

    def get_args(self):
        return self.args

    def get_kwargs(self):
        return self.kwargs


def proxy(fn):
    return Proxy(fn)


if __name__ == '__main__':
    @proxy
    def add(a, b):
        return a + b

    c = add(1)(2)
    print(c.get_args(), c.get_kwargs())
    print(c())

    print(add(1)(2)())
