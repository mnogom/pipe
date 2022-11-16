"""Some special components tests."""
import pytest

from pipe import utils as u


def test_add():
    assert u.add(1)() == 1
    assert u.add(1)(2)() == 3
    assert u.add(1)(1)(1)(1)(1)() == 5


def test_power():
    assert u.power(2)(10)() == 1024


def test_sub():
    assert u.sub(5)() == 5
    assert u.sub(8)(3)() == 5
    assert u.sub(10)(1)(1)(1)(1)(1)() == 5


def test_multiply():
    assert u.multiply(1)() == 1
    assert u.multiply(5)(6)() == 30
    assert u.multiply(1)(2)(3)(4)(5)() == 120


def test_divide():
    assert u.divide(2)() == 2
    assert u.divide(4)(2)() == 2
    assert u.divide(2048)(4)(4)(4)(4)(4)() == 2


def test_reverse_args():
    assert u.revargs(u.divide)(4)(2)() == 0.5
    assert u.revargs(u.sub)(1)(4)(1)() == 2


def test_concat():
    assert u.concat([1])() == [1]
    assert u.concat([])([])() == []
    assert u.concat([1])([2])() == [1, 2]

    a = [1, 2, 3]
    b = [4, 5]
    c = [6, ]
    result = [1, 2, 3, 4, 5, 6]
    assert u.concat(a)(b)(c)() == result
    assert a != result


def test_push():
    assert u.push([])() is None

    a = [1, 2, 3]
    element_1 = 4
    element_2 = 5
    element_3 = 6
    result = [*a, element_1, element_2, element_3]
    u.push(a)(element_1)(element_2)(element_3)()
    assert a == result


def test_cascadate():
    fn_1 = u.casc(lambda x: x + 1)
    assert fn_1(2)() == 3

    fn_2 = u.casc(lambda x, y: x + y)
    assert fn_2(1)(2)() == 3

    fn_3 = u.casc(lambda *args: sum(args))
    assert fn_3(1)(2)(3)(4)(5)() == 15

    def fn_4(a, b, c, *args):
        return max(a, b, c, *args)

    assert u.casc(fn_4)(1)(2)(3)() == 3
    assert u.casc(fn_4)(1)(2)(3)(4)(5)() == 5
    with pytest.raises(TypeError) as error:
        u.casc(fn_4)(1)()
    assert 'missing' in str(error.value)
    with pytest.raises(TypeError) as error:
        u.casc(fn_4)(1, 2, 3)()
    assert 'many arguments' in str(error.value)
    with pytest.raises(TypeError) as error:
        u.casc(fn_4)(1)(2, 3)()
    assert 'many arguments' in str(error.value)

    def fn_5():
        return 5

    assert u.casc(fn_5)() == 5


def test_set_to():
    @u.casc
    def fn_1(a, b, c):
        return (a - b) * c

    def fn_2(a):
        def inner_1(b):
            def inner_2(c):
                def executor():
                    return (a - b) * c

                return executor

            return inner_2

        return inner_1

    assert fn_1(1)(2)(3)() == fn_2(1)(2)(3)()

    assert u.stt(0)(fn_1)(1)(2)(10)() == 18
    assert u.stt(1)(fn_1)(1)(2)(10)() == -18
    assert u.stt(2)(fn_1)(1)(2)(10)() == -10

    assert u.stt(0)(fn_2)(1)(2)(10)() == 18
    assert u.stt(1)(fn_2)(1)(2)(10)() == -18
    assert u.stt(2)(fn_2)(1)(2)(10)() == -10


def test_iff():
    assert u.iff(True)(1)(2)() == 1
    assert u.iff(False)(1)(2)() == 2

    assert u.stt(0)(u.iff)('even')('odd')(u.is_even(2)())() == 'even'


def test_map():
    items = [1, 2, 3]
    expected = [10, 20, 30]
    assert u.map(u.multiply(10))(items)() == expected

    expected = [2, 3, 4]
    add_1 = u.casc(lambda x: x + 1)
    assert u.map(add_1)(items)() == expected
    assert u.revargs(u.map)(items)(add_1)() == expected


def test_filter():
    items = [1, 2, 3, 4]
    is_even = u.casc(lambda x: x % 2 == 0)
    expected = [2, 4]
    assert u.filter(is_even)(items)() == expected

    expected = [1, 2]
    assert u.filter(u.is_gt(3))(items)() == expected
