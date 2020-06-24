#!/usr/bin/env python3
""" sort a 2d array into a single list in spiral order.
"""


def spiral_order(matrix):
    spiral_list = []

    while matrix:
        # print the top row
        top = matrix.pop(0)
        while top:
            spiral_list.append(top.pop(0))

        # print the right column.
        for i in range(len(matrix)):
            row = matrix[i]
            if row:
                spiral_list.append(row.pop())

        # print the bottom row.
        if matrix:
            bottom = matrix.pop()
            while bottom:
                spiral_list.append(bottom.pop())

        # print the left column.
        for i in range(len(matrix) - 1, 0, -1):
            row = matrix[i]
            if row:
                spiral_list.append(row.pop(0))

    return spiral_list


if __name__ == "__main__":
    test_matrix = [[1, 2, 3, 4], [5, 6, 7, 8],
                   [9, 10, 11, 12], [13, 14, 15, 16]]
    spiral_list = spiral_order(test_matrix)
    print(spiral_list)
