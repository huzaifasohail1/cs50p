from seasons import get_min as f
import pytest

def test_input():
     with pytest.raises(TypeError):
         f(12-12-2012) == 'Invalid date'

def test_format():
    assert f(12-12-12) == 'Invalid date'
    assert f(2012-121-12) == 'Invalid date'
    assert f(229-1-1) == 'Invalid date'