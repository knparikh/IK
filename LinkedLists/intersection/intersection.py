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

# Correct soln: Length of l1, l2 take difference. Then advance longer list by difference.
# Then when ptr1 == ptr2 , it is intersection


def find_intersection_helper(l1, l2):
    if (l1 == None) or (l2 == None):
        return None

    if l2.next == l1:
        return l1.val

    if l1.next == l2:
        return l2.val

    fast = l1
    slow = l2

    while((slow.next != fast) and (fast.next != None)):
        slow = slow.next
        fast = fast.next.next

    if slow.next == fast:
        return slow.val
    else:
        return -1


def find_intersection(l1, l2):
    ret1 = find_intersection(l1, l2)
    if ret1 == -1:
        ret1 = find_intersection(l2, l1)
    return ret1

if __name__ == "__main__":

    l1 = None
    l1_tail = None
    l1_size = int(input())
    l1_i = 0
    while l1_i < l1_size:
        l1_item = int(input())

        l1_tail = _insert_node_into_singlylinkedlist(l1, l1_tail, l1_item)
        if l1_i == 0:
            l1 = l1_tail
        l1_i += 1

    l2 = None
    l2_tail = None
    l2_size = int(input())
    l2_i = 0
    while l2_i < l2_size:
        l2_item = int(input())

        l2_tail = _insert_node_into_singlylinkedlist(l2, l2_tail, l2_item)
        if l2_i == 0:
            l2 = l2_tail
        l2_i += 1

    #--------
    merge_at = int(input())
    l1_temp = l1
    i = 0
    while i < merge_at:
        l1_temp = l1_temp.next
        i += 1
    if l2_tail == None:
        l2 = l1_temp
    else:
        l2_tail.next = l1_temp
    #--------
        
    res = find_intersection(l1, l2);
    print res


