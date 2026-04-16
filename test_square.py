from square import get_square

def test_positive():
    x = 2
    expected = 4
    res = get_square(x)
    assert res == expected
def test_one():
    x = 1
    expected = 1
    res = get_square(x)
    assert res == expected
def test_negative():
    x = -3
    expected = 9
    res = get_square(x)
    assert res == expected
def test_zero():
    x = 0
    expected = 0
    res = get_square(x)
    assert res == expected
def test_float():
    x = 2.5
    expected = 6.25
    res = get_square(x)
    assert res == expected

    