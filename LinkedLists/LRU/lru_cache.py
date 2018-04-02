#!/bin/python3

import sys
import os

from collections import OrderedDict
class lru(object):
    def __init__(self, capacity):
        self.capacity = capacity
        # Cache containing key, value pairs
        self.cache = {}
        self.lru = OrderedDict()

    def _mark_recent(self, key):
        # Move this key to end of lru as its recently used
        del self.lru[key]
        self.lru[key] = 1

    # Remove key,value at front of lru as its least recently used
    def _evict(self):
        key,_ = self.lru.popitem(last=False)
        del self.cache[key]

    # Check if key exists in the cache, if it does return it. Also mark it 
    # recent by moving the key in the deq to the end
    # If key does not exist return -1
    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self._mark_recent(key)
            return value
        else:
            return -1

    # If key exists, update its value. Also mark it recent in the deq by
    # moving it to end of deq. If it does not exist, add it and append the
    # key in deq
    def set(self, key, value):
        if key in self.cache:
            self._mark_recent(key)
            # Update the new deq index in the cache
            self.cache[key] = value
        else:
            # Check if capacity is reached, evict 1 item from cache
            if len(self.cache.keys()) == self.capacity:
                self._evict()
            self.lru[key] = 1
            self.cache[key] = value


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
    f = open(os.environ['OUTPUT_PATH'], 'w')

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

