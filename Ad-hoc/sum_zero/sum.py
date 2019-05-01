#!/bin/python3

import sys
import os
from collections import defaultdict

# given a set of integers, find a contiguous subset whose sum is 0
# 0 is valid subarray. If no such subsets print nothing.
# If there are multiple such subsets, print any one.

# below finds all possible subsets
def sumZero(intArr):
    sum_map = defaultdict(list)
    idx = []
    sum = 0
    for i in range(len(intArr)):
        sum += intArr[i]
        if intArr[i] == 0 and i != 0:    # If element itself is 0
            idx.append((i,i))
        if sum == 0:          # Found subarray with zero sum, starting at index 0
            idx.append((0, i))
        if sum in sum_map:
            for st in sum_map[sum]:   # found subarray whose sum is zero, starting at index+1 at which same sum was found before
                idx.append((st+1, i))
        sum_map[sum].append(i)

    res = []
    for i in range(len(idx)):
        st, end = idx[i]
        sub = []
        for j in range(st, end+1, 1):
            sub.append(str(intArr[j]))
        res.append(','.join(sub))
    return res


if __name__ == "__main__":
    intArr_cnt = 0
    intArr_cnt = int(input())
    intArr_i = 0
    intArr = []
    while intArr_i < intArr_cnt:
        intArr_item = int(input())
        intArr.append(intArr_item)
        intArr_i += 1


    res = sumZero(intArr);
    for res_cur in res:
        print(res)

if __name__ == "__main2__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    intArr_cnt = 0
    intArr_cnt = int(input())
    intArr_i = 0
    intArr = []
    while intArr_i < intArr_cnt:
        intArr_item = int(input())
        intArr.append(intArr_item)
        intArr_i += 1


    res = sumZero(intArr);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()

