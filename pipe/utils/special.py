def iff(condition):
    def inner_true(t):
        def inner_false(f):
            def executor():
                return t if condition else f

            return executor

        return inner_false

    return inner_true
