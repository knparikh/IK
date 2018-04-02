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

def length(pList):
    l = 0
    curr = pList
    while (curr):
        l += 1
        curr = curr.next

    return l

def  addNumbers(l1, l2):
    len1 = length(l1)
    len2 = length(l2)

    new_head = l1
    if len1 < len2:
        new_head = l2

    curr1 = l1
    curr2 = l2
    res = new_head
    carry = 0
    prev = None

    while (curr1 and curr2):
        sum = (curr1.val + curr2.val + carry)
        if sum > 9:
            carry = 1
        else:
            carry = 0
        res.val = sum % 10
        prev = res
        res = res.next
        curr1 = curr1.next
        curr2 = curr2.next

    while(curr1):
        sum = carry + curr1.val
        if sum > 9:
            carry = 1
        else:
            carry = 0

        res.val = sum % 10
        prev = res
        res = res.next
        curr1 = curr1.next
        
    while(curr2):
        sum = carry + curr2.val
        if sum > 9:
            carry = 1
        else:
            carry = 0

        res.val = sum % 10
        prev = res
        res = res.next
        curr2 = curr2.next

    if carry:
        prev.next = LinkedListNode(carry)

    return new_head

_l1 = None
_l1_tail = None
_l1_size = 0
_l1_size = int(input())
_l1_i=0
while _l1_i < _l1_size:
    _l1_item = int(input());
    if _l1_i == 0:
        _l1 = _insert_node_into_singlylinkedlist(_l1, _l1_tail, _l1_item)
        _l1_tail = _l1
    else:
        _l1_tail = _insert_node_into_singlylinkedlist(_l1, _l1_tail, _l1_item)
    _l1_i += 1


_l2 = None
_l2_tail = None
_l2_size = 0
_l2_size = int(input())
_l2_i=0
while _l2_i < _l2_size:
    _l2_item = int(input());
    if _l2_i == 0:
        _l2 = _insert_node_into_singlylinkedlist(_l2, _l2_tail, _l2_item)
        _l2_tail = _l2
    else:
        _l2_tail = _insert_node_into_singlylinkedlist(_l2, _l2_tail, _l2_item)
    _l2_i += 1

res = addNumbers(_l1, _l2)
while (res != None):
    print(res.val)
    res = res.next;



