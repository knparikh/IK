# Input "abcdd"
# Regex "ab*"
# . - match any 1 char
# * - match 0 or more chars
#         a    i = 0, j = 0
#         b    i = 1, j = 1
#         .    i = 2, j = 2
#         *     i = 3, j = 3
#        /      \
#    skip *     include *
#    i = 3, j=4    i = 4, j = 3
def regex(inp, regx, i, j):
    if (i == len(inp)):
        return j == len(regx)

    if i > len(inp):     # For the corner case: abc , abc*
        return False

    if i < len(inp) and regx[j] == '*':
        return regex(inp, regx, i, j+1) or regex(inp, regx, i+1, j)

    if (regx[j] == '.') or inp[i] == inp[j]:
        return regex(inp, regx, i+1, j+1)

    return False
