#!/bin/python

import sys

# https://articles.leetcode.com/binary-tree-post-order-traversal/

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



# Use stack for iterative post order traversal
# Post order traversal is L R C
# Keep track of prev. Start with root pushed into stack
#       While stack is not empty"
#               curr = stack.top()
#               if curr is left or right child of prev, we are going down the tree. Push left/right child if present, Else pop
#               else If prev is left child, we are coming up from left subtree, push right child if present else pop.
#               else If prev is right child, we are coming up from right subtree, pop
#               prev = current
def  postorderTraversal(root):
    if root == None:
        return

    stack = []
    out = []
    stack.append(root)
    prev = None

    while len(stack) > 0:
        curr = stack[-1]
        # Traversing the tree downwards
        if prev == None or (prev.left == curr) or (prev.right == curr):
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)
            else:
                t = stack.pop()
                out.append(t.val)
        # Traversing tree upwards from left
        elif (curr.left == prev):
            if curr.right:
                stack.append(curr.right)
            else:
                t = stack.pop()
                out.append(t.val)
        # Traversing tree upwards from left
        elif (curr.right == prev):
            t = stack.pop()
            out.append(t.val)
        prev = curr   # Record last traversed node
        
    for v in out:
        print v,


_size = int(raw_input());


_str = raw_input()
root = createTree(_str);
postorderTraversal(root);

