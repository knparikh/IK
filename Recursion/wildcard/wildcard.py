# Wildcard
# Input: 10?
# Output: 101, 100
def wildcard_helper(s, start, out, curr_str):
    if start == len(s):
        out.append(''.join(curr_str))
        return

    c = s[start]
    if c == '?':
        curr_str.append('1')
        wildcard_helper(s, start+1, out, curr_str)
        curr_str.pop()
        curr_str.append('0')
        wildcard_helper(s, start+1, out, curr_str)
        curr_str.pop()
    else:
        curr_str.append(c)
        wildcard_helper(s, start+1, out, curr_str)
        curr_str.pop()

    return

def wildcard(s):
    out = []
    curr_str = []
    wildcard_helper(s, 0, out, curr_str)
    return out


if __name__ == "__main__":
    s = str(raw_input())
    s = list(s)
    res = wildcard(s)

    for r in res:
        print r
