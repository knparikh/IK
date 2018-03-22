#Given a string, find all possible palindromic partitions of given string.
# input: abracadabra
# output: a|b|r|a|c|a|d|a|b|r|a, a|b|r|a|c|ada|b|r|a, a|b|r|aca|d|a|b|r|a
def is_palindrome(s):
    return s == s[::-1]

def generate_palindromic_decompositions_helper(s, start, end, curr, out):
    if start >= end:
        curr_decompose = '|'.join(curr)
        out.append(curr_decompose)
        return

    for i in range(start, end):
        sub_s = s[start:i+1]
        if is_palindrome(sub_s):
            curr.append(''.join(sub_s))
            generate_palindromic_decompositions_helper(s, i+1, end, curr, out)
            curr.pop() 
    


def generate_palindromic_decompositions(s):
    out = []
    curr = []
    s_list = list(s)
    generate_palindromic_decompositions_helper(s_list, 0, len(s_list), curr, out)
    return out

if __name__ == "__main__":
    s = str(raw_input())
    res = generate_palindromic_decompositions(s);
    for res_cur in res:
        print res_cur

