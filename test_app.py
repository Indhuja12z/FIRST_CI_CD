from app import add, multiply

def test_add():
    assert add(10, 20) == 30

def test_add_zero():
    assert add(5, 0) == 5

def test_multiply():
    assert multiply(10, 20) == 200
