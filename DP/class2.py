# Prudhvi - DP Fast
# DP is usually used for optimization and counting problems. ex. max, min, shortest and # of paths

# Generate all subsets
def subsets(arr, i, out):
    if i == len(arr):
        print out

    # Call without arr[i]
    subsets(arr, i+1, out)

    # Call with arr[i] in out
    out = out.append(arr[i])
    subsets(arr, i+1, out)
    # Remove
    out.pop()



# Regex 'abcd', pattern 'a.*c*'
# Recurrence relation
# f(str_idx, pattern_idx) -> If string starting from str_idx matches pattern starting pattern_idx is a match.
# f (i, j)  -> True if i == len(string) and j == len(pattern)
#           -> False if j == len(pattern)
#           -> f(i+1, j+1) if pattern[j] == '.'  or pattern[j] == string[i]
#           -> f(i+1, j) or f(i, j+1) if pattern[j] == '*'
# Still need to deal with , if length of string is done, but pattern is remaining - 2 ways - check in first check if remaining of pattern is only *
#                                                                               OR before calling f(i+1 , check if i+1 is not end of string
# Time complexity worst case 2^n
# Turning it to DP becomes n^2
# In above, overlapping subproblems -> i+1, j and i, j+1


# DP is about computing values in table, starting from values we know to values we seek
# 1. Identify the table
#               - Dimensions - # of variables in function definition  (2)
#               - Size - Terminating and starting conditions i = 0 to len(str) incl , j = 0 to len(pattern) incl (n+1, m+1)
# 2. Initialize values - prepopulate extreme cases
# 3. Figure out direction of traversal - In order to figure out f(i,j) I need f(i+1/j+1): i has to go from higher to lower
#                                                                                         j has to go from higher to lower
# 4. Populate every cell


# Max path problem from DP Slow
# 
#       5   16 51 0
#       1   84 36 15
#       65  18 24 19
#       100 24 0 21
# Recurrence relationship:
#       f(i,j): Return max collected from i,j -> right bottom m-1, n-1
#       f(i,j) = 0  if i == M or j == N   ******In this problem u don't need this
#       grid[i][j] if i == M-1 and j == N-1
#       max(f(i+1,j), f(i, j+1)) + grid[i][j]
#
#       Table: M+1 x N+1

#       216  200 151 55   0
#       211  184 100 55   0
#       219  82   64 40   0
#       145  45   21 21   0
#        0   0    0  0    0
#
#       for i: M-1 : 0
#               for j: N-1 -> 0
#                    table[i][j] = max(table[i+1][j], table[i][j+1]) + grid[i][j]
def max_path(grid):
    table = [[]]  #2D list of size m+1, n+1
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        table[i][n] = 0

    for j in range(n):
        table[m][j] = 0

    for i in range(m+1, -1, -1):
        for j in range(n+1, -1, -1):
            table[i][j] = max(table[i+1][j], table[i][j+1]) + grid[i][j]

    return table[0][0]   # Max of required position

# For path calculation, do inverse of table[i][j] calculation

# Variant of above question - find # of paths to reach from start to end in a grid of 1 and 0.
# Can only get through cells with 1.
# f(i,j) -> returns # of paths from i,j to n-1, m-1
#
# Recurrence relationship:
#       f(i,j) : 0 if i == m or j == n
#                1 if i == m-1 and j == n-1
#                0 if grid[i][j] == 0
#               f(i+1, j) + f(i, j+1)
def num_paths(grid):
    table = [[]]  #2D list of size m+1, n+1
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        table[i][n] = 0

    for j in range(n):
        table[m][j] = 0

    for i in range(m+1, -1, -1):
        for j in range(n+1, -1, -1):
            if grid[i][j] == 0:
                table[i][j] = 0
            else:  # 1
                table[i][j] = table(i+1, j) + table(i, j+1)

        return table[0][0]

# If you have to find paths in above problem, no overlapping subproblems, so not a DP problem

# Coin change
# f(t) -> Min coins to make total of T
# f(t):  0 if t == 0
#       min(f(t-di)) for all di in D + 1 if d[i] <= t    # If we don't pick any di, return undefined
# Table  is 1-D of size T+1
# D is denomination array
def coin_change(D, T):

    t = 1
    while t < T:
        min_val = INT_MAX
        for d in D:
            if d <= t:
                min_val = min(min_val, table[t-d])
        table[t] = min_val

    table[T] = min_val + 1
    return table[T]

