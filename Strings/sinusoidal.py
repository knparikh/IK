#!/bin/python3
# Print string sinusoidally.

import os
import sys

def print_string_helper(s, n):
    s_len = len(s)
    print_matrix = [[' ' for i in range(s_len)] for j in range(n)]

    row = 0
    down = True
    for i in range(s_len):
        if s[i] == ' ':
            print_matrix[row][i] = '~'
        else:
            print_matrix[row][i] = s[i]
        if row == n-1:
            down = False
        elif row == 0:
            down = True
        if down:
            row += 1
        else:
            row -= 1

    # Print the matrix
    for i in range(n):
        for j in range(s_len):
            print print_matrix[i][j],
        print ''

    return



def print_string_sinusoidally(s):
    s_list = list(s)
    return print_string_helper(s_list, 3);


if __name__ == '__main__':
    s = raw_input()

    print_string_sinusoidally(s)

