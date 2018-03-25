# Integer array of size n where n is very large
# Sliding window of size w, moving left to right, by one position each time.
# Return an array, where the i-th number is max of arr[i] to arr[i+w-1]
def max_in_sliding_window(arr, w):
    out = []


    return out


if __name__ == "__main__":
    arr_cnt = 0
    arr_cnt = int(input())
    arr_i = 0
    arr = []
    while arr_i < arr_cnt:
        arr_item = int(input())
        arr.append(arr_item)
        arr_i += 1


    w = int(input())

    res = max_in_sliding_window(arr, w);
    for res_cur in res:
        print res_cur

