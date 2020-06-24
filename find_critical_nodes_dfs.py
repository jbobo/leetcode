#!/usr/bin/env python3

"""Implement Tarjan's algorithm to find all strongly connected components
in a DAG.
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


def path_based_scc(graph, root_node):
    """TODO: Do the thing.
    """
    stack = []
    no_scc_stack = []
    preorder_stack = []
    visited = {}
    counter = 0
    strongly_connected_components = []
    has_scc = set()
    # dfs_low = 0
    # dfs_num = 0
    # [0] = Root Val; [1] = Done; [2] = Visited; [3] =
    stack.append(root_node)

    # while stack:
    #     node = stack.pop()
    #     print(node)
    #     if node not in visited:
    #         counter += 1
    #         visited[node] = counter
    #         no_scc_stack.append(node)
    #         preorder_stack.append(node)
    #         for child in graph.get_children(node):
    #             if child not in visited:
    #                 stack.append(child)
    #             elif child not in has_scc:
    #                 child_count = visited[child]
    #                 while preorder_stack and preorder_stack[-1] in visited \
    #                         and visited[preorder_stack[-1]] > child_count:
    #                     preorder_stack.pop()
    #         if preorder_stack and preorder_stack[-1] == node:
    #             new_component = []
    #             while no_scc_stack[-1] != node:
    #                 component_node = no_scc_stack.pop()
    #                 new_component.append(component_node)
    #                 has_scc.add(component_node)
    #             new_component.append(no_scc_stack.pop())
    #             strongly_connected_components.append(new_component)
    #             preorder_stack.pop()
    # return strongly_connected_components

    # TODO: postorder DFS of the graph to transpose the graph and push (root?) vertices to a second stack.
    # for each node:
    #     if node not in visited:
    #         mark node as visited
    #         put node in the stack
    #         while stack is not empty:
    #             parent = stack.peek(-1) (node from before)
    #             set DONE = True
    #             for child in parent node:
    #                 reverse the connection in the transposed graph
    #                 if child node is not visited:
    #                     mark child node as visited
    #                     set DONE to False
    #             if DONE:
    #                 stack.pop(-1) (the parent node)
    #                 root_stack.append(parent node)

    # TODO: postorder DFS on T to pop root vertices from L and mark SCCs.
    # components = {}
    # while root_stack:
    #   root_node = root_stack.pop()
    #   stack = [root_node]
    #   if root_node in visited:
    #       set visited to false
    #       components[root_node] = root_node
    #   while stack:
    #       set DONE = True
    #       node = stack.peek(-1)
    #       for child of transposed node:
    #           if child has been visited:
    #               set DONE = False
    #               set child visited to False
    #               append child to stack
    #               components[child_node] = root_node
    #               break
    #       if DONE:
    #           stack.pop() (root node)
    # return components

    # NOTE: Basic DFS
    # while stack:
    #     node = stack.pop()
    #     if node not in discovered:
    #         dfs_low += 1
    #         dfs_num = dfs_low
    #         print(node)
    #         for child_node in graph.get_children(node):
    #             if child_node in discovered:
    #                 dfs_num = min(
    #                     discovered[child_node][1],
    #                     dfs_num
    #                 )
    #             else:
    #                 stack.append(child_node)
    #         print(node, dfs_low, dfs_num)
    #         discovered[node] = (dfs_low, dfs_num)
    #         if dfs_low == dfs_num:
    #             strongly_connected_components.append(node)
    # return strongly_connected_components


if __name__ == "__main__":
    undiscovered_graph = graph()
    undiscovered_graph.add_edge("A", "B")
    undiscovered_graph.add_edge("B", "C")
    undiscovered_graph.add_edge("C", "A")
    undiscovered_graph.add_edge("B", "D")
    undiscovered_graph.add_edge("D", "E")
    undiscovered_graph.add_edge("E", "F")
    undiscovered_graph.add_edge("F", "G")
    undiscovered_graph.add_edge("G", "H")
    undiscovered_graph.add_edge("H", "E")

    strongly_connected_components = path_based_scc(undiscovered_graph, "A")
    print(strongly_connected_components)
