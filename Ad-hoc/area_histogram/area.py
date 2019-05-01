#!/bin/python3

import os
import sys


# Find Largest Rectangular Area in a Histogram, where largest rectangle can be made of contiguous bars.

# Find the rectangular areas for all bars. Push each bar on stack. When higher bar is encountered, pop last smaller 
# bar and compute area with it - left index for popped bar will be previous bar's index, 
# right index will be current index. Record the max area.
def findMaxPossibleArea(arr):
    n = len(arr)

    max_area = 0
    stack = []
    
    for i in range(n+1):
        if i == n:
            h = 0    # Special case, so that all stack elements get popped at the end with below while
        else:
            h = arr[i]
        while len(stack) > 0 and h <= arr[stack[-1]]:
            top = stack.pop()
            if len(stack) > 0:
                w = i - stack[-1] - 1
            else:
                w = i
            area = arr[top] * w
            if area > max_area:
                max_area = area
        stack.append(i)


    return max_area
     
if __name__ == '__main__':

    arr_count = int(input())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input())
        arr.append(arr_item)

    res = findMaxPossibleArea(arr)

    print(res)


if __name__ == '__main2__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input())
        arr.append(arr_item)

    res = findMaxPossibleArea(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

