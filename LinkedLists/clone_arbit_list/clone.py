#!/bin/python

class Node:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None
        self.arbit = None


# Given a doubly linked list with node having one pointer next, other pointer arbit, pointing to arbitrary node. Clone the list.
# Approach 1: Uses extra space O(n) in hash table: Use hash table of existing node to new node. Go through each node, make new_node.arbit = hash[curr_node.arbit].
#             Also new_node.next = hash[old_node.next]
#
# Apprach 2: Use O(1) extra space. 
#            1. For each node, make its clone the next node.
#            2. In the second pass make the arbit of clone point to old node's arbit's next
#            3. Restore both lists by making their next point to next.next.
#
def clone_list(root):
    if root == None:
        return None

    old_node = root

    # Insert cloned nodes after each node in the linked list
    while(old_node):
        temp = old_node.next
        new_node = Node(old_node.val)
        old_node.next = new_node  # Old node1 -> New node1
        new_node.next = temp   # Old node1 -> New node1 -> Old node2
        old_node = temp

    old_node = root
    # Adjust arbit pointers
    while (old_node):
        new_node = old_node.next
        new_node.arbit = old_node.arbit.next   # Next of old node's arbit, is the cloned arbit
        old_node = new_node.next


    # Separate both lists
    old_node = root
    root2 = root.next
    while(old_node):
        new_node = old_node.next
        if new_node:
            old_node.next = new_node.next
        if new_node.next:   # For last new node, new_node.next will be None
            new_node.next = new_node.next.next
        old_node = old_node.next

    return root2

def print_list(root):
    curr = root
    print 'next:'
    while(curr):
        print curr.val,
        curr = curr.next
    print '\n'

    curr = root
    print 'arbit:'
    while(curr):
        print curr.arbit.val,
        curr = curr.next
    print '\n'


if __name__ == "__main__":
    node1 = head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node1.arbit = node3
    node2.arbit = node1
    node3.arbit = node5
    node4.arbit = node3
    node5.arbit = node2


    head2 = clone_list(head)

    print_list(head2)
    print_list(head2)
