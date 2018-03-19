# Merge 2 bst into 1 bst. It should be balanced. Soln should be of O(m+n) complexity.
# Inorder traveral of both tree O(n+m)
# Merge 2 sorted arrays - O(n+m)
# Reconstruct bst - Take middle element of merged sorted array as root. Recurse over
# left and right half of arrays and make their root as left and right child of above root. - O(n+m)
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

# Complete the function below.
def inorder(root, arr):
    if root == None:
        return

    inorder(root.left, arr)
    arr.append(root.val)
    inorder(root.right, arr)

def bst_from_inorder(arr, start, end):
    if start > end:
        return None

    mid = start + ((end-start)/2)
    root = Node(arr[mid], None, None)
    root.left = bst_from_inorder(arr, start, mid-1)
    root.right = bst_from_inorder(arr, mid+1, end)
    return root

def merge_arrays(arr1, arr2, out):
    s1 = 0
    e1 = len(arr1)-1
    s2 = 0
    e2 = len(arr2)-1
    out = []

    while (s1 <= e1) and (s2 <= e2):
        if arr1[s1] < arr2[s2]:
            out.append(arr1[s1])
            s1 += 1
        elif arr1[s1] > arr2[s2]:
            out.append(arr2[s2])
            s2 += 1
        elif arr1[s1] == arr2[s2]:
            out.append(arr1[s1])
            out.append(arr2[s2])
            s1 += 1
            s2 += 1

    while s1 <= e1:
        #if (out[:-1] != arr1[s1]):
        out.append(arr1[s1])
        s1 += 1

    while s2 <= e2:
        #if (out[:-1] != arr2[s2]):
        out.append(arr2[s2])
        s2 += 1

    return out


def mergeTrees(node1, node2):
    arr1 = []
    arr2 = []
    arr3 = []
    inorder(node1, arr1)
    inorder(node2, arr2)

    arr3 = merge_arrays(arr1, arr2, arr3)

    root = bst_from_inorder(arr3, 0, len(arr3)-1)
    return root
    
_size1 = int(raw_input());
_str1 = raw_input()
n1 = createTree(_str1);
_size2 = int(raw_input());
_str2 = raw_input()
n2 = createTree(_str2);

res = mergeTrees(n1,n2);
printInorder(res)

