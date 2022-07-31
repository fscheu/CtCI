''' test_p5_one_away.py '''
import time
from p5_one_away import is_one_away

test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

testable_functions = [is_one_away]

def test_one_away():

    for f in testable_functions:
        start = time.perf_counter()
        for _ in range(100):
            for [text_a, text_b, expected] in test_cases:
                assert f(text_a, text_b) == expected
        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    test_one_away()
