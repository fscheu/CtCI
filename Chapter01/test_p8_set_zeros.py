from copy import deepcopy
import time
from p8_set_zeros import set_zeros_extra_space, set_zeros

test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
testable_functions = [set_zeros,
                    set_zeros_extra_space,]

def test_zero_matrix():
    for f in testable_functions:
        start = time.perf_counter()
        for [test_matrix, expected] in test_cases:
            test_matrix = deepcopy(test_matrix)
            assert f(test_matrix) == expected
        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    test_zero_matrix()
