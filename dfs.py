#!/usr/bin/env python3
""" DFS graph discovery implementation for finding cycles in undirected graphs.
"""

class graph:

    edges = dict()

    def __init__(self):
        """Initialize a graph object with no edges.
        '"""
        self.edges = dict()

    def add_edge(self, parent, child):
        """Add an edge between two nodes to the graph.
        """
        self.edges.setdefault(parent, []).append(child)
        if child not in self.edges:
            self.edges[child] = [parent]
        else:
            self.edges[child].append(parent)

    def get_children(self, node):
        """Get the children of the given node in the graph.
        Returns [] if the given node does not exist in the graph.
        Return a sentinel value of [-1] if you want to detect cycles.
        """
        return self.edges.get(node, [])


class DFS:
    def __init__(self, graph, root_node):
        """Perform a DFS search on the given graph.
        """
        self.graph = graph
        self.root_node = root_node
        self.discovered = {}
        self.stack = []
        self.search()

    def search(self):
        self.stack.append(self.root_node)
        while len(self.stack) > 0:
            node = self.stack.pop()
            # if node == goal_node:
            #     return node
            if node not in self.discovered:
                self.discovered[node] = True
                print(node)
                for child_node in self.graph.get_children(node):
                    # print("Child: ", child_node)
                    if child_node != -1:
                        self.stack.append(child_node)
                    # else:
                    #     print("Found cycle in graph. Aborting...")
                    #     return


if __name__ == "__main__":
    """Driver program to test the DFS graph search implementation.
    """
    undiscovered_graph = graph()
    undiscovered_graph.add_edge("A", "B")
    undiscovered_graph.add_edge("A", "C")
    undiscovered_graph.add_edge("A", "E")
    undiscovered_graph.add_edge("B", "D")
    undiscovered_graph.add_edge("B", "F")
    undiscovered_graph.add_edge("C", "G")
    undiscovered_graph.add_edge("F", "E")

    DFS(undiscovered_graph, "A")










