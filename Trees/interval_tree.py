# Used in calendar app - scheduling meeting
# Given a set of overlapping intervals support
#       Inserting a new interval    O(log n)
#       Deleting an interval        O(log n)
#       Find one overlapping interval O(log n)
#       Find k matching intervals O(klogn), but matching interval will need to be removed to prevent returning duplicates.
# Make BST based on first value of interval. Insert using first values only.
# Augment each node to contain max of second value present in its entire subtree.
def interval_traverse(root, val):
    # If interval intersects with our node, return
    # else if left subtree is null go right
    # else if val.start > left.max go right      --> OR can combine with above statement: else if left and (val.start > left.max ) go right
    # else go left

