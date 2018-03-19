#!/bin/python
import sys
import os

# Given inorder and preorder traversals, reconstruct the tree
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterative Method to print the height of binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return
     
    # Create an empty queue for level order traversal
    queue = []
 
    # Enqueue Root and initialize height
    queue.append(root)
    while (1):
        q_len = len(queue)
        if q_len == 0:
            break
        while(q_len > 0):
            # Print front of queue and remove it from queue
            print queue[0].val,
            node = queue.pop(0)
 
            #Enqueue left child
            if node.left is not None:
                queue.append(node.left)
 
            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)
            q_len -= 1
        print ''

            
# Helper function which actually builds the tree.
# Constructs root with value at preOrderArray's current index.
# Find root value's index in inoder array, and divide the inorder array into left
# and right children in the tree. Recursively build the tree using the root, left and right children.
def constructTreeHelper(iInOrderArray, iPreOrderArray, inStart, inEnd):
    if inStart > inEnd:
        return None 

    root = Node(iPreOrderArray.pop(0))
    inIndex = iInOrderArray.index(root.val)

    root.left = constructTreeHelper(iInOrderArray, iPreOrderArray, inStart, inIndex-1)
    root.right = constructTreeHelper(iInOrderArray, iPreOrderArray, inIndex+1, inEnd)
    return root

def  constrctTree(iInOrderArray, iPreOrderArray):
    root = constructTreeHelper(iInOrderArray, iPreOrderArray, 0, len(iInOrderArray)-1)
    printLevelOrder(root)
    return root



_iInOrderArray_cnt = 0
_iInOrderArray_cnt = int(raw_input())
_iInOrderArray_i=0
_iInOrderArray = []
while _iInOrderArray_i < _iInOrderArray_cnt:
    _iInOrderArray_item = int(raw_input());
    _iInOrderArray.append(_iInOrderArray_item)
    _iInOrderArray_i+=1
    


_iPreOrderArray_cnt = 0
_iPreOrderArray_cnt = int(raw_input())
_iPreOrderArray_i=0
_iPreOrderArray = []
while _iPreOrderArray_i < _iPreOrderArray_cnt:
    _iPreOrderArray_item = int(raw_input());
    _iPreOrderArray.append(_iPreOrderArray_item)
    _iPreOrderArray_i+=1
    

constrctTree(_iInOrderArray, _iPreOrderArray);

