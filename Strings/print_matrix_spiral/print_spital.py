#!/bin/python3

import sys
import os

def printSpirallyHelper(matrix, start_row, start_col, num_rows, num_cols, out):
    # Print row from left to right
    i = start_row
    for j in range(start_col, start_col + num_cols, 1):
        out.append(matrix[i][j])

    if num_rows > 1:
        # Print last col up to down
        j = start_col + num_cols - 1
        for i in range(start_row+1, start_row + num_rows, 1):
            out.append(matrix[i][j])

    if num_cols > 1:
        # Print last row right to left
        i = start_row + num_rows -1
        for j in range(start_col + num_cols - 2, start_col-1, -1):
            out.append(matrix[i][j])

    if num_rows > 1 and num_cols > 1:
        # Print first col down to up
        j = start_col
        for i in range(start_row + num_rows - 2, start_row, -1):
            out.append(matrix[i][j])

    return out


def  printSpirally(matrix):
    if len(matrix) == 1:
        return ''.join(matrix[0])

    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize output array
    out = []

    #Print spiral starting at top left corner of each spiral
    i = 0
    j = 0

    while(rows > 0 and cols > 0):
        out = printSpirallyHelper(matrix, i, j, rows, cols, out)
        # Next start point is next diagonal element
        i += 1
        j += 1
        # Since we print 2 rows and 2 col in each iteration, reduce by 2.
        rows -= 2
        cols -= 2

    return ''.join(out)


    
_matrix_rows = 0
_matrix_cols = 0
_matrix_rows = int(input())
_matrix_cols = int(input())

_matrix = []
for _matrix_i in range(_matrix_rows):
    _matrix_temp = [str(_matrix_t) for _matrix_t in raw_input().strip().split(' ')]
    _matrix.append(_matrix_temp)

res = printSpirally(_matrix);
print res
