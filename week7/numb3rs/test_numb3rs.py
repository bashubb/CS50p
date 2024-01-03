from numb3rs import validate


def test_validate_true1():
    assert validate("1.2.3.4") == True

def test_validate_true2():
    assert validate("127.0.0.1") == True

def test_validate_true3():
    assert validate("255.255.255.0") == True


def test_validate_false1():
    assert validate("275.22.22.0") == False

def test_validate_false2():
    assert validate("-1.22.33.22") == False

def test_validate_false3():
    assert validate("abc.2.3.4") == False

def test_validate_false4():
    assert validate("?.$.:.+") == False

def test_validate_false4():
    assert validate("cat") == False


def test_validate_false5():
    assert validate("200.256.256.256") == False


