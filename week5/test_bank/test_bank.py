from bank import value

def test_value1():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_value2():
    assert value("hi") == 20
    assert value("Hi") == 20

def test_value3():
    assert value("whats") == 100
    assert value("WWhats") == 100

