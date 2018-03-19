def sortCharacters(inp):
    freq_map = [0 for i in range(256)]

    for ch in list(inp):
        freq_map[ord(ch)] += 1

    j = 0
    out = [None for i in range(len(inp))]
    for i in range(len(freq_map)):
        for k in range(freq_map[i]):
            out[j] = chr(i)
            j += 1
    return ''.join(out)
