class Stack(object):
    def __init__(self):
        self.arr = []
        self.min_arr = []

    def push(self, val):
        if (len(self.min_arr)):
            if val <= self.min_arr[0]:
               self.min_arr.append(val)
        else:
            self.min_arr.append(val)
        self.arr.append(val)

    def pop(self):
        if len(self.arr):
            pop_val = self.arr.pop()
            if (len(self.min_arr)) and pop_val == self.min_arr[0]:
                self.min_arr.pop()
            return pop_val
        else:
            return IndexError


    def peek(self):
        return sef.arr[0]

    def min(self):
        return self.min_arr[0]


