from pipe.pipe import Pipe
from pipe import utils as u


@u.casc
def hey(times):
    return 'hey!' * int(times)


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
    pipe >> 1 >> u.add(1) >> u.multiply(2) >> u.revargs(u.sub)(1) >> u.revargs(u.divide)(3) >> u.casc(lambda x: round(x)) >> u.add(3) >> hey  # noqa: E501
    assert pipe.result == 'hey!hey!hey!hey!'
    assert pipe.steps == '1 >> 2 >> 4 >> 3 >> 1.0 >> 1 >> 4 >> hey!hey!hey!hey!'  # noqa: E501


def test_pipe_3():
    pipe = Pipe()
    pipe >> [1, 2, 3] >> u.map(u.add(1)) >> u.filter(u.is_even) >> u.filter(u.casc(lambda x: x > 3))  # noqa: E501
    assert pipe.result == [4]
    assert pipe.steps == '[1, 2, 3] >> [2, 3, 4] >> [2, 4] >> [4]'


def test_pipe_4():
    pipe = Pipe()
    pipe >> 2 >> u.iff(u.is_even(pipe.result)())('even')('odd')
    assert pipe.result == 'even'
