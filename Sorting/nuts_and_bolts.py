def partition(arr, start, end, pivot):
    lt = i = start
    gt = end

    while (i <= gt):
        if (arr[i] < pivot):
            # Swap arr[i] with lt, incr i, lt
            arr[i], arr[lt] = arr[lt], arr[i]
            i += 1
            lt += 1
        elif(arr[i] > pivot):
            # Swap arr[i] with gt, decr gt
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            # arr[i] equals pivot, incr i
            i += 1

    return lt
      

# Enter your code here. Read input from STDIN. Print output to STDOUT
def quick_sort(nuts, bolts, start, end):
    if (start >= end):
        return

    pivot = bolts[start]
    # Using bolt as pivot, find the position for nut
    nut_pos = partition(nuts, start, end, bolts[start])
    # Using about nut as pivot, find position of bold
    bolt_pos = partition(bolts, start, end, nuts[nut_pos])
   
    print 'Partition for bolt ', pivot, nut_pos, bolt_pos
    # Since pivot_pos is final position for nut and bolt, sort remaining halves of array
    quick_sort(nuts, bolts, start, nut_pos-1)
    quick_sort(nuts, bolts, nut_pos+1, end)

if __name__ == "__main__":
    #nuts_bolts = [
    #              [[4, 3, 7, 9, 1, 2, 8, 6, 5],[5, 3, 6, 1, 9, 8, 2, 4, 7]],
    #              [[9, 8, 7, 6, 5, 4, 3, 2, 1],[1, 2, 3, 4, 5, 6, 7, 8, 9]],
    #             ]
    nuts = [4,3,5,1,2]
    bolts = [2,4,1,3,5]
    print 'Input nuts = ', nuts, 'bolts = ', bolts
    quick_sort(nuts, bolts, 0, len(nuts)-1)
    print 'sorted nuts/bolts = ', nuts, bolts
