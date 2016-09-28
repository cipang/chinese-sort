"""
Generates a plain text file with Chinese characters, stroke counts and frequencies.
Only includes common characters.
Use gen_dict.py to generate the dict first.
"""

import sortdata
from datetime import datetime

l = [(chr(code), info["kTotalStrokes"], info["kFrequency"]) for code, info in sortdata.data.items() if code <= 65535]
l.sort(key=lambda x: x[1])

with open("chinese.txt", "w", encoding="utf8") as f:
    f.write("# Chinese Strokes Database - Date: {0:%Y-%m-%d %H:%M:%S}\n".format(datetime.now()))
    f.write("# Char\tStrokes\tFrequency\n")
    for t in l:
        f.write("{0}\t{1}\t{2}\n".format(*t))
