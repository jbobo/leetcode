#!/usr/bin/env python3
""" BFS graph discovery implementation.

- This can be used for detecting cycles in DIRECTED graphs.

- Use a linked list node structure and mark nodes as visited to improve space complexity.
"""


class graph:

    def __init__(self):
        """Initialize a graph object with no edges.
        '"""
        self.edges = {}

    def add_edge(self, parent, child):
        """Add an edge between two nodes to the graph.
        """
        self.edges.setdefault(parent, []).append(child)
        # NOTE: UNCOMMENT IF GRAPH IS UNDIRECTED.
        # self.edges.setdefault(child, []).append(parent)
        # if child not in self.edges:
        #     self.edges[child] = [parent]
        # else:
        #     self.edges[child].append(parent)

    def get_children(self, node):
        """Get the children of the given node in the graph.
        Returns [-1] if the given node does not have children.
        """
        return self.edges.get(node, [])
        # if node in self.edges:
        #     return self.edges[node]
        # else:
        #     return [-1]


class BFS:
    def __init__(self, graph, root_node):
        """Perform a BFS search on the given graph.
        """
        self.graph = graph
        self.root_node = root_node
        self.discovered = {}
        self.queue = []
        self.search()

    def search(self):
        self.queue.append(self.root_node)
        self.discovered[self.root_node] = True
        while len(self.queue) > 0:
            node = self.queue.pop(0)
            # if node == goal_node:
            #     return node
            # print("Parent: ", node)
            print(node)
            for child_node in self.graph.get_children(node):
                # print("Child: ", child_node)
                # if child_node != -1:
                if child_node not in self.discovered:
                    # print("Child: ", child_node)
                    self.discovered[child_node] = True
                    self.queue.append(child_node)
                # else:
                #     print("Found cycle in graph. Aborting...")
                #     return


if __name__ == "__main__":
    """Driver program to test the BFS graph search implementation.
    """
    undiscovered_graph = graph()
    undiscovered_graph.add_edge(0, 1)
    undiscovered_graph.add_edge(0, 2)
    undiscovered_graph.add_edge(1, 2)
    undiscovered_graph.add_edge(2, 0)
    undiscovered_graph.add_edge(2, 3)
    undiscovered_graph.add_edge(3, 3)

    BFS(undiscovered_graph, 2)
