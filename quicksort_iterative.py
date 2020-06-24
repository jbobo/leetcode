#!/usr/bin/env pythone
""" Iterative implementation of QuickSort. merge sort when subarray length is 7.
"""


def get_partition(input_list, min_index, max_index):
    """Function takes last element as pivot,
    places the pivot element at its correct
    position in sorted array, and places all
    smaller (smaller than pivot) to left of
    pivot and all greater elements to right
    of pivot.
    """
    left = min_index - 1
    pivot = input_list[max_index]

    for current_index in range(min_index, max_index):
        if input_list[current_index] <= pivot:
            # increment index of smaller element
            left += 1
            input_list[left], input_list[current_index] = \
                input_list[current_index], input_list[left]

    left += 1
    input_list[left], input_list[max_index] = input_list[max_index], input_list[left]
    return left


def quicksort(input_list):
    min_index = 0
    max_index = len(input_list) - 1
    stack = []

    stack.append((min_index, max_index))

    while stack:
        """NOTE: This could be made faster by using a queue with a sentinel
        value or a second stack to store partitions <= a set length (7). Then
        use insertion sort to merge them into a sorted list
        """
        min_index, max_index = stack.pop()
        print(min_index, max_index)
        partition = get_partition(input_list, min_index, max_index)

        # If there are elements on left side of pivot,
        #  then push left side to stack
        if partition - 1 > min_index:
            stack.append((min_index, partition - 1))

        # If there are elements on right side of pivot,
        # then push right side to stack
        if partition + 1 < max_index:
            stack.append((partition + 1, max_index))

    return input_list


if __name__ == "__main__":
    """TODO: Do the thing.
    """
    test_list = [4, 3, 5, 2, 1, 3, 2, 3]
    sorted_list = quicksort(test_list)
    print("Sorted array is: %s" % (sorted_list))
    pass
