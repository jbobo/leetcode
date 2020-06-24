from math import ceil

def get_median(array1, array2):
    """Use Divide-and-conquer to binary search over the smaller array for the point where:
        
            array1-a <= array2b && array2-a <= array1-b
        
        it's a binary search using pointers to represent a partition/slice. 
        if we don't care about the indices we could maybe use array slices instead.
        
        Required: len(Array1) <= len(Array2)
    """
    median = 0
    array1_partition_start = 0
    array1_partition_end = len(array1)

    while (array1_partition_start <= array1_partition_end):
        array1_pointer = ceil((array1_partition_start + array1_partition_end) / 2) 
        array2_pointer = ceil(((len(array1) +  len(array2)) / 2) - array1_pointer)

        if (
            array1_pointer < len(array1) 
            and array2_pointer > 0 
            and array2[array2_pointer - 1] > array1[array1_pointer]
        ):
            array1_partition_start = array1_pointer + 1

        elif(
            array1_pointer > 0 
            and array2_pointer < len(array2) 
            and array2[array2_pointer] < array1[array1_pointer - 1]
        ):
            array1_partition_end = array1_pointer - 1
        else:
            if (array1_pointer == 0):
                median = array2[array2_pointer - 1]
            elif (array2_pointer == 0):
                median = array1[array1_pointer - 1]
            else:
                median = max(array1[array1_pointer - 1], array2[array2_pointer - 1])
            break
    return median


if __name__ == "__main__":
    test_cases = [
        [[1, 2, 3, 4],[5, 6, 7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8]],
        [[1, 3, 5, 7],[2, 4, 6, 8]],
        [[6, 7, 8, 9],[1, 2, 3, 4]],
        [[8, 9], [1, 2, 3, 4, 5, 6, 7]]
    ]

    for case in test_cases:
        median = get_median(case[0], case[1])
        print ("The median of: %s and %s is: %s" % (case[0], case[1], median))
