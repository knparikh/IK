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


def printInorder(root):
    if root == None:
        return
    printInorder(root.left)
    print root.val, 
    printInorder(root.right)

def upsideDownHelper(node, parent, parent_right_child):
    if node == None:
        return parent

    new_parent = upsideDownHelper(node.left, node, node.right)
    node.left = parent_right_child
    node.right = parent
    parent.left = None
    parent.right = None

    return new_parent

def upsideDown(root):
    if root == None:
        return None

    return upsideDownHelper(root.left, root, root.right)
    

_size = int(raw_input());
_str = raw_input()
root = createTree(_str);
new_root = upsideDown(root);
printInorder(new_root)
