#!/usr/bin/env python3

# from math import floor
# def get_long_entry(set, max_val):
#     min_index = 0
#     max_index = len(set) - 1
#     while min_index < max_index:
#         middle_index = floor(min_index + ((max_index - min_index) / 2))
#         if set[middle_index][1] == target:
#             returnset[middle_index]
#         elif set[middle_index][1] < target


def optimize_utilization(set_a, set_b, target):
    """ TODO: Each entry in the given sets is a [key, val] tuple.
    Return the entry from each set with the greatest sum that is
    less than the given target.
    """
    max_sum = -1
    max_sum_set = {}
    long_set = max(set_a, set_b)
    small_set = min(set_a, set_b)

    long_set.sort(key=lambda entry: entry[1])

    for small_entry in small_set:
        if small_entry[1] < target:
            # long_entry = get_long_entry(lomng_set, target - small_entry)
            for long_entry in long_set:
                if long_entry[1] <= target:
                    current_sum = small_entry[1] + long_entry[1]
                    if max_sum <= current_sum <= target:
                        max_sum = current_sum
                        max_sum_set.setdefault(current_sum, []).append(
                            [small_entry[0], long_entry[0]])

    return max_sum_set[max(max_sum_set)]


if __name__ == "__main__":
    set_a = [[1, 3], [2, 5], [3, 7], [4, 10]]
    set_b = [[1, 2], [2, 3], [3, 4], [4, 5]]
    target = 10

    print(optimize_utilization(set_a, set_b, target))

    # Output: [[2, 4], [3, 2]]
