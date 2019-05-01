#!/bin/python3

import sys

# Given denominations 1 to n, give the minimum number of coins which makes change C.
# Print all combinations.

# Recursive formulation to get min coins
# f(t, n): 0 if t = 0
#        : 1 + min(f(t-i) for i in range(1,n) where i <= t)
#
def  makeChangeRec( C,  intDenominations):
    if C == 0:
        return 0

    min_coins = sys.maxsize
    for i in range(0, len(intDenominations)):
        d = intDenominations[i]
        if d <= C:
            min_coins = min(min_coins, makeChangeRec(C-d, intDenominations))
    return 1+min_coins

# DP
# Use table of size C+1 to store number of coins for each change value. 
# Higher value of change calculations depend on lower values. So go from 1 to C
def  makeChangeDP( C, intDenominations):
    t = [[sys.maxsize for j in range(C+1)] for i in range(len(intDenominations))]

    t[0] = 0
    for i in range(1, C+1, 1):
        min_coins = sys.maxsize
        for i in range(0, len(intDenominations)):
            d = intDenominations[i]
            if d <= C:
                min_coins = min(min_coins, t[C-d])
        t[i] = min_coins+1 if min_coins < sys.max_size

    return t


def makeChangeDPSel(C, intDenominations)
    t = makeChangeDP(C, intDenominations)
    out = []
    c = C
    # Find the coin combinations
    while c > 0:
        for i in range(0, len(intDenominations)):
            next_change = c - intDenominations[i]
            exp_coins = t[c]-1
            if t[next_change] == t[c]-1:
                out.append(intDenominations[i])
                c = next_change
                break
    return ','.join(out)

def makeChange(C, intDenominations)
    t = makeChangeDP(C, intDenominations)
    return t[C]


if __name__ == "__main__":
    _C = int(input());

    _intDenominations_cnt = int(input())
    _intDenominations_i=0
    _intDenominations = []
    while _intDenominations_i < _intDenominations_cnt:
        _intDenominations_item = int(input());
        _intDenominations.append(_intDenominations_item)
        _intDenominations_i+=1

    coin_selection = makeChangeDPSel(_C, _intDenominations)
    for s in coin_selection:
        print(s)

if __name__ == "__main2__":
    _C = int(input());

    _intDenominations_cnt = int(input())
    _intDenominations_i=0
    _intDenominations = []
    while _intDenominations_i < _intDenominations_cnt:
        _intDenominations_item = int(input());
        _intDenominations.append(_intDenominations_item)
        _intDenominations_i+=1
        

    num = makeChange(_C, _intDenominations)
    print(num)

