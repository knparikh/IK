#!/bin/python

# Convert bst to circular doubly linked list in O(n) time. left should contain 
# previous point, right should contain next pointer. Nodes should be 
# in increasing order.
# http://cslibrary.stanford.edu/109/TreeListRecursion.html

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


def BSTToLLHelper(node):
    if node == None:
        return
    global prev
    global head
    BSTToLLHelper(node.left)
    node.left = prev
    if prev:
        prev.right = node
    else:
        head = node
    prev = node
    BSTToLLHelper(node.right)



def BSTtoLL(node):
    global head
    head = None
    global prev
    prev = None
    BSTToLLHelper(node)
    temp = head
    while temp != None:
        print temp.val,
        temp = temp.right


_size = int(raw_input());

_str = raw_input()

node = createTree(_str);
BSTtoLL(node);
