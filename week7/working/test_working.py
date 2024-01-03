import pytest
from working import convert

def test_working_true():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_working_true2():
    assert convert("8:00 PM to 12:00 AM") == "20:00 to 00:00"

def test_working_false():
    assert convert("1:00 PM to 4:00 AM") != "01:00 to 4:00"

def test_working_false2():
    assert convert("7:00 AM to 8:00 PM") != "19:00 to 08:00"


def test_value_error():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("15:00 AM to 20:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 3:60 PM")
