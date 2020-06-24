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

# def get_vertex(matrix, x_min, x_max, y_min, y_max)


class SubMatrix:

    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.vertex = (
            ceil((self.x_min + self.x_max) / 2),
            ceil((self.y_min + self.y_max) / 2)
        )

    def __str__(self):
        return ("SubMatrix: x_min: %s; x_max: %s; y_min: %s; y_max: %s; vertex: %s" % (self.x_min, self.x_max, self.y_min, self.y_max, self.vertex))

    def get_northeast_quadrant(self):
        northeast_quadrant = SubMatrix(
            self.vertex[0], self.x_max, self.y_min, self.vertex[1]-1)
        if northeast_quadrant.vertex != self.vertex:
            return northeast_quadrant
        return None

    def get_northwest_quadrant(self):
        northwest_quadrant = SubMatrix(
            self.x_min, self.vertex[0] - 1, self.y_min, self.vertex[1]-1)
        if northwest_quadrant.vertex != self.vertex:
            return northwest_quadrant
        return None

    def get_southeast_quadrant(self):
        southeast_quadrant = SubMatrix(
            self.vertex[0], self.x_max, self.vertex[1], self.y_max)
        if southeast_quadrant.vertex != self.vertex:
            return southeast_quadrant
        return None

    def get_southwest_quadrant(self):
        southwest_quadrant = SubMatrix(
            self.x_min, self.vertex[0] - 1, self.vertex[1], self.y_max)
        if southwest_quadrant.vertex != self.vertex:
            return southwest_quadrant
        return None


def contains_target(matrix, submatrix, target):
    # if matrix[submatrix.y_min][submatrix.x_min] == target:
    #     return True
    if matrix[submatrix.y_min][submatrix.x_min] > target:
        return False
    elif matrix[submatrix.y_max][submatrix.x_max] < target:
        return False
    else:
        return True


def search_matrix(matrix, target):
    """Perform a quadrary search for a given target on the given 2d array.
    """
    if not matrix or not matrix[0] or not target:
        return False

    visited = set()
    center_vertex = SubMatrix(0, len(matrix[0]) - 1, 0, len(matrix) - 1)
    vertex_queue = [center_vertex]

    while vertex_queue:
        # get a new vertex from the queue.
        current_vertex = vertex_queue.pop()
        current_index_x, current_index_y = current_vertex.vertex
        current_value = matrix[current_index_y][current_index_x]
        if current_vertex.vertex not in visited:
            visited.add(current_vertex.vertex)
            print(current_vertex)
            print(current_value)
            if contains_target(matrix, current_vertex, target):
                if current_value < target:
                    southeast_quadrant = current_vertex.get_southeast_quadrant()
                    if southeast_quadrant and southeast_quadrant.vertex not in visited:
                        print("South East Quadrant: %s" % (southeast_quadrant))
                        vertex_queue.append(southeast_quadrant)
                elif current_value > target:
                    northwest_quadrant = current_vertex.get_northwest_quadrant()
                    if northwest_quadrant and northwest_quadrant.vertex not in visited:
                        print("North West Quadrant: %s" % (northwest_quadrant))
                        vertex_queue.append(northwest_quadrant)
                else:
                    # We found the target value
                    return True

                # get the northeast quadrant, we always add this one.
                northeast_quadrant = current_vertex.get_northeast_quadrant()
                if northeast_quadrant and northeast_quadrant.vertex not in visited:
                    print("North East Quadrant: %s" % (northeast_quadrant))
                    vertex_queue.append(northeast_quadrant)

                # get the southwest quadrant, we always add this one.
                southwest_quadrant = current_vertex.get_southwest_quadrant()
                if southwest_quadrant and southwest_quadrant.vertex not in visited:
                    print("South West Quadrant: %s" % (southwest_quadrant))
                    vertex_queue.append(southwest_quadrant)

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

    print("Is %s in the matrix? %s" % (target, search_matrix(matrix, target)))
    # print(matrix)
