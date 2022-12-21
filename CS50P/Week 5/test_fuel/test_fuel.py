from fuel import convert, gauge
import pytest

def test_input():
    assert convert('3/4') == 75
    assert convert('1/2') == 50
    assert convert('0/10') == 0

def test_errors():
    with pytest.raises(ZeroDivisionError):
         convert('3/0')
    with pytest.raises(ValueError):
         convert('5/4')

def test_output():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(50) == '50%'