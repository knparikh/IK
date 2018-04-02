#!/bin/python3
# Split linked list such that every other node goes into a new list
# For list with odd number of nodes, first list should be larger

import sys

class Node:
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


def alternativeSplit(pList):
    if pList == None or pList.next == None:
        return pList, None

    curr = pList
    pList2 = curr.next
    while(curr):
        curr2 = curr.next
        if curr2:
            curr.next = curr2.next
        else:
            curr.next = None

        if curr2:
            if curr2.next:
                curr2.next = curr2.next.next
            else:
                curr2.next = None

        curr = curr.next

    return pList2

def print_list(root):
    curr = root
    while(curr):
        print curr.val,
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

    print_list(head)

    head2 = alternativeSplit(head);

    print_list(head)
    print_list(head2)
    


