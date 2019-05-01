#!/bin/python3

import os
import sys

# Given array of n intervals, merge the overlapping intervals.
def partition(inp, st, end):
    pivot = inp[st][0]
    left = st
    right = end
    i = st

    while (left <= right):
        while left <= right and inp[left][0] <= pivot:
            left += 1

        while left <= right and inp[right][0] > pivot:
            right -= 1


            if left < right:
                # Swap
                inp[left], inp[right] = inp[right], inp[left]


    # Swap pivot with right
    inp[st], inp[right] = inp[right], inp[st]

    return right

def quick_sort(inputArray, st, end):
    if st >= end:
        return

    pivot = partition(inputArray, st, end)
    quick_sort(inputArray, st, pivot)
    quick_sort(inputArray, pivot+1, end)


def getMergedIntervals(inputArray):
    if len(inputArray) <= 1:
        return inputArray

    merged = []

    quick_sort(inputArray, 0, len(inputArray)-1)

    # Now merge consecutive intervals as follows:
    # Compare 2 consecutive intervals, if int2's st is <= int1's end
    # merged_interval = int1_st, max(int1_end, int2_end)
    merged.append(inputArray[0][:])
    for i in range(1, len(inputArray), 1):
        int1 = merged[-1]
        int2 = inputArray[i]

        if int2[0] <= int1[1]:
            merged[-1][1] = max(merged[-1][1], int2[1])
        else:
            merged.append(inputArray[i][:])

    #print(merged)
    return merged

if __name__ == '__main__':

    inputArray_rows = int(input())
    inputArray_columns = int(input())

    inputArray = []

    for _ in range(inputArray_rows):
        inputArray.append(list(map(int, input().rstrip().split())))

    res = getMergedIntervals(inputArray)

    print('\n'.join([' '.join(map(str, x)) for x in res]))


if __name__ == '__main2__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    inputArray_rows = int(input())
    inputArray_columns = int(input())

    inputArray = []

    for _ in range(inputArray_rows):
        inputArray.append(list(map(int, input().rstrip().split())))

    res = getMergedIntervals(inputArray)

    f.write('\n'.join([' '.join(map(str, x)) for x in res]))
    f.write('\n')

    f.close()

