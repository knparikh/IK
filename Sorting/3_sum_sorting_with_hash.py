from sets import Set
def two_sum(inp, excl, target):
    out = set()
    sum_pair = {}
    for i in range(len(inp)):
        if (i == excl) or ((i > 0) and (inp[i] == inp[i-1])):
            continue
        sum_partner = target - inp[i]

        if inp[i] in sum_pair:
            in_tuple = (inp[i], inp[sum_pair[inp[i]]])
            rev_tuple = (inp[sum_pair[inp[i]]], inp[i])
            #out.append((i, sum_pair[input[i]]))
            if (in_tuple in out) or (rev_tuple in out):
                continue
            else:
                out.add(in_tuple)
        else:
            sum_pair[sum_partner] = i
        #print sum_pair

    return out

def findZeroSum(arr):
    arr.sort()
    three_sum_map = {}
    out = []
    for i in range(len(arr)):
        if arr[i] not in three_sum_map:
            two_sum_target = -1 * arr[i]
            three_sum_map[arr[i]] = two_sum(arr, i, two_sum_target)

    for k in three_sum_map.keys():
        for two_sum_elem in three_sum_map[k]:
            v1, v2 = two_sum_elem
            l = [str(k), str(v1), str(v2)]
            out.append(','.join(l))
    return out
    #return three_sum_map

if __name__ == "__main__":
    inp = [10, 3, -4, 1, -6, 9]
    #sum = -7
          
    #print 'two_sum = ', two_sum(inp, 0, sum)
    print '3sum = ', findZeroSum(inp)
