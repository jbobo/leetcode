#!/usr/bin/env python3
"""Binary search a sorted array.
"""
from math import ceil


def binary_search(sorted_list, target):
    """ Return True if sorted_list contains the target.
    Return False if sorted_list does not contain the target.
    """
    min_index = 0
    max_index = len(sorted_list) - 1
    while min_index < max_index:
        middle_index = ceil((min_index + max_index) / 2)
        current_val = sorted_list[middle_index]
        if current_val == target:
            return middle_index
        elif current_val < target:
            if middle_index < max_index:
                min_index = middle_index + 1
            else:
                return -1
        elif current_val > target:
            if middle_index > min_index:
                max_index = middle_index - 1
            else:
                return -1
    return -1


if __name__ == "__main__":
    sorted_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

    target = 2
    target_index = binary_search(sorted_list, target)

    print("Index of %s in the sorted array is: %s" % (target, target_index))
