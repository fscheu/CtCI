from copy import deepcopy
from p8_set_zeros import set_zeros

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
testable_functions = [set_zeros]

def test_zero_matrix():
    for f in testable_functions:
        for [test_matrix, expected] in test_cases:
            test_matrix = deepcopy(test_matrix)
            assert f(test_matrix) == expected
