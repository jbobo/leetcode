def max_subarray(array):
    """This is an implementation of Kadane's Algorithm."""
    # init with first index
    current_sum = global_maximum = array[0]

    # loop over the rest of the array
    for _, element in enumerate(array[1:]):
        # increment the leading pointer and update the current sum
        current_sum = current_sum + element

        # if the sum is bigger with the new element, update max sum
        if global_maximum < current_sum:
            global_maximum = current_sum

        # if the current sum is negative, increment the trailing pointer
        if current_sum < 0:
            current_sum = 0

    return global_maximum


if __name__ == "__main__":
    array = [1, 5, -1, 0, 10]
    max_sum = max_subarray(array)
    print(array, "\n", max_sum)
