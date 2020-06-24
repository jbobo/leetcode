#!/usr/bin/python3
"""implement a DFS algorithm to discover and count the number of islands on a map.
"""


def get_island_count(grid):
    """ TODO: Do the thing.
    """
    height = 0
    width = 0
    island_count = 0
    if grid and grid[0]:
        height = len(grid)
        width = len(grid[0])
    else:
        return island_count
    for row in range(height):
        for column in range(width):
            if grid[row][column] == "1":
                island_count -= 1
                stack = []
                stack.append((row, column))
                while stack:
                    current_row, current_column = stack.pop()
                    # give the vertex an island ID
                    grid[current_row][current_column] = str(island_count)
                    # get north
                    if current_row > 0:
                        north = (current_row - 1, current_column)
                        if grid[north[0]][north[1]] == "1":
                            stack.append(north)
                    # get south
                    if current_row < height - 1:
                        south = (current_row + 1, current_column)
                        if grid[south[0]][south[1]] == "1":
                            stack.append(south)
                    # get west
                    if current_column > 0:
                        west = (current_row, current_column - 1)
                        if grid[west[0]][west[1]] == "1":
                            stack.append(west)
                    # get east
                    if current_column < width - 1:
                        east = (current_row, current_column + 1)
                        if grid[east[0]][east[1]] == "1":
                            stack.append(east)
    return abs(island_count)


if __name__ == "__main__":
    test_grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    island_count = get_island_count(test_grid)
    print("Island count: %s" % (island_count))
