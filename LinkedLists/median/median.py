#!/bin/python3

import sys
import os

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None

def _insert_node_into_singlylinkedlist(head, tail, val):
    if head == None:
        head = LinkedListNode(val)
        tail = head
    else:
        node = LinkedListNode(val)
        tail.next = node
        tail = tail.next
    return tail

# NOTE random pointer given
# Find the length of the circular linked list
# Also need to find start of linked list based on ascending or descending
# order(smallest/largest element)
# Use length or slow/fast logic to find median
# To find the ascending/descending - compare 3 elements, or go to next smallest
# element from ptr, then decide.
def find_median(ptr):
    if ptr == None or ptr.next == None:
        return ptr.val

    index = 0
    slow = ptr
    fast = ptr.next
    prev = None

    #import pdb; pdb.set_trace()
    while((fast.val != ptr.val) and (fast.next.val != ptr.val)):
        prev = slow
        slow = slow.next
        fast = fast.next.next
        index += 1

    if fast.val == ptr.val:
        return slow.val
    else:
        return (prev.val + slow.val)/2




if __name__ == "__main__":
    ptr = None
    ptr_tail = None
    ptr_size = int(input())
    ptr_i = 0
    while ptr_i < ptr_size:
        ptr_item = int(input())

        ptr_tail = _insert_node_into_singlylinkedlist(ptr, ptr_tail, ptr_item)
        if ptr_i == 0:
            ptr = ptr_tail
        ptr_i += 1

    #----added manually----
    ptr_tail.next = ptr
    arbitrary_shift = int(input())
    while (arbitrary_shift > 0):
        arbitrary_shift -= 1
        ptr = ptr.next
    #--------
        
    res = find_median(ptr)
    print res


