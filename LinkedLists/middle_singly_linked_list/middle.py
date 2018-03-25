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


#For your reference:
#LinkedListNode {
#    int val
#    LinkedListNode next
#}
# Take 2 pointers p1, p2 - p1 moves by 1, p2 moves by 2. Repeat until p2 or 
# p2.next is None. p1.next will be the middle.
def find_middle_node(head):
    if head == None or head.next == None:
        return head

    p1 = head
    p2 = head.next.next

    while ((p2 != None) and (p2.next != None)):
        p1 = p1.next
        p2 = p2.next.next

    return p1.next


if __name__ == "__main__":
    head = None
    head_tail = None
    head_size = int(input())
    head_i = 0
    while head_i < head_size:
        head_item = int(input())

        head_tail = _insert_node_into_singlylinkedlist(head, head_tail, head_item)
        if head_i == 0:
            head = head_tail
        head_i += 1


    res = find_middle_node(head);
    while (res != None):
        print res.val
        res = res.next;


