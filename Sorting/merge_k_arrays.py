class heap_elem(object):
    def __init__(self, val, pos, arr_id):
       self.val = val
       self.pos = pos
       self.arr_id = arr_id

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
        while (((2 * index) + 1) <= self.get_size()-1):
            j = (2 * index) + 1
            if (j < self.get_size()-1) and (self.arr[j].val < self.arr[j+1].val):
                j = j + 1
            if (self.arr[index].val < self.arr[j].val):
                # Child is greater, swap
                self.arr[index], self.arr[j] = self.arr[j], self.arr[index]
                j = (2 * index) + 1
            else:
                break
            
    def reverse_heapify(self, index):
        #print 'reverse_heapify ', index

        while ((index-1)//2 >= 0):
            parent = (index-1)//2
            if self.arr[parent].val < self.arr[index].val:
               # Parent is smaller, swap
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = (index-1)//2
            else:
                break

        #print 'after reverse_heapify ', len(self.arr)
        #for elem in self.arr:
        #    print elem.val


class min_heap(object):
    def __init__(self):
        self.arr = []
        
    def get_size(self):
        return len(self.arr)

    def insert(self, elem):
        self.arr.append(elem)
        if self.get_size() > 1:
            self.reverse_heapify(self.get_size()-1)
        #print 'after reverse_heapify '
        #for elem in self.arr:
        #    print elem.val
        
    def extract(self):
        min_elem = self.arr[0]
        # Swap with last elem and pop
        self.arr[0], self.arr[self.get_size()-1] = self.arr[self.get_size()-1], self.arr[0]
        self.arr.pop()
        self.heapify(0)
        return min_elem
        
    def heapify(self, index):
        # Find the lesser of the 2 children
        j = (2 * index) + 1
        while ( ((2 * index) + 1) <= self.get_size()-1):
            j = (2 * index) + 1
            if (j < self.get_size()-1) and (self.arr[j].val > self.arr[j+1].val):
                j = j + 1
            if (self.arr[index].val > self.arr[j].val):
                # Parent is greater, swap
                self.arr[index], self.arr[j] = self.arr[j], self.arr[index]
            else:
                break
        #print 'after heapify '
        #for elem in self.arr:
        #    print elem.val
            
    def reverse_heapify(self, index):
        #print 'reverse_heapify ', index

        while ((index-1)//2 >= 0):
            parent = (index-1)//2
            if self.arr[parent].val > self.arr[index].val:
               # Parent is greater, swap
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = (index-1)//2
            else:
                break

        #print 'after reverse_heapify '
        #for elem in self.arr:
        #    print elem.val

def mergeArrays(arr):

    k = len(arr)
    if k <= 1:
        return
    n = len(arr[0])

    h = None
    # Find if arrays are sorted in ascending or descending order
    sort = 'min'
    if n > 1:
        for i in range(k):
            if arr[i][0] > arr[i][n-1]:
                sort = 'max'
                break
            elif arr[i][0] < arr[i][n-1]:
                sort = 'min'
                break
            else:
                j = 0
                m = len(arr[i])-1
                while (j <= m):
                    if [arr[i][j] < arr[i][m]]:
                        sort = 'min'
                        break
                    elif [arr[i][j] > arr[i][m]]:
                        sort = 'max'
                        break
                    j += 1
                    m -= 1

    print 'sort =', sort
    if sort == 'min':
        h = min_heap()
    else:
        h = max_heap()
    
    for i in range(k):
        h.insert(heap_elem(arr[i][0], 0, i))
    
    #print 'Initial heap:'
    #for elem in h.arr:
    #    print elem.val

    merged_arr = [None for i in range(k*n)]
    print 'length of merged arr = ', len(merged_arr)
    j = 0
    while (h.get_size() > 0):
        min_max_elem = h.extract()
        #print 'min_elem = ', min_max_elem.val
        merged_arr[j] = min_max_elem.val
        j += 1

        if min_max_elem.pos < n-1:
            # Add next element from same array as min_elem
            next_arr_id = min_max_elem.arr_id
            next_pos = min_max_elem.pos + 1
            #print 'Inserting ', arr[next_arr_id][next_pos]
            h.insert(heap_elem(arr[next_arr_id][next_pos], next_pos, next_arr_id))
    return merged_arr

if __name__ == "__main__":
    f = open('merge_arr_output', 'w')
    r = open('merge_arr_small.txt', 'r')

    arr_rows = 0
    arr_cols = 0
    arr_rows = int(r.readline())
    arr_cols = int(r.readline())

    arr = []
    for arr_i in range(arr_rows):
        arr_temp = []
        for arr_j in range(arr_cols):
            arr_temp.append(int(r.readline()))
        arr.append(arr_temp)

    res = mergeArrays(arr);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )

    f.close()
    r.close()
