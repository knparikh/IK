#!/bin/python

# Reverse linked list in groups of k. Last group can have lesser elements than k.

import os
import sys

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


'''
For your reference:

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None
'''
def reverse_linked_list_in_groups_of_k(head, k):
    if head == None or head.next == None:
        return head

    curr = head
    group_num = 0

    # Find head and tail of sub-list to be reversed
    num_nodes = 0
    prev = None

    prev_group_tail = None
    while(curr):
        while((num_nodes < k) and (curr != None)):
            if num_nodes == 0:
                group_tail = curr   # first node of this group will be new tail
            temp = curr.next
            curr.next = prev
            prev = curr     # Points to new head at end of reversal
            curr = temp     # Points to next node in new group at end of reversal
            num_nodes += 1
        if group_num == 0:
            # New head of the first group becomes new head of linked list
            head = prev
        if prev_group_tail:
            prev_group_tail.next = prev
        prev_group_tail = group_tail
            
        prev = None
        num_nodes = 0
        group_num += 1

    return head


if __name__ == '__main__':
    head_size = int(input())

    head = None
    head_tail = None

    for head_i in range(head_size):
        head_item = int(input())
        head_tail = _insert_node_into_singlylinkedlist(head, head_tail, head_item)
        if head_i == 0:
            head = head_tail

    k = int(input())
    res = reverse_linked_list_in_groups_of_k(head, k)

    while res != None:
        print res.val
        res = res.next

