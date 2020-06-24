#! /usr/bin/env python3
"""Kahn's algorithm for topological sorting.

It's basically BFS/DFS with tracking of in-degrees.
It's not as proper as kahn's algorithm, however it's good for when you have a
large adjacency list mapping various dependencies, and only care about getting
the topological sorting for one item.

IF YOU NEED A FULL TOPOLOGICAL DEPENDENCY SORT USE KAHN'S ALGO INSTEAD!!!
"""


def get_adjacency_matrix(adjacency_list):
    """Takes in an Adjacency list of (PARENT, CHILD) and converts it to an
    adjacency matrix mapping {CHILD: [PARENTS...]}.
    """
    adjacency_matrix = {}
    for edge in adjacency_list:
        parent = edge[0]
        child = edge[1]
        if child not in adjacency_matrix:
            adjacency_matrix[child] = [parent]
        else:
            adjacency_matrix[child].append(parent)
    return adjacency_matrix


def get_topo_to_child(adjacency_matrix, child):
    ordered_list = []
    visited_node_set = set()
    queue = [child]

    while len(queue) > 0:
        current_node = queue.pop(0)
        # prepend the parent node to the beginning of the topologically ordered list.
        ordered_list.insert(0, current_node)
        visited_node_set.add(current_node)
        if current_node in adjacency_matrix:
            parent_nodes = adjacency_matrix[current_node]
            for node in parent_nodes:
                if node not in visited_node_set:
                    queue.append(node)
    return ordered_list


if __name__ == "__main__":
    adjacency_list = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [1, 5]]

    adjacency_matrix = get_adjacency_matrix(adjacency_list)
    sorted_list = get_topo_to_child(adjacency_matrix, 5)
    print(sorted_list)
