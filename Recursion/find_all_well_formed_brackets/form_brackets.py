def form_brackets_recursive(out_str, out, open_count, close_count):
    if open_count == 0 and close_count == 0:
        out.append(''.join(out_str))
        return

    if open_count > 0:
        out_str.append('(')
        form_brackets_recursive(out_str, out, open_count-1, close_count)
        out_str.pop()

    if close_count > open_count:  # If close becomes more than open, we cannot build balanced brackets, so consume
        out_str.append(')')
        form_brackets_recursive(out_str, out, open_count, close_count-1)
        out_str.pop()

    

def find_all_well_formed_brackets(n):
    if n == 0:
        return ""

    out_str = []
    out = []
    form_brackets_recursive(out_str, out, n, n)
    return out


if __name__ == "__main__":
    n = int(input())

    res = find_all_well_formed_brackets(n);
    for res_cur in res:
        print res_cur

