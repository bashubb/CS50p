import fuel
import pytest


def test_convert_raises():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")
    with pytest.raises(ValueError):
        fuel.convert("2/1")
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")

def test_convert_asserts():
    assert fuel.convert("1/1") == 100
    assert fuel.convert("0/1") == 0
    assert fuel.convert("1/2") == 50



def test_gauge_full_empty():
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(0.8) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99.5) == "F"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(0) == "E"

def test_gauge_other():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(47) == "47%"



