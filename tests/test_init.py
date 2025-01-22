from python_package_template import hello, add, multiply


def test_hello():
    assert hello("World!") == "Hello World!"


def test_add():
    assert add(1, 2) == 3


def test_multiply():
    assert multiply(2.5, 2) == 5
