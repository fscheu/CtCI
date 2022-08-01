''' test_p6_string_compression.py'''
from p6_string_compression import string_compression
import time

test_cases = [
    ("aabcccccaaa", "a2b1c5a3"),
    ("abcdef", "abcdef"),
    ("aabb", "aabb"),
    ("aaa", "a3"),
    ("a", "a"),
    ("", ""),
]
testable_functions = [
    string_compression,
]

def test_string_compression():
    for f in testable_functions:
        start = time.perf_counter()
        for _ in range(1000):
            for test_string, expected in test_cases:
                assert f(test_string) == expected
        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    test_string_compression()
