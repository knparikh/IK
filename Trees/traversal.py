class node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# DFS
# Time complexity O(n)
# Space complexity O(log n): (log n is height of tree) if tree is balanced.
# Worst case when tree is skewed O(n)
def pre_order_recursively(root):
    if root == None:
        return

    print root.val
    pre_order(root.left)
    pre_order(root.right)

def pre_order_iterative(root):
    if root == None:
        return

    stack = [root]
    while(len(stack) > 0):
        node = stack.pop()   # Pops the last element
        if node != None
            print node.val
            stack.append(node.right)   # Note: Insert right followed by left, so that pop returns left next time.
            stack.append(node.left)

# BFS
# Time complexity O(n)
# Space complexity O(n/2) i.e O(n) - Size of queue in worst case - last level has n/2 nodes
def bfs_iterative(root):
    if root == None:

    queue = [root]
    while(len(queue) > 0):
        node = queue.pop(0)
        if node != None:
            print node.val
            queue.append(node.left)
            queue.append(node.right)
