from bank import value


def test_value_casesensitivity():
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_value_firstletter():
    assert value("How are you") == 20
    assert value("Heyy") == 20


def test_value_failure():
    assert value("maybe?") == 100
    assert value("Winner!@") == 100