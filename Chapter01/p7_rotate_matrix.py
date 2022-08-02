''' Rotate Matrix
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

Example 3x3:
0 1 2
4 5 6
7 8 9

7 4 0
8 5 1
9 6 2

'''
def rotate_matrix(old_mtx):
    ''' Rotates a matrix 90 degrees'''
    n_size = len(old_mtx)
    new_mtx = [[0] * n_size] * n_size
    for row_ix in range(0,n_size):
        new_mtx[row_ix] = [old_mtx[col_ix][row_ix] for col_ix in range(n_size-1,-1,-1)]
    return new_mtx
