# Given 2 sorted arrays find if one is subset of another
# set1 = [1, 2, 3, .. 100]
# set2 = [1, 2, 3, .. 50]
# Use 2 pointers and compare to find
# O (max (m,n))  ok if m ~ n
# If m is >>>>> n, (nlogm) < m
# Optimization - Count matches, and if final count = size of smaller array, then return True
#
# 
