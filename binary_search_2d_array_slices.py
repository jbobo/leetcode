#!/usr/bin/env python3
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

https://leetcode.com/problems/search-a-2d-matrix-ii/
"""
from math import ceil
# - start in the middle.
# - if node is bigger:
#   - add the middle node of the upper-right, lower-right, and lower-left quadrants
#     to the queue.
# - if the node is smaller:
#   - add the middle node of the upper-right, lower-right, and upper-left quadrants
#     to the queue.
# - if the current vertex value is the target, return TRUE.
# - if the queue is empty, return FALSE.


def searchMatrix(matrix, target):
    """Perform a quadrary search for a given target on the given 2d array.
    """
    if not matrix or not matrix[0] or not target:
        return False

    queue = []

    row_min = 0
    row_max = len(matrix) - 1
    col_min = 0
    col_max = len(matrix[0]) - 1

    queue.append((row_min, row_max, col_min, col_max))

    while queue:
        submatrix = queue.pop(0)

        row_min = submatrix[0]
        row_max = submatrix[1]
        col_min = submatrix[2]
        col_max = submatrix[3]

        # Base case, no elements
        if (row_max < row_min or col_max < col_min):
            return False

        # Base case, Single cell
        if (row_min == row_max and col_min == col_max):
            if matrix[row_min][col_min] == target:
                return True

        row_mid = row_min + ((row_max - row_min) / 2)
        col_mid = col_min + ((col_max - col_min) / 2)

        if matrix[row_min][col_min] == target:
            return True

        # Search Top-Right
        queue.append(row_min, row_mid + 1, col_mid + 1, col_max)

        # Search Bottom-Left
        queue.append(row_mid + 1, row_max, col_min, col_mid)

        # Search Top-Left
        if (target < matrix[row_mid][col_mid]):
            queue.append(row_min, row_mid, col_min, col_mid)

        # Search Bottom-Right
        else:
            queue.append(row_mid + 1, row_max, col_mid + 1, col_max)

    return False


if __name__ == "__main__":
    # matrix = [
    #     [1,   4,  7, 11, 15],
    #     [2,   5,  8, 12, 19],
    #     [3,   6,  9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ]
    # target = 27
    # matrix = [
    #     [1, 4, 7, 11, 15],
    #     [2, 5, 8, 12, 19],
    #     [3, 6, 9, 16, 22],
    #     [10, 13, 14, 17, 24],
    #     [18, 21, 23, 26, 30]
    # ]
    # target = 5
    matrix = [
        [1, 4],
        [2, 5]
    ]
    target = 1

    print("Is %s in the matrix? %s" % (target, searchMatrix(matrix, target)))
    # print(matrix)
