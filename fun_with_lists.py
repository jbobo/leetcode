#!/usr/bin/env python3
""" Play aroudn a bit with list/array slicing and enumeration behavior.
"""

if __name__ == "__main__":
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i, val in enumerate(test_list[4:]):
        print("index: %s\nvalue: %s" % (i, val))
