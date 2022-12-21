from twttr import shorten


def test_shorten():
    """Shorten should remove all vowels in a string."""
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Hello") == "Hll"
    assert shorten("My name is Huzaifa") == "My nm s Hzf"
    assert shorten("1234qwerty") == "1234qwrty"