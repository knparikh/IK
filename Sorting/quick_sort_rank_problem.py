# Best case complexity n log n, space complexity log n (# of partitions => height of binary true)
# Worst case - bad partition - sorted array - n^2, space complexity O(n) (# of paritions = n)
# Picking pivot - median of 3 random integers gives best case complexity 97% times
# Quick sort is not stable, because in partition method, we may swap elements out of order.
# HW - Make quick sort stable hint: comparison method
# HW - Hoare's partition
def quick_select(inp, start, end, k):
    if (start >= end):
        return inp

    pivot_pos = partition(inp, start, end)

    if ((pivot_pos) == k-1):
        return inp[pivot_pos]
    elif ((pivot_pos) > k-1)
        # quick sort left half of array
        quick_select(inp, start, pivot_pos-1)
    else:
        # quick sort right half of array
        quick_select(inp, pivot_pos+1, end)


# Lamuto's partition using 2 pointers left and right
def partition(inp, start, end):
    pivot = inp[start]   # choose_pivot(inp, start, end)

    left = start + 1
    right = end

    while (left <= right):
        while (inp[left] < pivot):
            left = left + 1
        while (inp[right] > pivot):
            right = right - 1
        
        if (left < right):
            temp = inp[left]
            inp[left] = inp[right]
            inp[right] = temp

    return right


# Given an aray of n integers, find the element of kth rank (kth smallest element)
# Complexity is O(n) best case to O(n^2) worst case
if __name__ == "__main__":
    k = 4
    inp = [7, 4, 1, 21, 6, 5, 3, 2]
    print 'Element at k = ', quick_select(inp, 0, 7, 4)
