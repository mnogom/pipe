from pipe.pipe import Pipe
from pipe import utils as u

if __name__ == '__main__':
    print(f'{u.is_eq(1)(1)() = }')
    x = 5
    print(f"{u.iff(u.is_gt(x)(2)())(u.multiply(x)(10))(u.divide(x)(10))() = }")  # == 50

    x = 1
    print(f"{u.iff(u.is_gt(x)(2)())(u.multiply(x)(10))(u.divide(x)(10))() = }")  # == 0.1
    print(f"{u.iff(u.is_gt(x)(2)())(u.multiply(x))(u.divide(x))(10)() = }")  # == 0.1

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = u.filter(u.is_even)(x)()  # == [0, 2, 4, 6, 8, 10]
    x = u.map(u.casc(lambda x: int(u.power(2)(x)())))(x)()  # = [1, 4, 16, 64, 256, 1024]

    result = u.add
    for el in x:
        result = result(el)
    print(result())  # == 1365

    # ========================================
    res = 10 + (8 - 2 * 3) * (12 - 4) / 2 + 6

    res2 = u.add(10)(
        u.divide(
            u.multiply(
                u.multiply(
                    u.sub(8)(
                        u.multiply(2)(3)()
                    )()
                )(
                    u.sub(12)(4)()
                )()
            )()
        )(2)()
    )(6)()

    print(res == res2)

    # ========================================
    res = ((1 + 1) * 2 - 1) / 3 + 3

    p = Pipe()
    p >> 1 >> u.add(1) >> u.multiply(2) >> u.revargs(u.sub)(1) >> u.revargs(u.divide)(3) >> u.add(3)
    print(res == p.result)

    res = 10 + (8 - 2 * 3) * (12 - 4) / 2 + 6

    p = Pipe()
    p >> 1 >> u.add(1) >> u.revargs(u.power)(3)
    print(p.result)
