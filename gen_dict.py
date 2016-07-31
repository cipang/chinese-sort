"""
This file reads Unihan_DictionaryLikeData.txt in the Unihan database, then generates a Python file that stores
 the data in a dict.

The Unihan database can be downloaded from: http://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip
Unihan_DictionaryLikeData.txt can be seen after extracting the above zip file.
"""

import os
import sys


kTotalStrokes = "kTotalStrokes"
kFrequency = "kFrequency"


def _process_value(value):
    value = value.strip()
    if " " in value:
        parts = value.split(" ")
        return max(int(x) for x in parts)
    else:
        return int(value)


def read(path):
    data = dict()
    with open(path, "r") as input_file:
        for line in input_file:
            # Line format: U+???? KeyName Value
            if not line or line.startswith("#"):
                continue

            parts = line.split("\t")
            if len(parts) != 3:
                continue

            code = int(parts[0][2:], base=16)
            key_name = parts[1]
            value = parts[2]
            if key_name != kTotalStrokes and key_name != kFrequency:
                continue

            if code not in data:
                data[code] = {kTotalStrokes: 99, kFrequency: 99}
            data[code][key_name] = _process_value(value)

    return data


def write(path, data):
    with open(path, "w") as output_file:
        output_file.write("data = ")
        output_file.write(repr(data))
        output_file.write("\n")


if __name__ == "__main__":
    if __name__ == "__main__" and len(sys.argv) != 2:
        print("usage: {0} path_to_unihan_txt".format(os.path.basename(__file__)))
        print("will output to sortdata.py.")
        exit(2)

    input_path = sys.argv[1]
    output_path = "sortdata.py"
    write(output_path, read(input_path))
