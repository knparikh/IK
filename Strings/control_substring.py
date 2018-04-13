# # of substrings/subarray in a string - O(n^2)
# # of subsequence/subset 2^n
# Shortest substring that controls the set
# Input = "helloworld"
# set = {'l', 'r', 'w'}
# Results = "worl"
# Brute force: O(n3) Make all substrings starting at 'h' - h, he, hel.. O(n^2).
# Then check for substing containing the set, O(n^3)
# Little optimize: O(n^2) - Starting at h, keep going till we encounter all 3 chars (O(n)). Do for substrings starting at e, l etc. Store that in hash. O(n^2)
# Expand and optimize: Maintain hash table of chars in set with count.
# Start at h, keep going till all counts are non-zero.
#
