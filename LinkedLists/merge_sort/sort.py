#!/bin/python3

# Sort singly linked list using merge sort

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


def merge(list1, list2):
    ptr1 = list1
    ptr2 = list2

    if list1 and list2:
        if list1.val < list2.val:
            new_head = list1
            ptr1 = ptr1.next
        else:
            new_head = list2
            ptr2 = ptr2.next

    elif list1:
        new_head = list1
        ptr1 = ptr1.next
    else:
        new_head = list2
        ptr2 = ptr2.next

    prev = new_head
    while (ptr1 and ptr2):
        if ptr1.val < ptr2.val:
            prev.next = ptr1
            prev = ptr1
            ptr1 = ptr1.next
        else:
            prev.next = ptr2
            prev = ptr2
            ptr2 = ptr2.next

    while ptr1:
        prev.next = ptr1
        prev = ptr1
        ptr1 = ptr1.next

    while ptr2:
        prev.next = ptr2
        prev = ptr2
        ptr2 = ptr2.next

    return new_head

def mergeSortRec(pList, length):
    if (length == 0) or (length == 1):
        return pList

    # Break in 2 halves
    count = 1
    temp = pList
    while (count < length/2):
        temp = temp.next
        count += 1

    pList2 = temp.next
    temp.next = None   #Break the list

    pList = mergeSortRec(pList, count)
    pList2 = mergeSortRec(pList2, length-count)

    pList = merge(pList, pList2)

    return pList

def  mergeSortList(pList):
    if pList == None or pList.next == None:
        return pList

    curr = pList
    length = 0
    while (curr):
        length += 1
        curr = curr.next

    pList = mergeSortRec(pList, length)
    return pList


_pList = None
_pList_tail = None
_pList_size = 0
_pList_size = int(input())
_pList_i=0
while _pList_i < _pList_size:
    _pList_item = int(input());
    if _pList_i == 0:
        _pList = _insert_node_into_singlylinkedlist(_pList, _pList_tail, _pList_item)
        _pList_tail = _pList
    else:
        _pList_tail = _insert_node_into_singlylinkedlist(_pList, _pList_tail, _pList_item)
    _pList_i += 1

res = mergeSortList(_pList);
while (res != None):
    print res.val
    res = res.next;


