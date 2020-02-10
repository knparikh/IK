# Min-heap
# Children of i at 2i+1, 21+2
# Parent of i -> fl(i-1/2)
# Always perform operations with last element of array
# Delete min element extract_min - swap top with last, delete last, then heapify starting from root down
#       compare parent to children -> swap if parent > child, then go down swapped path
# Insert element in heap - insert at end of array -> heapify from last to root
#        compare child to parent, swap if parent > child
# Insert 1 element - log n
# Insert n elements - n * log n
# Leaf nodes are n/2 -> at end of array
# For build_heap - skip last half of array (since leaf nodes are in last half.)
#       Then insert items and heapify
class Heap(object):
    def __init__(self, inp):
        self.size = len(inp)
        self.capacity = 2 * self.size
        # Create array twice input size
        self.arr = [0 for i in range(self.capacity)]
        for i in range(self.size):
            self.arr[i] = inp[i]
        mid = len(inp)-1/2  # ????
        for i in range(mid, -1, -1):  # Heapify first half of array
            self.heapify(i)

    def extract_min(self):
        min = self.arr[0]
        # Exchange with last element of arr and heapify top-down
        temp = self.arr[self.size-1]
        self.arr[self.size-1] = self.arr[0]
        self.arr[0] = temp

        # Reduce the array size by 1
        self.size = self.size-1
        self.heapify(0)
        return min

    # Not used for heapsort in our case
    def insert(self, val):
        # If size has reached capacity, then re-allocate array
        #if (self.size) == self.capacity):
        #    self.reallocate(self.arr)
        # Append element at end, and reverse-heapify
        self.arr[self.size] = val
        self.size = self.size+1

        self.reverse_heapify(self.size-1)

    def reverse_heapify(self, i):
        while((i-1)/2 > 0):
            j = (i-1)/2
            if (self.arr[i] < self.arr[j]):
                # Exchange with parent
                temp = self.arr[i]
                self.arr[i] = self.arr[j]
                self.arr[j] = temp
                i = j
            else:
                break

    def heapify(self, i):
        while (((2*i) + 1) < self.size):  # While left child exists
            j = (2*i) + 1
            # Find the smaller of the two children
            if((j < self.size-1) and (self.arr[j] > self.arr[j+1])):
                j = j + 1
            # Exchange parent and child if child is smaller
            if (self.arr[i] > self.arr[j]):
                temp = self.arr[i]
                self.arr[i] = self.arr[j]
                self.arr[j] = temp
                i = j
            else:
                break


def heap_sort(inp):
    h = Heap(inp)

    for i in range(len(inp)):
        h.extract_min()

    # Read elements in reverse order to get sorted array
    inp = [h.arr[i] for i in range(len(inp)-1, -1, -1)]

    return inp

if __name__ == "__main__":
    inp = [8,7,6,5,4,3,2,1]
    print 'heap_sort = ', heap_sort(inp)
