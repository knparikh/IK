import heapq
import heapq
def topK(arr, k):

    n = len(arr)
    top_k = []
    num_seen = {}
    
    # Insert the first k elements in the heap
    for i in range(min(n, k)):
        heapq.heappush(top_k, arr[i])
        num_seen[arr[i]] = 1

    i += 1
    while(i < n):
        if (top_k[0] < arr[i]) and (arr[i] not in num_seen):
            del num_seen[top_k[0]]
            heapq.heappop(top_k)
            heapq.heappush(top_k, arr[i])
            num_seen[arr[i]] = 1
            
        i += 1

    new_arr = [heapq.heappop(top_k)]
    j = 1
    for i in range(len(top_k)):
        val = heapq.heappop(top_k)
        if val != new_arr[j-1]:
            new_arr.append(val)
            j += 1
    
    print('arr = ', arr)
    print('new_arr = ', new_arr)
    return new_arr

if __name__ == '__main__':
    arr = [4, -2, 1, -6, 2, -10, 4, -3, 10, -6, 5, -6, 7, -2, 10, -10, 4, -6, 5,-8]
    k = 7

    print 'top_k = ', topK(arr, k)
