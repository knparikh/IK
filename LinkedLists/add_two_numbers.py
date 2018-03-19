# Given 2 LL , produce LL representing sum of two numbers
# Brute force: Convert to numbers and then add them and create LL for result
# Another approach - using recursion
# Prepend 0s to shorter number, write recursion
def add_two_numbers(l1, l2);

    len1 = get_len(l1)
    len2 = get_len(l1)
    
    # Make shorter one of same length as longer one
    if (len1 > len2):
        prepend(l2, len1-len2)
    elif(len2 > len1):
        prepend(l1, len2-len1, 0)

    carry = add_ll_rec(l1, l2)
    if carry > 0:
        prepend(l2, 1, carry)


def add_ll_rec(l1, l2):
    if l1 == None and l2 == None:
        return None, 0

    carry = add_ll_rec(l1.next, l2.next)
    l2.val = l1.val + l2.val + carry

    return l2, l2.val/10


