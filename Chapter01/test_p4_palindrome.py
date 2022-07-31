''' test_p4_palindrome.py '''

from p4_palindrome import is_permutation_palindrome, is_palindrome_bit_vector

test_cases = [
    ("aba", True),
    ("aab", True),
    ("abba", True),
    ("aabb", True),
    ("a-bba", True),
    ("a-bba!", True),
    ("Tact Coa", True),
    ("jhsabckuj ahjsbckj", True),
    ("Able was I ere I saw Elba", True),
    ("So patient a nurse to nurse a patient so", False),
    ("Random Words", False),
    ("Not a Palindrome", False),
    ("no x in nixon", True),
    ("azAZ", True),
]
testable_functions = [
    is_permutation_palindrome,
    is_palindrome_bit_vector,
]

def test_pal_perm():
    for func_palin in testable_functions:
        for [test_string, expected] in test_cases:
            assert func_palin(test_string) == expected
