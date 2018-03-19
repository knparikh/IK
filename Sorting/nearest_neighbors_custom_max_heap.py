#Given a point P and other N points in two dimensional space, find K points out
# of N points which are nearest to P.

class max_heap(object):
    def __init__(self):
        self.arr = []
        
    def get_size(self):
        return len(self.arr)

    def insert(self, elem):
        self.arr.append(elem)
        if self.get_size() > 1:
            self.reverse_heapify(self.get_size()-1)
        
    def extract(self):
        max_elem = self.arr[0]
        # Swap with last elem and pop
        self.arr[0], self.arr[self.get_size()-1] = self.arr[self.get_size()-1], self.arr[0]
        self.arr.pop()
        self.heapify(0)
        return max_elem
        
    def heapify(self, index):
        # Find the greater of the 2 children
        j = (2 * index) + 1
        while (j <= self.get_size()-1):
            if (j < self.get_size()-1) and (self.arr[j] < self.arr[j+1]):
                j = j + 1
            if (self.arr[index] < self.arr[j]):
                # Child is greater, swap
                self.arr[index], self.arr[j] = self.arr[j], self.arr[index]
            else:
                break
            
    def reverse_heapify(self, index):
        print 'reverse_heapify ', index

        while ((index-1)//2 >= 0):
            parent = (index-1)//2
            if self.arr[parent] < self.arr[index]:
               # Parent is smaller, swap
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
            else:
                break


class point(object):
    def __init__(self, tup, p):
        self.x = tup[0]
        self.y = tup[1]
        self.eucl = (((self.x ** 2) - (p[0] ** 2)) + ((self.y ** 2) - (p[1] ** 2)))  # skip the sqrt for efficiency

        def __lt__(self, other):
            return self.eucl < other.eucl

def nearest_neighbors(p, neighbors, k):
    if len(neighbors) < k:
        return neighbors

    heap = max_heap()
    # Insert first k neighbors in heap
    for i in range(k):
        heap.insert(point(neighbors[i], p))

    for i in range(k, len(neighbors)):
        # If this neighbor's distance is less than max in heap, pop the max from heap and insert this neighbor.
        neigh = point(neighbors[i], p)
        if neigh < heap.arr[0]:
            heap.extract()
            heap.insert(neigh)

    out = []
    # Finally return the k nearest points
    for i in range(len(heap.arr)):
        elem = heap.extract()
        out.append((elem.x, elem.y))

    return out


if __name__ == "__main__":
    neighbors = [(2,2), (1,2),(2,3),(4,6),(7,9)]
                 # 0,     1,   5,     44, 
    p = (2,2)
    print 'nearest_neighbors = ', nearest_neighbors(p, neighbors, 2)
    
