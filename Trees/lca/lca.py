#!/bin/python

import sys


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

def printInorder(root):
    if root == None:
        return
    printInorder(root.left)
    print root.val, 
    printInorder(root.right)


# Complete the function below.
def  findLCA(root, n1, n2):
    if root == None:
        return None

    if (root.val == n1) or (root.val == n2):
        return root

    leftLCA = findLCA(root.left, n1, n2)
    rightLCA = findLCA(root.right, n1, n2)

    if leftLCA and rightLCA:
        return root

    if leftLCA != None:
        return leftLCA
    else:
        return rightLCA


_size = int(raw_input());


_str = raw_input()


_n1 = int(raw_input());


_n2 = int(raw_input());

root = createTree(_str);

res = findLCA(root, _n1, _n2);
print res.val;
