# DP is recursion + memoization, but done iteratively. Then convert to iterative mechanically.
# DP can only be used for problems with overlapping sub-problems
# 1. Identify overlapping sub-problem
# 2. Formulate recursion optimally
# Example n-queens cannot be solved with DP

# Problems

# Best path problem:
# m rows, n cols
#   S   1 3 7
#       2 5 1
#       2 6 4     E
# Go from (0,0) to (2,2) using either right or down directions. Give path with max weight
#
# Max weight: 19   (1, 3, 5, 6, 4)
# Formulate recursion: 
# Start from (0,0) :  BP[i][j] = W[i][j] + max(BP[i+1][j], BP[i][j+1])
# Start from (2,2) : BP[i][j] = W[i][j] + max(BP[i-1][j], BP[i][j-1])
# O (2^height-1) Height is length of path. path length =  m+n-1 so O(2^(m+n-1) -1)

def best_path_rec(i, j, matrix, m, n):
    if (i == m-1) and (j == n-1):
        return matrix[i][j]


    if (i == m-1):
        return matrix[i][j] + (best_path_rec(i, j+1, m, n))   # Can go only down
    elif (j == n-1):
        return matrix[i][j] + (best_path_rec(i+1, j, m, n))   # Can go only up
    else:
        return matrix[i][j] + max(best_path_rec(i+1, j, matrix, m, n), best_path_rec(i, j+1, m, n))   # Choose from both right and down

def best_path(matrix, m, n):
    return best_path_rec(0, 0, matrix, m, n)

# Guidelines to convert recursive to iterative. Not all problems can be converted
# 1. Input should be constant. Example n-queens input is not constant, depnding on where queens are placed before this position, board is different.
# 2. Identify changing parameters. In best path, i,j are changing paremeters. 2 changing parameters O(n^2) in this case O(mn).
#          - They have to be indepedent. example j = i+3 , complexity changes to O(n)
# 3. Create DP table. - memoization as below. (return is return type of rec function) int DP [m][n]. Add return from pre-computed cache, and change all returns to cache[i][j] =
# 4. Convert to Bottom up/ Iterative   Opposite direction of recursion
def best_path_rec_memoization(i, j, matrix, m, n):
    if cache[i][j] != -1:      # If value already computed return from cache. Change all returns below to cache[i][j] =
        return cache[i][j]


    if (i == m-1) and (j == n-1):
        cache[i][j] =  matrix[i][j]

    if (i == m-1):
        cache[i][j] = matrix[i][j] + (best_path_rec(i, j+1, m, n))   # Can go only down
    elif (j == n-1):
        cache[i][j] = matrix[i][j] + (best_path_rec(i+1, j, m, n))   # Can go only up
    else:
        cache[i][j] = matrix[i][j] + max(best_path_rec(i+1, j, matrix, m, n), best_path_rec(i, j+1, m, n))   # Choose from both right and down

    return cache[i][j]



def best_path_dp(i, j, matrix, m, n):
    # Create DP table
    cache[m][n] = [[-1 for i in range(n)] for j in range(m)]

    # Start from end or leaf
    for (i in range(m-1, -1, -1)):
        for (j in range(n-1, -1, -1)):

            # Copy as is from recursion
            # Change return to write to cache[i][j]
            # Calls to recursive function are changed to read from cache[i][j]

            if (i == m-1) and (j == n-1):
                cache[i][j] =  matrix[i][j]

            if (i == m-1):
                cache[i][j] = matrix[i][j] + cache[i][j+1] # Can only come from down
            elif (j == n-1):
                cache[i][j] = matrix[i][j] + cache[i+1][j]   # Can go come from up
            else:
                cache[i][j] = matrix[i][j] + max(cache[i+1][j], cache[i][j+1])   # Choose from both right and down


        return cache[0][0]    # Take from caller


# In above, we can optimize - initialize last col and row of cache outside of loops
# Also can only use 1 row for DP table, if we only want to get max weight. To get best path, we need entire DP table
# In above, if direction changes to 3, complexity is still O(mn)
# NOTE In above, first check if greedy algorithm works, choose that. Here, we need
# to visit all nodes, so greedy will not work, so recursive, and overlapping subproblems so use DP
# To get best path in above problem, use DP table
# DP table
#         19 18 12
#         17 15 5
#         12 10 4
# Do greedy DFS in DP ->  19 -> 18 -> 15 -> 10 -> 4
# What is there is tie in the path, traverse both paths. i.e. DFS traversal of both paths

# Basic code to remember - DFS traversal, Find cycle in graph.
# NOTE digression - some tips Example find difference in words - edit distance
# bat -> cat -> car   Find shorted path to car.  Edit distance by 1, graph problem



# COIN CHANGE PROBLEM
# Cons {1, 5, 10, 25}
# Change : 76c
# Min coins that yields change: 4  (25, 25, 25, 1)
# Greedy algorithm - pick max each time, and reduce target
# In this problem, greedy will not work if denomination is changing
#  ex. 1 5 10 25 50   -> 31    greedy will give 25, 5, 1. but answer is 15, 15, 1?
# Will have to go through all choices , so recursion
# recursion formula : ca[A] = 1 + min (for all c in denomination cc[A-c])
# Recursion tree
#                                76
#                   1/         5/    10\    25\
#                  75         71      66      51
#              1/ 5/ 10\ 25\ 
#             74  70   65  50
#  O (4^76)   4 denomination i.e. branches, raised to height i.e. (target change/lowest denomination 1c)
# NOTE In DP, dont keep negative condition in base case, as they become subscripts in DP table
def coin_change_rec(denomination , target):
    if target == 0:
        return 0

    min = INT_MAX
    for d in denomination:
        if d <= target:
            num_coins = coin_change_rec(denomination, target-d)
            if num_coins == INT_MAX:
                continue    # In case 1penny was not there, we would not get any change, so handle that
            if num_coins < min:
                min = num_coins
    return 1 + min


# Changing to DP
# Complexity - changing parameter is change = 76. so worst case, O(change* num_denominations) i.e. from 4^76 to linear O(76*4)
# DP table : changing parameter is change , so int DP [change+1]   [0..76]
# NOTE   In many DP problems, Padding will be needed based on base case. Also try to add padding at end.
# Add memoization as below
#
def coin_change_rec(denomination , target, cache):
    if target == 0:
        cache[0] = 0

    min = INT_MAX
    for d in denomination:
        if d <= target:
            num_coins = coin_change_rec(denomination, target-d, cache)
            if num_coins == INT_MAX:
                continue    # In case 1penny was not there, we would not get any change, so handle that
            if num_coins < min:
                min = num_coins
    cache[target] = 1 + min

# Change to iterative
def coin_change_dp(denomination, target):
    cache = [0*(target+1)]

    cache[0] = 0  # Base case
    for new_target in range(1, target+1, 1):
        min = INT_MAX
        for d in denominations:
            if d <= new_target:
                num_coins = cache[new_target-d]   # Read
                if num_coins == INT_MAX:
                    continue    # In case 1penny was not there, we would not get any change, so handle that
                if num_coins < min:
                    min = num_coins
        cache[new_target] = 1 + min

    return cache[target]

def coin_change(denomination, target):
    cache = coin_change_dp(denomination, target)


# To get the coins selected, use the DP table, which is an array containing
# counts of each denomination. Start with dp[target], subtract each denom and
# lookup value at new_target. If new_val is 1 less than current val, go ahead. DFS.
