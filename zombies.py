#!/usr/bin/env python3
"""
Given a 2D grid, each cell is either a zombie 1 or a human 0.
Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour.
Find out how many hours does it take to infect all humans?
"""


def min_hours(rows, columns, zombie_map):
    """Return the number of hours it would take for zombies to take over the map.
    """
    queue = []
    min_hours = -1
    north = (-1, 0)
    south = (1, 0)
    east = (0, 1)
    west = (0, -1)

    # seed initial values.
    for row_index in range(rows):
        for column_index in range(columns):
            if zombie_map[row_index][column_index] == 1:
                queue.append((row_index, column_index))

    # add sentinel value.
    queue.append((-1, -1))

    # discovery of new zombies after each hour.
    while queue:
        zombie = queue.pop(0)
        if zombie == (-1, -1):
            min_hours += 1
            if queue:
                queue.append((-1, -1))
        else:
            check = []
            if zombie[0] > 0:
                check.append((zombie[0] + north[0], zombie[1] + north[1]))
            if zombie[0] < rows - 1:
                check.append((zombie[0] + south[0], zombie[1] + south[1]))
            if zombie[1] > 0:
                check.append((zombie[0] + west[0], zombie[1] + west[1]))
            if zombie[1] < columns - 1:
                check.append((zombie[0] + east[0], zombie[1] + east[1]))
            for index in check:
                if zombie_map[index[0]][index[1]] == 0:
                    zombie_map[index[0]][index[1]] = 1
                    queue.append((index))

    return min_hours


if __name__ == "__main__":
    zombie_map = [
        [0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0]
    ]

    rows = len(zombie_map)
    columns = len(zombie_map[0])

    print("%s hours until the zombies take over!" %
          (min_hours(rows, columns, zombie_map)))
