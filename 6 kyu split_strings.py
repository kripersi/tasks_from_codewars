def split_strings(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]
