#!/usr/bin/env python3
"""Kahn's algorithm for topological sorting.

1. Get the number of edges.
2. Calculate the indegrees of all nodes (storing all nodes with 0 in-degrees in a queue).
3. Start with a root (0 indegrees) node, remove it and deincrement the indegrees of all it's children.
4. Append the root node to a list to return at the end.
5. Pop the next root node and repreat until none remain.
6. if the number of nodes in the topologically sorted list is equal to the number of nodes in your indegrees map then the topological sort is valid.
"""


def get_adjacency_matrix(adjacency_list):
    """ Convert the given adjacency list (PARENT, CHILD) into an adjacency matrix
    {PARENT: [CHILDREN...]}
    """
    adjacency_matrix = {}
    for edge in adjacency_list:
        # If the node isn't present in the matrix, add it with a default list to
        #  store neighbors, then append the neighbor to that list.
        adjacency_matrix.setdefault(edge[0], []).append(edge[1])
    return adjacency_matrix


# Time complexity: O(V+E)
# Space complexity: O(V)
def topological_sort(adjacency_matrix):
    topological_queue = []
    root_node_queue = []
    indegree_map = {}

    # Step 1: Iterate adjacency_matrix and build in-degree for each node
    # Time complexity: O(V+E) - outer loop goes V times and inner loop goes E times
    for node in adjacency_matrix:
        indegree_map.setdefault(node, 0)
        for child in adjacency_matrix.get(node, []):
            # Set a default value of 0 for new child nodes.
            indegree_map.setdefault(child, 0)
            # increment the in-degree count by 1
            indegree_map[child] += 1

    # Step 2: Find node(s) with 0 in-degree
    for node in indegree_map:
        if (indegree_map[node] == 0):
            root_node_queue.append(node)

    # Step 3: Process nodes with in-degree = 0
    while root_node_queue:
        current_node = root_node_queue.pop(0)
        topological_queue.append(current_node)
        # Step 4: Update in-degree
        for child in adjacency_matrix.get(current_node, []):
            indegree_map[child] -= 1
            if (indegree_map[child] == 0):
                root_node_queue.append(child)
    if len(indegree_map) == len(topological_queue):
        return topological_queue
    else:
        return ("Error, cycles detected in graph.")


if __name__ == "__main__":
    adjacency_list = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    adjacency_matrix = get_adjacency_matrix(adjacency_list)
    topological_sort = topological_sort(adjacency_matrix)
    print(topological_sort)
