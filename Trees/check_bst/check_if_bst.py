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


# Complete the function below.
def isBSTInorder(node, newprev):
    if node == None:
        return True

    left = isBSTInorder(node.left, newprev)

    if (node.val <= newprev[0]):
        return False
    newprev[0] = node.val

    right = isBSTInorder(node.right, newprev)
    return left and right

    
# Method1 Use inorder traversal. Send the previous value to the inorder function,
# so when it is visiting the center node, it can compare with prev value and return False
# if node's value is greater or equal to previous value.
def  isBST(root):
    newprev = [None]
    if root == None:
        return True
    return isBSTInorder(root, newprev)

def inorder(root, out):
    if root == None:
        return

    inorder(root.left, out)
    out.append(root.val)
    inorder(root.right, out)

# Use inorder traveral, and keep output in array.
# Check if output array is sorted or not.
def isBST2(root):
    if root == None:
        return True

    out = []
    inorder(root, out)
    print out
    for i in range(len(out)):
        if (i > 0) and out[i] <= out[i-1]:
            return False
    return True


f = open(os.environ['OUTPUT_PATH'], 'w')
    

_size = int(raw_input());


_str = raw_input()
root = createTree(_str);
res = isBST(root);
f.write(str(int(res)) + "\n")

f.close()
