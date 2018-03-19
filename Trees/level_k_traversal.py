# Given a tree, print all nodes at level k
# Assumption/Question:
#       What is level?
#       Binary tree?  Yes
#       BST? No
#       Error handling? Valid tree?
#       Balanced? 2^k nodes at each level. In this case tree is not balanced.
# Approach 1 - Store level of node in queue alongwith node. ex. store tuple (3, 1). But it needs extra space.
# Approach 2 - Use queue size for each level. After popping those many times, increase level. 
# Approach 3 - centinel method, use marker to indicate end of level - ex push #. When we reach #,pop #, increment level, push children, push #.
# For BFS above: Time complexity O(n). Space complexity O(k) 
def bfs_level_k(root):
    if root == None:

    queue = [root]
    level = 1
    queue_size = 1
    while(len(queue) > 0):
        node = queue.pop(0)
        if node != None:
            print node.val
            queue.append(node.left)
            queue.append(node.right)


def bfs_sentinel():



# Approach 4 - Using DFS - Pass k to each child with level l. 
# Start with l = k, pass k-1 to each of its children. 
# Time complexity O(n) for skewed tree.
# Space complexity - height of tree - O(log n) Average case. Worst case - skewed tree O(n)
# *******DFS is preferred because it has slight advantage in average case.
def dfs_level(root, k):
    if root == None:
        return

    if (k == 0):
        print root.val
        return

    dfs_level(root.left, k-1)
    dfs_level(root.right, k-1)

