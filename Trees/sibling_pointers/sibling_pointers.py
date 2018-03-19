#!/bin/python
# Given a binary tree, populate its sibling pointers
# BFS using stack

import sys

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.nextRight = None

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
    if root.nextRight:
        print root.nextRight.val
    else:
        print 'None'
    printInorder(root.right)

# Push each node in a queue. While queue is not empty, pop node. 
# If prev node was None, then push a 'None' followed by
# its left and right child in the queue. Connect node's nextRight to 
# next in stack. Repeat above.
def populate_sibling(root):
    if root == None:
        return None

    #print root.val, root.left, root.right
    queue = [root]
    prev = None

    while (len(queue) > 0):
        curr = queue.pop(0)
        if curr != None:
            if prev == None:
                # Start of a new level
                queue.append(None)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            curr.nextRight = queue[0]
        prev = curr
    return root

# TODO O(1) solution


_size = int(raw_input());
_str = raw_input()

root = createTree(_str);
root = populate_sibling(root);
printInorder(root)


