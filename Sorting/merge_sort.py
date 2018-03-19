# Divide into 2 halves using mid, then start merging them
def merge_sort(inp, start, end):
    
    if (start >= end):
        return

    mid = start + (end - start)/2
    merge_sort(inp, start, mid)
    merge_sort(inp, mid+1, end)

    inp = merge(inp, start, mid, end)

def merge(inp, start, mid, end):

    merged = [0 for i in range (end+1)]

    left = start
    right = mid+1
    i = 0

    while(left <= mid and right <= end):
        if (inp[left] <= inp[right]):
            merged[i] = inp[left]
            left = left + 1
            i = i + 1
        else:
            merged[i] = inp[right]
            right = right + 1
            i = i + 1

    # Copy remaining elements from left half of array
    while (left <= mid):
        merged[i] = inp[left]
        left = left + 1
        i = i + 1

    # Copy remaining elements from right half of array
    while (right <= end):
        merged[i] = inp[right]
        right = right + 1
        i = i + 1


    # Copy back into inp
    j = 0
    for i in range(start, end+1):
        inp[i] = merged[j]
        j = j + 1

    return inp

def MergeSort(intArr):
    merge_sort(intArr, 0, len(intArr)-1)
    return intArr

if __name__ == "__main__":
    inp = [5, 0, -1, -2, 5, 4]

    print 'merge_sort = ', MergeSort(inp)
