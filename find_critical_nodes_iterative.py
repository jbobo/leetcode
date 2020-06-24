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


class stack_entry:
    def __init__(self, node, parent_node=None, depth=0):
        self.node = node
        self.parent_node = parent_node
        self.depth = depth


def get_critical_edges(graph, root_node):
    critical_edges = []
    node_depth = {}  # Low-Link
    stack = []
    root_entry = stack_entry(root_node, None, 0)
    stack.append(root_entry)

    # POST-ORDER DFS traversal of the graph.
    while stack:
        # Peek the stack.
        current_entry = stack[-1]
        node_depth[current_entry.node] = current_entry.depth
        # Get all children.
        for child in graph.get_children(current_entry.node):
            # IF: the child node is unexplored, add it to the stack.
            if child not in node_depth:
                child_entry = stack_entry(
                    node=child,
                    parent_node=current_entry.node,
                    depth=current_entry.depth + 1
                )
                stack.append(child_entry)
        # POST-ORDER. Only process the current node AFTER all of its children.
        if stack[-1] == current_entry:
            # init min_depth
            min_depth = current_entry.depth
            # Remove the entry from the stack.
            stack.pop()
            # Get all children.
            for child in graph.get_children(current_entry.node):
                # IF: the child is not the parent node AND we have explored the child node.
                if child != current_entry.parent_node and child in node_depth:
                    # IF: the child belongs to another SCC, then this edge is critical.
                    child_depth = node_depth[child]
                    if child_depth > current_entry.depth:
                        critical_edges.append((current_entry.node, child))
                    # ELSE: update the current node's low-link (depth).
                    min_depth = min(current_entry.depth, child_depth)
            # Update the current node's low-link (depth).
            node_depth[current_entry.node] = min_depth

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
