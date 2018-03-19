#!/bin/python

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


# Check if left and right subtrees are unival.
# Also pass the count down so it is updated for leaf nodes.
# If both left and right subtree are unival, check if tree with current node
# is unival
def findSingleValueTreesRec(node, count):
    if node == None:
        return True

    isLeft = findSingleValueTreesRec(node.left, count)
    isRight = findSingleValueTreesRec(node.right, count)

    if isLeft and isRight:
        # Leaf node
        if (node.left == None) and (node.right == None):
            count[0] += 1
            return True

        # If current node val is equal to left and right vals
        if ((node.left != None) and (node.left.val == node.val) and
            (node.right != None) and (node.right.val == node.val)):
            count[0] += 1
            return True

        # if only right child exists
        if (node.left == None) and (node.right != None) and (node.right.val == node.val):
            count[0] += 1
            return True

        # if only left child exists
        if (node.right == None) and (node.left != None) and (node.left.val == node.val):
            count[0] += 1
            return True

    return False


def findSingleValueTrees(root):
    count = [0]
    findSingleValueTreesRec(root, count)
    return count[0]


_size = int(raw_input());
_str = raw_input()
root = createTree(_str);
res = findSingleValueTrees(root);
print res
