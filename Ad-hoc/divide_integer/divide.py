#!/bin/python3

import os
import sys


# Subtract b from a till remainder becomes less than b. Count how many times we subtracted.
def divide(a, b):
    sign = 1
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        sign = -1
        if a < 0:
            a = a * sign
        else:
            b = b * sign

    if a < 0 and b < 0:
        a = a * -1
        b = b * -1

    if a == 0:
        return 0

    q = 0
    rem = a
    while (rem >= b):
        rem -= b
        q += 1

    return q * sign


if __name__ == '__main__':

    a = int(input())

    b = int(input())

    res = divide(a, b)

    print(res)

if __name__ == '__main2__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input())

    b = int(input())

    res = divide(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

