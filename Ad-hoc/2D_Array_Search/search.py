#!/bin/python3

import os
import sys


#Given sorted array of size r*c, where all numbers in array are in increasing 
# order order from left to right and top to bottom.
# https://www.youtube.com/watch?v=ZhG1M_FzxgI

# Stairs search. 
# Start from top right element, if key is less than element, go left.
# If key is greater than element go down. If equal return True.
def isPresent(arr, x):
    rows = len(arr)
    cols = len(arr[0])
    if (x > arr[rows-1][cols-1]) or (x < arr[0][0]):
        return 'not present'


    i = 0
    j = cols-1
    while(i < rows and j >= 0):
        if x < arr[i][j]:
            # x is smaller than element, go left
            j -= 1
        elif x > arr[i][j]:
            # x is greater than element, go down
            i += 1
        else:
            # x is equal
            return 'present'

    return 'not present'


if __name__ == '__main__':

    arr_rows = int(input())
    arr_columns = int(input())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    x = int(input())

    res = isPresent(arr, x)
    print res


if __name__ == '__main2__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_rows = int(input())
    arr_columns = int(input())

    arr = []

    for _ in range(arr_rows):
        arr.append(list(map(int, input().rstrip().split())))

    x = int(input())

    res = isPresent(arr, x)

    fptr.write(res + '\n')

    fptr.close()

