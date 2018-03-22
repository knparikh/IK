# Generate all possible expressions that evaluate to target value
# Input is string s containing any chars from ('0'-'9')
# Put operators ("", "*", "+") between pair of chars such that expression
# evaluates to target value. 
# Putting "" means chars are joined ex. 2""2 = 22
# Precedence of operatos : "", "*", "+"

char_map = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def atoi(l):
    result = 0
    for i in range(len(l)):
        result = result*10 + char_map[l[i]]
    return result


def generate_all_expressions_helper(s_list, pos, target, curr_str, curr_val, last_val, out):
    if pos == len(s_list):
        if curr_val == target:
            out.append(''.join(curr_str))
        return

    for i in range(pos, len(s_list)):
        # Implicit join operator
        part = s_list[pos:i+1]
        part_str = ''.join(part)
        part_value = atoi(part)
        
        if pos == 0:
            new_str = curr_str[:]
            new_str.append(part_str)
            generate_all_expressions_helper(s_list, i+1, target,
                new_str, part_value, part_value, out)
        else:
            plus_str = curr_str[:]
            plus_str.extend(('+', part_str))
            generate_all_expressions_helper(s_list, i+1, target,
                plus_str, curr_val+part_value, part_value, out)

            multiply_str = curr_str[:]
            multiply_str.extend(('*', part_str))
            generate_all_expressions_helper(s_list, i+1, target,
                multiply_str, curr_val-last_val+(last_val*part_value), part_value, out)


def generate_all_expressions(s, target):
    s_list = list(s)

    curr_str = []
    out = []
    generate_all_expressions_helper(s_list, 0, target, curr_str, 0, 0, out)
    return out


if __name__ == "__main__":
    try:
        s = str(input())
    except:
        s = None

    target = int(input());

    res = generate_all_expressions(s, target);
    for res_cur in res:
        print str(res_cur)

