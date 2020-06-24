#!/usr/bin/env python3

from heapq import heappush, heappop


def get_min_cost_to_repair_edges(node_count, edges_list, edges_to_repair_list):
    """There's an undirected connected graph with n nodes labeled 1..n.
    But some of the edges has been broken disconnecting the graph.
    Find the minimum cost to repair the edges so that all the nodes are once
    again accessible from each other.
    """
    graph = {}  # {parent_node: [(cost, child_node), (), ...]}
    edges_set = set()  # tuples (node A, node B)

    # build up our initial graph, adding the edges_to_repair with their cost.
    for first_node, second_node, cost in edges_to_repair_list:
        graph.setdefault(first_node, []).append((cost, second_node))
        # the graph is undirected, so we add a bydirectional relation.
        graph.setdefault(second_node, []).append((cost, first_node))
        edges_set.add((first_node, second_node))
        edges_set.add((second_node, first_node))

    # ignoring duplicate edges, add every original edge with a cost of 0.
    for first_node, second_node in edges_list:
        edge = (first_node, second_node)
        if edge not in edges_set:
            graph.setdefault(first_node, []).append((0, second_node))
            graph.setdefault(second_node, []).append((0, first_node))

    total_cost = 0
    # start with an arbitrary root node, as the graph is undirected.
    priority_queue = [(0, 1)]
    visited = set()

    while priority_queue:
        cost, node = heappop(priority_queue)
        if node not in visited:
            visited.add(node)
            total_cost += cost
            for cost, connected_node in graph.get(node):
                if connected_node not in visited:
                    heappush(priority_queue, (cost, connected_node))

    return total_cost


if __name__ == "__main__":
    node_count = 5
    edges_list = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    edges_to_repair_list = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]

    min_cost_to_repair_edges = get_min_cost_to_repair_edges(
        node_count, edges_list, edges_to_repair_list)

    print(min_cost_to_repair_edges)
