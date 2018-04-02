# Shuffle array
# In: [12, 11,14, 15, 13]
# 1. Return only one of n! solutions
# 2. Selection of equally likely solutions - choose a solution with prob 1/n!
# For 2, assume random generator: random(n) = {0..n-1} with prob 1/n
# Brute force - requires lot of space O(n!*n) - precompute all n! solutions  O(n^n). then use random number generator (n!) and index into solution and return it. O(1)
# Approach2 - Call random(n) for index 0 - prob 1/N
#                  random(n-1) for index 1 - prob 1/N-1
#                  ...
#                  random(1)  for index n - prob 1/n
#                  final prob = 1/N!
def random_shuffle(inp, n):
    # NOTE Important to start from end, since then random number generator gives 0 to n-1,
    # easy to work from back. else will have to add some offset since once we have 
    # processed index once, we don't want to process it again.
    for i in range(n-1, -1, -1)  # Call random n times each time with n, n-1, ...
        index = random(i+1)
        #swap elements
        inp[i], inp[index] = inp[index], inp[i]

# Real world application of above: Dynamo db, Berkeley DB
# Implement KV store ++
# KV APIs
# put(k, v)   -----
# get(k)           |
# delete(k)   -----
# get_random()   # Returns a random val with prob 1/size of store
# Example if some value containing a hashtag is returned multiple times, it means this hashtag is trending
# So instead of running bulky analytics job, we can query above get_random to know what is trending
# For above, ask interviewer which API is going to be used more frequently.
# 
# Use index_array containing key so we get index to key mapping
# Hashmap of key to (v, index)
# ****For 2 datastructures, keep forward going pointer and backward going pointer.
def put (k, v):
    # If key not in hashmap, then add to index arr and then to hashmap
    if k not in hashmap:
        index_arr.append(k)
        last_idx = len(index_arr)-1
        hashmap[k] = (last_idx, v)  #tuple

def delete(k):
    # Get index of k, swap with last element of index_arr
    if k in hashmap:
        index = hashmap(k)[0]
        #Swap with last element of array
        index_arr[index], index_arr[len(index)-1] = index_arr[len(index)-1], index_arr[index]
        update_key = index_arr[index]
        index_arr.pop()
        # Update index of swapped element i.e active key in hashmap
        old_index, val = hashmap(update_key)
        hashmap(update_key) = (index, val)

        # Delete input key from hashmap
        del hashmap(k)



