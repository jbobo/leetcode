#!/usr/bin/env python3
""" given an array of non-negative integers, calculate how many cubes of
rainwater can be held in the resulting histogram.
"""


def get_capacity(histogram):
    """determine the capacity of water that could be held by the peaks and
    valleys of the given histogram.
    """
    capacity = 0
    left = [0] * len(histogram)

    # set the left local maxima per index.
    max_height = 0
    for i, height in enumerate(histogram):
        max_height = max(max_height, height)
        left[i] = max_height

    # set the right local maxima per index.
    #  and using the left and right maxima, find how
    #  much water could be stored at each individual index.
    right = 0
    for i, height in reversed(list(enumerate(histogram))):
        right = max(right, height)
        capacity_at_index = min(left[i], right) - height
        if capacity_at_index > 0:
            capacity += capacity_at_index

    return capacity


if __name__ == "__main__":
    test_histogram = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # return 6

    rainwater_capacity = get_capacity(test_histogram)
    print(rainwater_capacity)
