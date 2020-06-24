#!/usr/bin/env python3


def search_matrix(matrix, target):
    """Search a sorted matrix for a given value using adaptive search.
    """
    if not matrix or not matrix[0] or not target:
        return False

    height = len(matrix)-1
    width = len(matrix[0])-1

    current_x = 0
    current_y = height

    while current_y >= 0 and current_x <= width:
        current_val = matrix[current_y][current_x]

        if target < current_val:
            # if the target is less than the current value, move North.
            current_y -= 1
        elif target > current_val:
            # if the target is greater than the current value, move East.
            current_x += 1
        else:
            # We found the target value
            return True
    # if we exaust the valid X and Y limits then the value doesn't exist in the
    #  matrix.
    return False


if __name__ == "__main__":
    matrix = [
        [1, 4],
        [2, 5]
    ]
    target = 1

    print("Is %s in the matrix? %s" % (target, search_matrix(matrix, target)))
