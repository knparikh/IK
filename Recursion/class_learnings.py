def fibo(n):
    if (n == 0) or (n == 1):
        return n

    return fibo(n-1) + fibo(n-2)


# Tips to write recursive functions
# Define function meaningfully
# Think about base cases, what's already defined
# Think about the typical case
# Example:
# Merge sort
# Recurrence relationship
# Define function: merge (a (ignore static data), start, end)
# Base case:  If st >= end, do nothing or just return
# Typical case: merge(a, start, mid)
#               merge(a, mid+1, end)
#               Merge the two sorted array

# Make a execution tree. Helps to compute run time of function - it is the number of nodes in the tree. O(n)
# Space complexity - Height of tree O(height of tree), largest number of stacks when reaching leaf node
#                               f(4)
#                       f(2)            f(3)
#                   f(0)    f(1)    f(1)    f(2)      
#                                         f(0) f(1)
#
#
# Number of nodes in complete binary tree - geometric progression
# Constant ratio across term
#
# solve geometric progression
#  Sum a*r^i (for i from 0 to n-1) = a.(r^n -1)/ r-1
# To prove:
# Expand:
#       a + ar + ar^2 + ...ar^n-1
#       a (1+r+r^2+r^3+...r^n-1)
#       a (r-1)/(r-1) (1+r+r^2+r^3+...r^n-1)
#       = a.(r^n-1)/(r-1)
# In above example: a = 1, r = 2
#
#
# Arithmetic progression
#  1+2+3+4..+N = n * (n+1) /2
#
#
# Towers of Hanoi
#
#
#
# Towers of Hanoi using stack
class StackFrame(object):
    def __init__(self, n, st, end, helper)
        self.n = n
        self.st = st
        self.end = end
        self.helper = helper

def toh(n):
    stack = ()

    for i in range(n, -1, -1):
        if (n-i) % 2 == 0
            end = B
            helper = C
        else:
            end = C
            helper = B

# Given an array of size n, print all its subsets. Elements can be repeated.
# n c 0 subets of size 0
# n c 1 subsets of size 1
# n c 2 subsets of size 2..
# nCr is number of ways we can pick r things out of N things
# nC0 = 1, nCn = 1
# Total # of subsets = nC0 + nC1 + ...nCn = 2^n
#
def subsets(arr):

    helper(arr, 0,[None]*len(arr), 0)

def helper(arr, i, op, op_idx):
    if i == len(arr):
        print op[:op_idx]
        return

    #exclude
    helper(arr, i+1, op, op_idx)

    #include
    op[op_idx] = arr[i]
    helper(arr, i+1, op, op_idx + 1)

# Recursion with backtracking
# Example print all subsets that add upto <= k
def helper_backtrack(arr, i, op, op_idx, total):
    if i == len(arr):
        print op[:op_idx]
        return

    #exclude
    helper(arr, i+1, op, op_idx, total)

    #include
    if ((arr[i+1] + total) < k):
        op[op_idx] = arr[i]
        helper(arr, i+1, op, op_idx + 1)


# permutations of set
def permutations(arr):
    p_helper(arr, 0)

def p_helper(arr):
    if i == len(arr):
        print arr
        return
    for index in range(i, len(arr)):
        swap(arr, i , idx)
        helper(arr, i+1)
        swap(arr, i, idx)


# N Queens problem
