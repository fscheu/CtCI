''' test_p7_rotate_matrix.py '''
from copy import deepcopy
from p7_rotate_matrix import rotate_matrix

test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]
testable_functions = [
    rotate_matrix,
]

def test_rotate_matrix():
    for f in testable_functions:
        for [test_matrix, expected] in test_cases:
            test_matrix = deepcopy(test_matrix)
            assert f(test_matrix) == expected


if __name__ == "__main__":
    test_rotate_matrix()
