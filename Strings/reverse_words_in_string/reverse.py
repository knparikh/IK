#!/bin/python3

import os
import sys

#
# Complete the reverse_ordering_of_words function below.
#
def reverse_ordering_of_words(s):




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    res = reverse_ordering_of_words(s)

    fptr.write(res + '\n')

    fptr.close()


