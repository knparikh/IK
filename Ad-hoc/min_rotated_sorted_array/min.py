#!/bin/python3

import sys
import os

# Given sorted, rotated array, find the min element.
# Ex. [1 2 3 4 5] is rotated to [2 3 4 5 1]
# Apply binary search.
# If first elem is less than equal to last, array is sorted return first element
# If mid element is less than its left and right, its the minimum
# Else, search in array half which is not sorted i.e. go right if left < mid,
# else go left
def findMinimum(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        if arr[left] <= arr[right]:
            return arr[left]

        mid = int(left + (right-left)/2)
        prev = (mid + n - 1) % n
        next = (mid + 1) % n
        if (arr[mid] <= arr[prev]) and (arr[mid] <= arr[next]):
            return arr[mid]
        elif arr[mid] <= arr[right]:
            # Right half is sorted, go left
            right = mid - 1
        else:
            # Left half is sorted, go right
            left = mid + 1
    

if __name__ == '__main__':
    _arr_cnt = 0
    _arr_cnt = int(input())
    _arr_i=0
    _arr = []
    while _arr_i < _arr_cnt:
        _arr_item = int(input());
        _arr.append(_arr_item)
        _arr_i+=1
        

    res = findMinimum(_arr)
    print(str(res) + "\n")


if __name__ == '__main2__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    _arr_cnt = 0
    _arr_cnt = int(input())
    _arr_i=0
    _arr = []
    while _arr_i < _arr_cnt:
        _arr_item = int(input());
        _arr.append(_arr_item)
        _arr_i+=1
        

    res = findMinimum(_arr)
    f.write(str(res) + "\n")

    f.close()