# RETAIN-BEST-CACHE
#
# APIs
# get(k) - Returns a value if exists in cache
#          if not present, pull from disk, using dsget(k)  
# if max-size is exceeded. evict lowest rank element from cache
# rank of element - getRank(v)
# multiple keys can have same rank
#  LRU cache has hashmap and dequeue/linkelist
# Here, we need hashmap and heap/priority_queue
# hashmap : <key,value>
# priority queue pq: <rank, key>   BW pointer
#
def get(k):
    if k in hashmap:
        return hashmap[k]
    else:
        v = dsget(k)
        rank = getRank(v)
        if len(hashmap.keys) == MAX_SIZE:
            if rank > pq[0][0]:  #peek in priority queue
                return v  # no need to insert in pq
            else:
                rank, k = heapq.heappop(pq)   # remove lowest and add the new key
                del hashmap[k]
        heapq.heappush(((rank,k))   # needs re-heapify
        hashmap[k] = v
        
# To ensure concurrency - use concurrent hash map
#  For pq, use synchronized remove and insert
# In above, to optimze pq, multiple keys have same rank , so keep them together
# So in above, when deleting from pq, just remove key from set of keys for rank.
# Only if keys is empty, remove rank and re-heapify. 
# For insert, check if rank is present, if not then add rank with first key. else find rank and append to its key.
# O(R i.e # of ranks) to search the rank. Before it was log(k i.e # of keys). How to prove O(R) is bettern then O(logK)
# if R < K, then log R < log K -> so instead of PQ make is BST so that search is O(log R)
# So finally - move from PQ to consolidated keys PQ to BST of consolidated keys
#


# Merge overalpping intervals
# Insert interval (long start, long end)
# GetMergedInterval()
# Inp: [1,5], [10,16], [2,4], [3,6] Output: [1,6][10,16]
# Brute force: Sort array based on start : [1,5] [2,4] [3,6] [10, 16]
#               Merge [1, max(2,4)] [3,6] [10,16]
#                      [1,max(4,6)] [10, 16]
#                       [1, 6][10,16]
# O(nlogn)  # based on sorting
# Now in case we have to keep dynamic array i.e insert new intervals
# Approach 1: Insert at end, then sort. so nsert O(1), getMerged (O(nlogn))
# In case getmerged needs to be better - offload sort to insert - insert in sorted array O(n) or in BST O(log n). Then for merge inorder traveral and then merge O(n)
# Approach 2: Interval tree   Get will be O(1). Creating interval tree O(nlogn. ) Interval tree not easy in coding
#     Use approach 1 BST as its good for insert O(logn), merge O(n)
# 


# Sliding window maximum - important for streaming data from IOT devices etc
# {4, 5, 6, 1, 5, 3, 7, 9, 8, 2}   sliding window k =1
# Output: {6, 6, 6, 5, 7, 9 9 9}   # of entries n-k+1
# get_max should be O(1)
# Soln: Using Queue - insertion/removal is O(1), FIFO, invariant, elements in deque are in descending order
#  for i in first k elements:
#       while (queue not empty) and arr[q.back] < arr[i]
#               q.pop_back()
#       q.push_back(i)
#
#  for rest of elements e:
#       while (queue not empty) and arr[q.back] <= i-k
#               q.pop_front()
# If decereasing data, O(n). If ascending order, then O(nk) since we need to delete from queue
#

# TRAPPING RAINWATER
# {4, 6, 7, 5, 1, 2, 3, 9, 10, 5, 7}
# Assume above are heights of a wall
# Keep global max to left of elements: {0,  4,  6,  7,   7,  7, 7,   7, 9, 10, 10}
# Keep global max from right:          {10, 10, 10, 10, 10, 10, 10, 10, 7, 7,  0}
# Take min of 2 at each position:      {0, 4,    6,  7,  7,  7,  7,  7, 7, 7,  0}
# For each eleme in input, if elem < min, then fill
def trap():
    max = 0
    templeft = [0]
    for i in range (1, n, 1):
        if a[i-1]  > max:
            max = a[i-1]
            templeft = max


# An array has distinct elements {1, N+2}. size of array N. Sort it.
# {7, 1 ,4, 3, 5}
# Find 2 missing numbers
# sum 1 to N+2 = ((N+2) * (N+3)) /2  = 28.
# Sum of input = 20
# Sum of missing numbers = 28-10 = 8
# (1 * 2 *.. * N+2)/ (Product of array)  = 12
# x + y = 8
# xy  = 12
# Skip missing numbers and rebuild array - O(n). Plain sort is O(nlogn)


# FINDING majority element in an array  {4, 1, 4, 5, 4, 4}
# Element that occurs more than n/2  times in the array
# Majority element is always maximally occuring element. But maximally element is not majority element
# Approach 1: Sorted array, and there's guarantee that majority element exists, then majority = middle element of array O(1) a[mid]
# Approach 2: Sorted array, but no guarantee. Go to mid: Then find start and last index of middle element
# with binary search. last-first is number of times element occurs. If n/2 then that is the majority element.  O(logn)
# Approach 3: Unsorted array, no guarantee#, no space. - sorting + binary search = O(nlogn) + O(logn)
# We want O(n), no auxilary space
# Moore's voting algorithm:
def find_majority(inp):
    n = len(inp)
    index = 0
    int count
    for (i in range (1, n, 1))
        if arr[i] == arr[index]:
            count += 1
        else:
            count -= 1

            if count == 0:
                count = 1
                index = i

    candidate = inp[index]
    # check count of inp[index]
    count = 0
    for i in len(range(n)):
        if inp[i] == candidate:
            count += 1

    if count > (n/2):
        return candidate

    return None


# MINSTACK ++
# push(v)
# pop()
# peek()
# peekmin()
# ********
# popmin()    # Remove all min elements
# Primary structure  doubly linked list for stack
# Secondary Structure - Start with PQ of values, but we need to consolidate by
#                       value, set of LL nodes <value, set of LL nodes> . But for pop, we need to search for val in PQ so O(n)
#                                       - now make this BST, so pop becomes O(logn)
#



# GRAPH
# k: memberid, v: [Adjacency list]
# getConn(id) return adjacency list in sorted array
# 1st degree connection n1, n2 : getConn(n1) search if n2 is present. O(logn) Binary search since sorted.
# 2nd degree connection n1, n2 : l1 = getConn(n1) intersection l2 = getConn(n2). Merge step or merge sort in l1,l2
# 3rd degree connection n1, n2: l1 = getConn(n1) then for all elements in graph, which are not 2nd degree connection O(n^2)
# Cannot solve above in single server, distributed system. vertical paritioning - find intersection only with range of connections.


# BOMBER-MAN ********
# Matrix of empty space or obstacles.
# Find position of max impace.

