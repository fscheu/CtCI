''' is_unique.py '''
from is_unique import is_unique


def test_unique_string():
    r = is_unique("abcdefghijklmnopq")
    assert  r is True

def test_no_unique():
    assert not is_unique("la chaucha")

