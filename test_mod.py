import pytest


# @mypytest.fixture
# def num_value():
#    num = 100
#    return num

@pytest.mark.great
@pytest.mark.order(2)
def test_greater(num_value):
    assert num_value > 100


@pytest.mark.great
@pytest.mark.order(3)
def test_greater_equal(num_value):
    assert num_value >= 100


@pytest.mark.others
@pytest.mark.order(1)
@pytest.mark.xfail
def test_less():
    num = 201
    assert num < 200


@pytest.mark.parametrize("num, output", [(1, 11), (2, 22)])
def test_multiplication_11(num, output):
    assert 11 * num == output


def add(a, b):
    return a + b


@pytest.mark.parametrize("a,b", [(3, 4), (4, 5), (5, 6)])
@pytest.mark.myassert
def test_add(a,b):
    assert add(a, b) in [7,9,11]


@pytest.mark.myassert
def test_not_in():
    a = "hello"
    b = "hi"
    assert b not in a


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


@pytest.mark.myassert
def test_true():
    assert is_prime(13)


@pytest.mark.myassert
def test_square():
    x = 4
    assert x * x == 16
