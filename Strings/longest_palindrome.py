# Find the longest substring that is a palindrome
# Input: abcbabcbddd
# Result: bcbabcb
# Brute force: Find all substring, find palindrome, return longest one. O(n^3)
# Optimize: Start with each of n elements as middle, go outwards and check for palindrome. O(n^2)  - Good enough for interview
# Note we need 2 loops - 1 for even palindrome and 1 for odd palindrome
# Manacher Algorithm - O(n) - Can be used as a solution for subproblem. Mention that longest palindrome can be done in O(n) with this algo.
#
# 
