#!/usr/bin/env python3
""" ImplementTarjan's algorithm to find all critical edges in a graph that
connect SCCs (strongly connected components). A critical edge is an edge that,
if removed, makes an SCC inaccessible.
"""


def criticalConnections(node_count, connections):

    # Create the graph as an adjacency matrix.
    graph = {}

    # Undirected graph, add bidirectional edges.
    for node, predecessor in connections:
        graph.setdefault(node, []).append(predecessor)
        graph.setdefault(predecessor, []).append(node)

    # Define the properties for Tarjan's algorithm.
    node_depth = [None] * node_count
    low_link = [None] * node_count
    current_depth = 0

    # Loop through the unvisited nodes with post-order dfs and find SCC
    #   (strongly connected components).
    dfs_stack = [(0, 0)]  # ( Node, predecessor )
    scc_stack = []
    on_stack = set()
    visited = set()  # set(graph.keys())

    while dfs_stack:
        # we only want to peek so we can perform post-order traversal
        node, predecessor = dfs_stack[-1]
        # set.remove() throws errors if key doesn't exist, set.discard() doesn't.
        # Mark the node as visited.
        visited.add(node)

        # Add the current node to on_stack.
        if node not in on_stack:
            scc_stack.append(node)
            on_stack.add(node)

        # Assign the node_depth and low link value.
        if node_depth[node] is None:
            node_depth[node] = current_depth
            low_link[node] = current_depth
            current_depth += 1

        # Loop through the neighbors (ignore predecessor).
        for neighbor in graph[node]:
            if neighbor != predecessor:
                # Add all unvisited neighbors to the scc_stack.
                if neighbor not in visited:
                    dfs_stack.append((neighbor, node))
                    break
                # Update low-link on neighbors in the stack.
                elif neighbor in on_stack:
                    low_link[node] = min(
                        low_link[node],
                        low_link[neighbor]
                    )

        # Continue the while loop if there are still neighbors to explore
        #   (i. e. top of the dfs_stack stack is different than the current node).
        if dfs_stack[-1][0] != node:
            continue

        # If node is a root node, backtrack (pop the stack) and generate an SCC.
        if low_link[node] == node_depth[node]:
            while node in on_stack:
                scc_neighbor = scc_stack.pop()
                low_link[scc_neighbor] = low_link[node]
                on_stack.remove(scc_neighbor)

        # This node has been has been visited (all its neighbors are visited as well),
        #   pop it from the dfs_stack stack.
        dfs_stack.pop()

    # Find all the critical edges (edges that connect different SCCs).
    critical_edges = []
    for node, predecessor in connections:
        if low_link[node] != low_link[predecessor]:
            edge = (node, predecessor)
            critical_edges.append(edge)

    return critical_edges


if __name__ == "__main__":
    node_count = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]

    print(criticalConnections(node_count, connections))
