#!/bin/python

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

# Use a slow pointer and fast pointer which moves twice in every step.
# At end of loop, slow will point to middle node of list. In case of even size
# list, mid will be second node.
def split_list_in_middle(head):
    slow = head
    fast = head.next.next


    while(fast and fast.next != None):
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    new_head = mid.next
    mid.next = None

    return new_head

# Keep a prev pointer to point next node's next pointer to prev.
def reverse_linked_list(head):
    prev = None
    curr = head

    while(curr):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # prev points to new head of list
    return prev

# Traverse through both lists, and insert node from second list after node from first list.
def merge_linked_lists(head1, head2):
    curr1 = head1
    curr2 = head2

    while(curr1 and curr2):
        temp1 = curr1.next
        temp2 = curr2.next

        curr1.next = curr2
        curr2.next = temp1

        curr1 = temp1
        curr2 = temp2

    return head1

def print_ll(head):
    temp = head
    while (temp):
        print temp.val,
        temp = temp.next
    print '\n'


# Input 1 2 3 4 5 6
# Output 1 6 2 5 3 4
# Soln: 
# 1. Split the list in middle
# 2. Reverse 2nd list
# 3. Merge lists with alternate nodes from same list
def zip_given_linked_list(head):
    if head == None or head.next == None:
        return head

    head2 = split_list_in_middle(head)
    if head2:
        head2 = reverse_linked_list(head2)
    
    #print_ll(head)
    #print_ll(head2)

    merge_linked_lists(head, head2)

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


    res = zip_given_linked_list(head)

    while res != None:
        print res.val
        res = res.next

