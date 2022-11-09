from pipe.pipe import Pipe
from pipe import utils as u

if __name__ == '__main__':
    is_not_even = u.casc(lambda x: x % 2 != 0)
    is_gt = u.casc(lambda x, y: x > y)
    is_lt = u.casc(lambda x, y: x < y)
    is_eq = u.casc(lambda x, y: x == y)

    pipe = Pipe()
    pipe \
        >> [1, 2, 3, 4] \
        >> u.filterf(u.casc(lambda x: x % 2 != 0)) \
        >> u.casc(len) \
        >> u.iff(True)(1)(2)

    print(pipe.steps)
