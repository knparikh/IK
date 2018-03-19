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


def  cloneTree(node):
    if node == None:
        return None

    nnode = Node(node.val)
    nnode.left = cloneTree(node.left)
    nnode.right = cloneTree(node.right)
    
    return nnode

_size = int(raw_input());
_str = raw_input()
root = createTree(_str);
clone = cloneTree(root);
printInorder(clone);
