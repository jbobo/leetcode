#!/usr/bin/env python3


class Graph:

    edges = dict()

    def __init__(self):
        """Initialize a graph object with no edges.
        '"""
        self.edges = dict()

    def add_edge(self, parent, child):
        """Add an edge between two nodes to the graph.
        """
        self.edges.setdefault(parent, []).append(child)
        # if child not in self.edges:
        #     self.edges[child] = [parent]
        # else:
        #     self.edges[child].append(parent)

    def get_children(self, node):
        """Get the children of the given node in the graph.
        Returns [] if the given node does not exist in the graph.
        Return a sentinel value of [-1] if you want to detect cycles.
        """
        return self.edges.get(node, [])


def get_critical_edges(graph, root_node):
    critical_edges = []
    node_depth = {}

    def dfs(graph, current_node, parent_node=None, current_depth=0):
        # print("current_node: %s" % (current_node))
        node_depth[current_node] = current_depth
        min_depth = current_depth
        for child in graph.get_children(current_node):
            # if child != parent_node:
            if child in node_depth:
                temp_depth = node_depth[child]
            else:
                temp_depth = dfs(
                    graph, child, current_node, current_depth + 1)

            if temp_depth > current_depth:
                critical_edges.append((current_node, child))
            else:
                min_depth = min(min_depth, temp_depth)

        node_depth[current_node] = min_depth
        return min_depth

    dfs(graph, root_node)
    return critical_edges


if __name__ == "__main__":
    undiscovered_graph = Graph()
    undiscovered_graph.add_edge("A", "B")
    undiscovered_graph.add_edge("B", "C")
    undiscovered_graph.add_edge("C", "A")
    undiscovered_graph.add_edge("B", "D")
    undiscovered_graph.add_edge("D", "E")
    undiscovered_graph.add_edge("E", "F")
    undiscovered_graph.add_edge("F", "G")
    undiscovered_graph.add_edge("G", "H")
    undiscovered_graph.add_edge("H", "E")

    print(get_critical_edges(undiscovered_graph, "A"))
