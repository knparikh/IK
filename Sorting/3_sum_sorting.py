# Sort the array.
# Start looking at element at i = 0 through len_arr-2, ignore if it is duplicate of i-1.
# From the remaining elements, try to find the two sum.
# Use 2 pointers to point to start and end of remaining array
# j = i+1
# k = len(arr)-1
# While j and k don't cross each other, and elements at j and k are not duplicates
#  if arr[j[ + arr[k] + arr[i] = 0, push the triplet in answer.
#  if sum is > 0, then we need to look at next smaller element, so j -= 1
#  if sum < 0, we need to look at next larger element, so i += 1
# Complexity: O(nlogn) for sorting + O(n^2) for traversing elements to find sum = O(n^2)
def three_sum(arr):
    # Sort the array
    arr.sort()
    out_list = []
    for i in range(len(arr)-2):
        # Ignore duplicates
        if (i > 0) and (arr[i] == arr[i-1]):
            continue

        j = i + 1
        k = len(arr)-1
        while(j < k):
            if ((j > (i+1)) and (arr[j] == arr[j-1])):
                j += 1
                continue
            if ((k < len(arr)-1) and (arr[k] == arr[k+1])):
                k -= 1
                continue
            two_sum = arr[j] + arr[k]
            if (arr[i] + two_sum) == 0:
                l = [str(arr[i]), str(arr[j]), str(arr[k])]
                out_list.append(','.join(l))
                j += 1
                k -= 1
            elif (arr[i] + two_sum > 0):
                # We need to go to next smaller element
                k -= 1
            else:
                # We need to go to next bigger element
                j += 1

    return out_list

if __name__ == "__main__":
    inp = [10, 3, -4, 1, -6, 9]
    #sum = -7
          
    #print 'two_sum = ', two_sum(inp, 0, sum)
    print '3sum = ', three_sum(inp) 
            
