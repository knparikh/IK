# Print a path from root to node that sums to S. Use dfs_level code.
# One or more paths?
# Complete below as HW
def dfs_level(root, sum_val, path):
    if root == None:
        return

    if (sum == 0):
        print root.val
        return

    dfs_level(root.left, sum-val)
    dfs_level(root.right, sum-val)

# Tweak to problem: Print level which sums to S. Can use BFS or DFS.
