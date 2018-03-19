import heapq
import math
#Given a point P and other N points in two dimensional space, find K points out
# of N points which are nearest to P.
class point(object):
    def __init__(self, tup, p):
        self.x = tup[0]
        self.y = tup[1]
        # Since python only has min heap, and we want max heap, negate the eucl distance and store.
        self.eucl = -1 * (((self.x ** 2) - (p[0] ** 2)) + ((self.y ** 2) - (p[1] ** 2)))  # skip the sqrt for efficiency

        def __lt__(self, other):
            return self.eucl < other.eucl

def nearest_neighbors(p, neighbors, k):
    if len(neighbors) < k:
        return neighbors

    heap = [point(neighbors[i], p) for i in range(k)]
    # First insert and heapify k elements
    heapq.heapify(heap)

    for i in range(k, len(neighbors)):
        # If this neighbor's distance is less than max in heap, pop the max from heap and insert this neighbor.
        neigh = point(neighbors[i], p)
        if neigh > heap[0]:  # invert the check because its actually min_heap
            heapq.heappop(heap)
            heapq.heappush(heap, neigh)

    out = []
    # Finally return the k nearest points
    for i in range(len(heap)):
        elem = heapq.heappop(heap)
        out.append((elem.x, elem.y))

    return out


if __name__ == "__main__":
    neighbors = [(1,2),(2,3),(4,6),(7,9)]
                 # 1,   5,     44, 
    p = (2,2)
    print 'nearest_neighbors = ', nearest_neighbors(p, neighbors, 2)
    
