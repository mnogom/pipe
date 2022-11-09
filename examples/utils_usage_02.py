from pipe import utils as u


@u.casc
def fn(a, b, c):
    return (a + b) * c


if __name__ == '__main__':
    x = 1
    result = fn(x)(2)(3)()
    print(result)  # 9

    result = u.stt(0)(fn)(2)(3)(x)()
    print(result)  # 9

    result = u.reduce(u.add)([1, 2, 3])(0)()
    print(result)  # 6

    result = u.stt(0)(u.reduce)([1, 2, 3])(0)(u.add)()
    print(result)  # 6

    result = u.stt(0)(u.reducef)([1, 2, 3])(0)(u.add)()  # TypeError: reduce() takes 1 positional argument but 3 were given
    print(result)  # 6

