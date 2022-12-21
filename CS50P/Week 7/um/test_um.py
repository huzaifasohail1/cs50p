from um import count


def test_case_sensitivity():
    assert count("Hello, UM, my name is Huzaifa.") == 1
    assert count("Hello, Um, my name is Huzaifa.") == 1
    assert count("Hello, Um... um... um... my name is Huzaifa.") == 3
    assert count("Hello, uM, my name is Huzaifa.") == 1
    assert count("Hello, um, my name is Huzaifa.") == 1
    assert count("Hello, uhm, my name is Huzaifa.") == 0


def test_pos():
    assert count("um, Hello, my name is Huzaifa.") == 1
    assert count("Um my name is Huzaifa?") == 1
    assert count("my name is Huzaifa Um") == 1

