#!/bin/python
#https://www.ideserve.co.in/learn/size-of-largest-bst-in-binary-tree
import sys
import os

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(data):
    def deserialize():
        val = next(vals,None)
        if val == None:
            return None
        if val == '#':
            return None
        node = Node(int(val))
        node.left = deserialize()
        node.right = deserialize()
        return node
    vals = iter(data.split())

    return deserialize()

# Recursively, find if left and right subtrees are BSTs. Return isBST, size, min, max from each subtree.
# If both left and right subtrees are BSTs, then return size as 1+lsize+rsize.
def  findLargestBSTHelper(node):
    if node == None:
        return False, 0, 0, 0

    if node.left == None and node.right == None:
        return True, 1, node.val, node.val

    lbst, lsize, lmin, lmax = findLargestBSTHelper(node.left)
    rbst, rsize, rmin, rmax = findLargestBSTHelper(node.right)

    if lbst and rbst:
        if (node.val > lmax) and (node.val < rmin):
            # BST starting at this node
            return True, 1+lsize+rsize, max(node.val, lmax), min(node.val, rmin)
        else:
            return False, max(lsize, rsize), lmin, lmax
    elif lbst:
        if node.val > lmax:
            return True, 1+lsize, node.val, lmax
        else:
            return False, lsize, lmin, lmax
    elif rbst:
        if node.val < rmin:
            return True, 1+rsize, node.val, rmax
        else:
            return False, rsize, rmin, rmax
    else:
        return False, max(lsize, rsize), lmin, lmax
        
def  findLargestBST(node):
    if node == None:
        return 0

    isBST, size, minv, maxv = findLargestBSTHelper(node)
    return size



_size = int(raw_input());
_str = raw_input()
root = createTree(_str);
res = findLargestBST(root);
print res
