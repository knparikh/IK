def solve(arr):
    out_list = []
    out_map = {}
    for s in arr:
        key, string = s.split(" ")
        if key in out_map:
            freq, lex = out_map[key]
            store = lex if lex > string else string
            out_map[key] = (freq + 1, store)
        else:
            out_map[key] = (1, string)
    for k in out_map.keys():
        freq, lex = out_map[k]
        out_str = k + ':' + str(freq) + ',' + lex
        out_list.append(out_str)
    return out_list

if __name__ == '__main__':
    arr = [
            "key1 abcd",
            "key2 zzz",
            "key1 hello",
            "key3 world",
            "key1 hello"
          ]
    print 'output = ', solve(arr)
