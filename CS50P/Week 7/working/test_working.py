from working import convert
import pytest

def test_format():
    with pytest.raises(ValueError):
         convert('09:00 AM - 7:00 PM')
    with pytest.raises(ValueError):
         convert('9:00AM to 7:00PM')

def test_convert():
    assert convert('08:00 AM to 4:00 PM') == '08:00 to 16:00'
    assert convert('01:35 AM to 10:59 AM') == '01:35 to 10:59'

def test_range():
    with pytest.raises(ValueError):
         convert('10:00 AM to 18:00 PM')
    with pytest.raises(ValueError):
         convert('10:60 AM to 08:00 PM')

if __name__ == '__main__':
    main()