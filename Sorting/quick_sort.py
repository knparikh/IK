# Best case complexity n log n, space complexity log n (# of partitions => height of binary true)
# Worst case - bad partition - sorted array - n^2, space complexity O(n) (# of paritions = n)
# Picking pivot - median of 3 random integers gives best case complexity 97% times
# Quick sort is not stable, because in partition method, we may swap elements out of order.
# HW - Make quick sort stable hint: comparison method
# HW - Hoare's partition
def quick_sort(inp, start, end):
    if (start >= end):
        return inp

    pivot_pos = partition(inp, start, end)

    quick_sort(inp, start, pivot_pos-1)

    quick_sort(inp, pivot_pos+1, end)


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

    # Swap pivot and right
    inp[start], inp[right] = inp[right], inp[start]

    return right