# Variant
# Return total # of ways in above problem
# Keep track of index in denomination array, so we don't end up including same denom again in subproblem
# f(t, i) -> No. of ways to make 't' from starting index 'i'
# f(t, i):  1 if t == 0
#           0 if i is at end of denom i == len(D)
#           f(t, i+1) if D[i] > t
#           f(t, i+1) + f(t-D[i], i)
# Make Recursion tree for [1,2,3] T = 3
# Table size: len(D)+1 rows, t = 0 to 3, so 4 cols
#
#       0   1   2  3
#     0 1
#     1 1
#     2 1
#     3 1  0   0  0
# i goes from high to low, t goes from 1 to T
# Read DP table: # of ways for making total 3 with entire denom - table[0][3] row = 0 because start index in D is 0
# If you want to only use denom [2,3], table[1][3] and so on
def count(D, T):

    for i in range(len(D)-1, -1, -1):
        for t in range(1, T+1):
            if D[i] > t:
                table[i][t] = table[i+1][t]
            else:
                table[i][t] = table[i+1][t] + table[i][t-D[i]]

    return table[0][T]

# Above can be changed to return min count, by coverting + to min


# Knapsack problem
# f(w, i) -> Max value starting from 'i' with 'w' remaining weight
# f(w, i) : 0 if w == 0
#           0 if i == len(obj)
#           f(w, i+1)  if wi > w
#           max (f(w, i+1), f(w-W[i], i+1) + Vi)
# 0 to W+1, 0 to len(V) + 1
def knapsack(W, V):

    table = [[]]

    return table[0][W]

# To get the list of objects, start at 0,W check which next is max
def get_object():
    i = 0
    w = w
    objects = []
    while w > 0 and i < len(obj):
        if table[i+1][w] == table[i][w]:
            # We did not pick object
            i += 1
        else:
            w = w - w[i]
            i += 1
            objects.append(i)
    return objects


# Given an array, count # of subsets that add upto k
# f(t, i) -> # of subsets starting from index i adding up to t
# f(t, i) : 1 if t == 0    # Null set
#           0 i == len(arr)
#           f(t, i+1) if arr[i] > t
#           f(t, i+1) + f(t-arr[i], i+1)   # Exclude and Include
# return table[T][0]
def count_subsets_to_k(arr, k):


# Balanced parition problem
# Given an array of positive integers, check if it can be paritioned into 2 subsets
# such that sum of both subsets is equal.
# Example {6 2 4} can be {6} {2 4}
# OR In US state, each state can have set of electoral votes which candidates can split and take, can there be a tie
# Since both subsets should be equal, sum of s1 = sum of s2 = total/2 if total is even
# So any one of subset should reach to t/2. So its above problem, count subsets to k where k = total/2


# Another version of balanced parition problem
# f (t, i)-> Whether there exists a subset starting from i that adds upto t
#  f(t, i):  True if t == 0
#            False if i == len(arr)
#            f(t, i+1) if arr[i] > t
#            f(t, i+1) or f(t-arr[i], i+1)


# Another version of balanced patition problem
# Parition array in 2 subsets such that difference between them is minimum.
# This is like knapsack problem - find subset such that T/2 - sum of subset is minimum
# [.. arr[i], arr[i], ..]  W = T/2. Value and weight are equal.
# f(t, i) -> max total starting from index i  <= t
# f(t, i): 0 if t = 0
#          0 i == len(arr)
#          f(t, i+1) if arr[i] > t
#          max(f(t, i+1), f(t-arr[i], i+1) + arr[i])
# Then find the elements of S1 from the table. Remaining elements are from S2.



# EDIT DISTANCE
# Edit distance problem or levenstein's distance
# Given a string, find least number of operations to another word with any of 3 ops:
#                       i Add char at index  i, j+1
#                       ii Remove char at index i+1, j
#                       iii Modify char at index  i+1, j+1
# CAT BITS
# Take examples to come up with above operations. To formulate extreme cases - 1. Push boundaries. 2. Known values
# f(i, j) -> Min # of operations to transform s1 starting from i to s2 starting from j
# f(i, j) : 0 if i == len(s1) and j == len(s2)   # Can get rid of this check because of below.
#           len(s2) - j if i == len(s1)
#           len(s1) - i if j == len(s2)
#           f(i+1, j+1) if s1[i] == s2[j]
#           else min(f(i, j+1), f(i+1, j), f(i+1, j+1)) + 1    # Need to add 1 because we are picking 1 of 3 operations
#
# Also write how to get transformations



# Robber trying to rob homes in a lane with cash values [V0, V1..Vn].
# If robber robs from a home, cannot rob from neighbors.
# Optimized amount to rob.
#       f(i) -> Max to rob starting from index i.
#       f(i):   0 if i == len(V)
#               max (f(i+1), f(i+2) + Vi)
#
