from plates import is_valid

def test_is_valid1():
    assert is_valid("CS50") == True

def test_is_valid5():
    assert is_valid("9") == False

def test_is_valid6():
    assert is_valid("OUTATIME") == False

def test_is_valid7():
    assert is_valid("CS50P") == False

def test_is_valid8():
    assert is_valid("CS05") == False

def test_is_valid9():
    assert is_valid("PI3.14") == False

def test_is_valid10():
    assert is_valid("12345") == False


