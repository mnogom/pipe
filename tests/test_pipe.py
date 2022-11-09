from pipe.pipe import Pipe
from pipe.utils import (
    casc, mapf, filterf, add, sub, multiply, divide, reverse_args,
    iff
)


is_even = casc(lambda x: x % 2 == 0)


def hey(times):
    def executor():
        return 'hey!' * int(times)
    return executor


def test_pipe_1():
    pipe = Pipe()
    assert pipe.result is None
    assert pipe.steps == ''

    pipe >> 1
    pipe >> 2
    pipe >> 3
    assert pipe.result == 3
    assert pipe.steps == '1 >> 2 >> 3'


def test_pipe_2():
    pipe = Pipe()
    pipe >> 1 >> add(1) >> multiply(2) >> reverse_args(sub)(1) >> reverse_args(divide)(3) >> casc(lambda x: round(x)) >> add(3) >> hey  # noqa: E501
    assert pipe.result == 'hey!hey!hey!hey!'
    assert pipe.steps == '1 >> 2 >> 4 >> 3 >> 1.0 >> 1 >> 4 >> hey!hey!hey!hey!'  # noqa: E501


def test_pipe_3():
    pipe = Pipe()
    pipe >> [1, 2, 3] >> mapf(add(1)) >> filterf(is_even) >> filterf(casc(lambda x: x > 3))  # noqa: E501
    assert pipe.result == [4]
    assert pipe.steps == '[1, 2, 3] >> [2, 3, 4] >> [2, 4] >> [4]'


def test_pipe_4():
    pipe = Pipe()
    pipe >> 2 >> iff(is_even(pipe.result)())('even')('odd')
    print(pipe.result)
    # assert pipe.result == 'even'
    #
    # pipe = Pipe()
    # pipe >> 3 >> iff(is_even(pipe.result))('even')('odd')
    # assert pipe.result == 'odd'
