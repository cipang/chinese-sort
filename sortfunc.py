import sortdata


def chinese_sort_key(s):
    """
    Accepts a string and generates a key for comparison.
    """
    data = sortdata.data
    l = list()
    for c in s:
        code = ord(c)
        if c.isupper() or c.islower() or c.isspace() or c.isdigit():
            l.append(0)   # Strokes.
            l.append(code)   # Frequency.
        else:
            if code in data:
                l.append(data[code]["kTotalStrokes"])
                l.append(data[code]["kFrequency"])
            else:
                l.append(99)
                l.append(99)

    return tuple(l)
