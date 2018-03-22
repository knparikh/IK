#!/bin/python3
# Write a function which will return the number of binary search trees that
# can be constructed with n nodes.
# Catalan number Cn = (2n)!/(n+1)!*n! 
import sys
import os
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Complete the function below.
def how_many_BSTs_helper(start, end):
    if (start > end):
        return 1
    tree_count = 0
    for i in range(start,end+1):
        mid = i
        # Count how many left subtrees are possible
        left = how_many_BSTs_helper(start, mid-1)
        # Count how many right subtrees are possible
        right = how_many_BSTs_helper(mid+1, end)
        # Total combinations of both child subtrees, plus only left subtrees plus only right subtrees
        count = (left * right)
        # Total combinations of trees for this root
        tree_count += count
    return tree_count



def how_many_BSTs(n):
    if n < 2:
        return n
    return how_many_BSTs_helper(1, n)

if __name__ == "__main__":
    n = int(input())

    res = how_many_BSTs(n);
    print res
