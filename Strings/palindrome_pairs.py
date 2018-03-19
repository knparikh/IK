# Given a list of words, find palindrome pairs
# inp: {race, cat, dog, god, car, ma, dam}  N, M length
# output : {racecar, doggod, madam, goddog}
# Brute force : O(n2) combine all words
# Approach 2: Hash table: Put every word's reverse in hash table. If word exists
# as prefix in hash and its remaining is palindrome, then pair is palindrome. But does not work for race/car, madam
# Time complexity: O(N(for all words) * M^2 (to strcmp prefix of length M) + M (palindrome for rest of string))  ~ O(M^2).
# Creating hash of reverse words = O(N^2) for each word, reverse and then insert in hash.
# Above does not work with ma/dam - for ma, mad does not exist
# We also need second hash table with words as it is , and look for reverse
# This problem can also be solved with Trie and ReverseTrie
#
#
