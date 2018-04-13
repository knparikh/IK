#!/bin/python3

import os
import sys


#
# Complete the move_letters_to_left_side_with_minimizing_memory_writes function below.
#
def move_letters_to_left_side_with_minimizing_memory_writes(s):
    #
    # Write your code here.
    #


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    res = move_letters_to_left_side_with_minimizing_memory_writes(s)

    fptr.write(res + '\n')

    fptr.close()


