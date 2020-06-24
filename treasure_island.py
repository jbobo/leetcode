#!/use/bin/env python3
"""
"""


def iddfs(matrix, max_depth, goal):
    """Implementation of IDDFS on the given matrix.
    """
    visited = set()
    max_row = len(treasure_map) - 1
    max_column = len(treasure_map[0]) - 1
    stack = []
    stack.append(
        (0, 0, 0)
    )

    while stack:
        current_row, current_column, current_depth = stack.pop()
        print(current_row, current_column, current_depth)

        if treasure_map[current_row][current_column] == goal:
            return current_depth

        if current_depth < max_depth:
            # Get North
            if current_row > 0:
                if treasure_map[current_row - 1][current_column] != "D":
                    if (current_row - 1, current_column) not in visited:
                        stack.append(
                            (current_row - 1, current_column, current_depth + 1)
                        )
                        visited.add((current_row - 1, current_column))
            # Get South
            if current_row < max_row:
                if treasure_map[current_row + 1][current_column] != "D":
                    if (current_row + 1, current_column) not in visited:
                        stack.append(
                            (current_row + 1, current_column, current_depth + 1)
                        )
                        visited.add((current_row + 1, current_column))
            # Get East
            if current_column < max_column:
                if treasure_map[current_row][current_column + 1] != "D":
                    if (current_row, current_column + 1) not in visited:
                        stack.append(
                            (current_row, current_column + 1, current_depth + 1)
                        )
                        visited.add((current_row, current_column + 1))
            # Get West
            if current_column > 0:
                if treasure_map[current_row][current_column - 1] != "D":
                    if (current_row, current_column - 1) not in visited:
                        stack.append(
                            (current_row, current_column - 1, current_depth + 1)
                        )
                        visited.add((current_row, current_column - 1))

    return -1


def get_distance_to_treasure(treasure_map):
    """Find the shortest path to the goal node in the treasure map.
    """
    distance_to_treasure = -1
    depth = 0
    if treasure_map and treasure_map[0]:
        vertex_count = len(treasure_map) * len(treasure_map[0])
        while distance_to_treasure < 0 and depth < vertex_count:
            depth += 1
            distance_to_treasure = iddfs(treasure_map, depth, 'X')
    return distance_to_treasure


if __name__ == "__main__":
    treasure_map = [
        ['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'O']
    ]

    distance_to_treasure = get_distance_to_treasure(treasure_map)
    print(distance_to_treasure)
