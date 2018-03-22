def generate_all_subsets_helper(so_far, rest, out):
    if not rest:
        out.append(''.join(so_far))
        return

    new_rest = rest[:]
    ch = new_rest.pop(0)
    new_so_far = so_far[:]
    new_so_far.append(ch)
    generate_all_subsets_helper(new_so_far, new_rest, out) # Include ch
    generate_all_subsets_helper(so_far, new_rest, out) # Don't include ch


def generate_all_subsets(s):
    s_list = list(s)
    out = []
    so_far = []
    generate_all_subsets_helper(so_far, s_list, out)
    return out

if __name__ == "__main__":
    s = str(raw_input())

    res = generate_all_subsets(s);
    for res_cur in res:
        print res_cur

