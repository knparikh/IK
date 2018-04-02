#!/bin/python3

# Implement a stack with push, pop, inc(e, k) operations
# inc (e,k) - Add k to each of bottom e elements
import sys

class Stack(object):
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if len(self.arr):
            return self.arr.pop()

    def inc(self, e, k):
        count = min(len(self.arr), e)
        for i in range(count):
            self.arr[i] += k

    def peek(self):
        if len(self.arr):
            return self.arr[-1]
        else:
            return 'EMPTY'

def superStack(operations):
    s = Stack()
    for o in operations:
        op = o.split(' ')
        if op[0] == 'push':
            s.push(int(op[1]))
            print(s.peek())
        elif op[0] == 'pop':
            s.pop()
            print(s.peek())
        elif op[0] == 'inc':
            s.inc(int(op[1]), int(op[2]))
            print(s.peek())
        

if __name__ == "__main__":
    operations_cnt = 0
    operations_cnt = int(input())
    operations_i = 0
    operations = []
    while operations_i < operations_cnt:
        try:
            operations_item = str(input())
        except:
            operations_item = None
        operations.append(operations_item)
        operations_i += 1


    res = superStack(operations);
    

