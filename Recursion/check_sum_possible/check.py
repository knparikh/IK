def check_if_sum_possible_helper(arr, target, pos, curr_val, curr_group):
    if (pos == len(arr)):
        return (curr_val == target and len(curr_group) > 0)
    
    # Check recursively by including current element and by not including current element
    curr_group.append(arr[pos])
    res1 = check_if_sum_possible_helper(arr, target, pos+1, curr_val+arr[pos], curr_group)
    curr_group.pop()
    res2 = check_if_sum_possible_helper(arr, target, pos+1, curr_val, curr_group)
    
    return res1 or res2
    
def check_if_sum_possible(arr, k):

    curr_group = []
    return check_if_sum_possible_helper(arr, k, 0, 0, curr_group)


if __name__ == "__main__":
    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input());
        arr.append(arr_item)
        arr_i += 1


    k = int(input());

    res = check_if_sum_possible(arr, k);
    print res

