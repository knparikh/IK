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

def  flipTree(node):
    if node == None:
        return None

    left = flipTree(node.right)
    right = flipTree(node.left)

    node.left = left
    node.right = right

    return node



_size = int(raw_input());
_str = raw_input()

root = createTree(_str);
flip = flipTree(root);
printInorder(flip)


