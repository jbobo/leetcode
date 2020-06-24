#!/usr/bin/env python3


def distance(coord):
    """Return the distance of the given coordinate from the origin.
    We use manhattan distance from (0, 0), but it could be extended to use a given
    origin, or euclidian distance.

    If time is valued over space, we could compute all of the distance values
    ahead of time and store them in the coordinate tuples or in a hashmap.
    """
    coord_x, coord_y = coord
    return (abs(coord_x) + abs(coord_y))


def partition(coords, low_pointer, high_pointer):
    """Lomuto's partition algo from QuickSort.
    This is more easily understood and more commonly used than Hoare's partition
    algo.

    We're iterating over the partition, moving all values less than the pivot
    value to the left side of the partition, then returning the swap_index.
    everything to the left of the swap index is lower than the value at the swap
    index.
    """
    # swap_index, should initialize as the lowest index in the partition.
    swap_index = low_pointer
    pivot_value = distance(coords[high_pointer])

    for current_index in range(low_pointer, high_pointer):
        if distance(coords[current_index]) <= pivot_value:
            # if the current value is less than the pivot value, swap them, to move
            #  the current value to the left side of the partition.
            coords[swap_index], coords[current_index] = coords[current_index], coords[swap_index]
            # increment swap_index.
            swap_index += 1
    # Put our pivot_value back at the swap_index.
    coords[swap_index], coords[high_pointer] = coords[high_pointer], coords[swap_index]
    return swap_index


def k_closest(coords, k):
    """Partially sorts A[i:j+1] so the first k elements are
    the smallest k elements. We don't care about sorting of the elements after k.
    so we can get away with less than N(Log(N)) runtime complexity in most cases
    where k < len(coords)  and k is not in non-increasing order.
    """
    # Validation steps: Handle empty coords or k=0.
    if not coords or not k:
        return []
    if k >= len(coords):
        return coords

    left = 0
    right = len(coords) - 1
    # Initialize the pivot point at the returned swap_index of the first run of
    #  our quicksort partition algo.
    pivot = partition(coords, left, right)

    # We can guarantee that all indexes left of the pivot index will be less than
    #  the pivot index. so we'll basically keep running quicksort (repeatedly
    #  partition, shifting left or right of the current pivot point) until the
    #  returned swap_index is at K.
    while pivot != k:
        print(pivot, left, right)
        if pivot > k:
            right = pivot - 1
        elif pivot < k:
            left = pivot + 1
        pivot = partition(coords, left, right)

    # return a slice of coords from 0->k ()
    return coords[:k]


if __name__ == "__main__":
    coords = [(1, 3), (4, -2), (-2, 2), (-3, 3), (2, -2), (5, 5)]
    k = 2
    print(k_closest(coords, k))
