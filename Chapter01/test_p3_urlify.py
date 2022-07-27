''' test_p3_urlify.py'''
from p3_urlify import urlify

def test_a():
    a_url = "Mr John Smith   "
    assert urlify(a_url) == "Mr%20John%20Smith"