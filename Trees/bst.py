class node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#inorder traversal
def inorder(root):
    if root == None
        return

    if root.left:
        inorder(root.left)
    print root.val
    if root.right
        inorder(root.right)

# Insert non-duplicate values.
# Recursive solution.
# Time complexity O(log n), O(n) for skewed trees
def bst_insert(root, val):
    n = node(val, None, None)
    if root == None:
        root = n
    else:
        if root.val > val:
            root = bst_insert(root.left, val)
        else:
            root = bst_insert(root.right, val)

    return root

# 1.  If val is leaf node, delete it and update its parent
# 2. If val is non-leaf,
#      2a If it has 1 child, move child to parent
#      2b If it has 2 children
#              Find in-order successor of val node (left most child of right subtree)
#              Swap val node with in-order successor 
#              Recursively delete on right subtree
def bst_delete(root, val):


# Case 1 If right subtree, find_min(subtree)
# Case 2 Find min parent larger than val
#def inorder_successor(root, val):


#def min(root):


#def max(root):
