#!/bin/python3

import sys
import os
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.prev = None
        self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_node(self, node):
        # Record the previous and next nodes of given node
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            # Prev node's next should point to new next
            prev_node.next = next_node
        if next_node:
            # Next node's prev should point to prev
            next_node.prev = prev_node
        # update head and tail nodes if needed
        if self.head == node: # Removing head node
            self.head = next_node
        if self.tail == node: # Removing tail node
            self.tail = prev_node

    def append_node(self, node):
        if self.head == None:  # If empty list
            self.head = node
        if self.tail == None: # If empty list
            self.tail = node
        else:
            # update tail to point to new node and make new node as tail
            self.tail.next = node
            node.prev = self.tail
            # Update tail
            self.tail = node

    def remove_front_node(self):
        node = self.head
        if self.head:  # Move head
            self.head = self.head.next # New head
            if self.head:  # Set new head's prev to None
                self.head.prev = None
        if self.tail == node: # If tail was also pointing to front node, update tail
            self.tail = node.prev
        return node

class lru(object):
    def __init__(self, capacity):
        self.capacity = capacity
        # Cache containing key, value pairs
        self.cache = {}
        self.lru = DoublyLinkedList()

    def _mark_recent(self, node):
        # Move this node to end of lru as its recently used
        self.lru.remove_node(node)
        self.lru.append_node(node)

    # Remove key,value at front of lru as its least recently used
    def _evict(self):
        node = self.lru.remove_front_node()
        del self.cache[node.key]

    # Check if key exists in the cache, if it does return it. Also mark it 
    # recent by moving the key in the dll to the end
    # If key does not exist return -1
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._mark_recent(node)
            return node.value
        else:
            return -1

    # If key exists, update its value. Also mark it recent in the deq by
    # moving it to end of deq. If it does not exist, add it and append the
    # key in deq
    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._mark_recent(node)
        else:
            # Check if capacity is reached, evict 1 item from cache
            if len(self.cache.keys()) == self.capacity:
                self._evict()
            node = Node(key, value)
            self.lru.append_node(node)
            self.cache[key] = node


def implement_LRU_cache(capacity, query_type, key, value):

    lru_cache = lru(capacity)
    out = []

    for i in range(len(query_type)):
        if query_type[i] == 0:
            out.append(lru_cache.get(key[i]))
        elif query_type[i] == 1:
            lru_cache.set(key[i], value[i])

    return out



if __name__ == "__main__":
    capacity = int(input())

    query_type_cnt = 0
    query_type_cnt = int(input())
    query_type_i = 0
    query_type = []
    while query_type_i < query_type_cnt:
        query_type_item = int(input())
        query_type.append(query_type_item)
        query_type_i += 1


    key_cnt = 0
    key_cnt = int(input())
    key_i = 0
    key = []
    while key_i < key_cnt:
        key_item = int(input())
        key.append(key_item)
        key_i += 1


    value_cnt = 0
    value_cnt = int(input())
    value_i = 0
    value = []
    while value_i < value_cnt:
        value_item = int(input())
        value.append(value_item)
        value_i += 1


    res = implement_LRU_cache(capacity, query_type, key, value);
    for res_cur in res:
        print res_cur

