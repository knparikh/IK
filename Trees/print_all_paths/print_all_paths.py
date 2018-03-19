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

# Visit each node, append its val to path.
# If reached a leaf node, print the path
# If left child, print paths for left subtree
# If right child, print paths for right subtree
# Pop current node from path as its already visited and return.
def _print_paths(node, path):
    if node == None:
        return

    path.append(node.val)
    if node.left == None and node.right == None:
        # Leaf node, print path
        print ' '.join(map(str, path))

    if node.left != None:
        _print_paths(node.left, path)

    if node.right != None:
        _print_paths(node.right, path)

    # Remove last node
    path.pop()

    return

def  printAllPaths(root):
    path = []
    _print_paths(root, path)



_size = int(raw_input());


_str = raw_input()
root = createTree(_str);
printAllPaths(root);
