''' set_zeros.py
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
'''
from copy import deepcopy

def set_zeros(old_mtx):
    n_rows = len(old_mtx)
    n_cols = len(old_mtx[0])

    res_mtx = deepcopy(old_mtx)
    for row_ix in range(n_rows):
        for col_ix in range(n_cols):
            if old_mtx[row_ix][col_ix] == 0:
                # set the row in 0
                res_mtx[row_ix] = [0] * n_cols

                # set the col in 0
                for row_ix_res in range(n_rows):
                    res_mtx[row_ix_res][col_ix] = 0
    return res_mtx
