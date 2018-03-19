# Calorie calculator, spreadsheet
# Given a static sized array of n numbers, support
#       point_update(index, vale)
#       random_sum(st, en)
# Brute Force point_update  O(1)
#    range_sum(st, en)  O(n)
# Can use prefix sum array - which is running sum till that index
#       point_update O(n)
#       range_sum  O(1)
# Segment tree
#    point_update O(log n)
#    range_sum O(log n)
# Can also do range_multiple similarly
# Above solution takes extra space
# For no extra space, use binary indexed tree.
# BIT can only used for sum operations not for range multiply 
#
