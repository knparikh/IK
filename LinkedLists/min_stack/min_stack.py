#!/bin/python

import os
import sys

class MinStack(object):
    def __init__(self):
        self.vals = []
        self.min_vals = []

    def push(self, val):
        self.vals.append(val)
        if self.min_vals:
            if val < self.min_vals[-1]:
                self.min_vals.append(val)
        else:
            # first val is always min
            self.min_vals.append(val)

    def pop(self):
        val = None
        if self.vals:
            val = self.vals.pop()
            if self.min_vals and val == self.min_vals[-1]:
                self.min_vals.pop() # Remove from min_vals
        return val

    def min_val(self):
        if len(self.min_vals):
            return self.min_vals[-1]
        return -1



def min_stack(operations):
    out = []
    stack = MinStack()

    for val in operations:
        if val == -1:
            stack.pop()
        elif val == 0:
            out.append(stack.min_val())
        else:
            stack.push(val)

    return out

if __name__ == '__main__':

    operations_size = int(input())

    operations = []
    for _ in range(operations_size):
        operations_item = int(input())
        operations.append(operations_item)


    res = min_stack(operations)

    print('\n'.join(map(str, res)))


