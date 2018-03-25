# Swap kth (1-based) node with kth node from end.
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


'''
For your reference:

class LinkedListNode:
    def __init__(self, node_value):
        self.val = node_value
        self.next = None
'''
def swap_nodes(head, k):
    if head == None or head.next == None:
        return head

    temp = head
    count = 1
    prev_k = None
    prev_k_end = None
    k_node = head
    k_end = head

    if count == k-1:
        prev_k = head

    while (True):
        count += 1
        temp = temp.next

        if (count == k-1):
            prev_k = temp
        elif (count == k):
            k_node = temp
        elif (count == k+2):
            prev_k_end = head
        elif (count > k+2):
            prev_k_end = prev_k_end.next

        if not temp:
            break


    # Following are nodes of interest
    if prev_k:
        k_node = prev_k.next
    if prev_k_end:
        k_end = prev_k_end.next

    #print k_node.val, k_end.val
    #print prev_k.val, prev_k_end.val

    if k_end == k_node.next:  ## k_node, k_end
        k_node.next = k_end.next
        k_end.next = k_node
        if prev_k:
            prev_k.next = k_end

    elif k_node == k_end.next:   # k_end, k_node
        k_end.next = k_node.next
        k_node.next = k_end
        if prev_k_end:
            prev_k_end.next = k_node

    else:
        # First swap the next pointers of k/k-end nodes
        temp = k_node.next
        k_node.next = k_end.next
        k_end.next = temp

        # Swap nodes themselves using prevs
        if prev_k:
            prev_k.next = k_end
        if prev_k_end:
            prev_k_end.next = k_node

    if k == 1:
        head = k_end
    if k == count-1:
        head = k_node

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

    res = swap_nodes(head, k)

    while res != None:
        print(str(res.val))
        res = res.next

