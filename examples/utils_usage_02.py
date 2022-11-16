from pipe import utils as u


@u.casc
def fn(a, b, c):
    return (a + b) * c


if __name__ == '__main__':
    # x = 1
    # result = fn(x)(2)(3)()
    # assert result == 9
    #
    # result = fn(2)(3)(x)()
    # assert result == 5
    #
    # result = u.stt(0)(fn)(2)(3)(x)()
    # assert result == 9
    #
    # result = u.reduce(u.add)([1, 2, 3])(0)()
    # assert result == 6
    #
    # result = u.stt(0)(u.reduce)([1, 2, 3])(0)(u.add)()
    # assert result == 6
    #
    # result = u.stt(0)(u.reducef)([1, 2, 3])(0)(u.add)()
    # assert result == 6
    #
    # assert fn(1)(2)(3)() != fn(3)(2)(1)
    # assert fn(1)(2)(3)() == u.stt(0)(fn)(2)(3)(1)()



    # TODO: Hmm...
    # print(u.add(2, 3, 4)())
    print(u.add(1, 2)())