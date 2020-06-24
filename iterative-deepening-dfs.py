#!/usr/bin/python3
"""Perform Iterative Deepening Depth First Search on a directed acyclical graph.

This search method is good for finding the path with the fewest edges _.

Considerations:
    directed or undirected?
    cyclical or acyclical?
    weighted or unweighted?
    does any of this need to be validated by my search?
"""

class node:
    
    def __init__(self, val):
        self.val = val
        self.children = []
    

    def get_val(self):
        return self.val


    def add_child(self, child):
        child_node = node(child)
        self.children.append(child_node)
        return child_node


    def get_children(self):
        return self.children


def IDDFS(root_node):
    """Helper function to invoke DLS().
    """
    max_depth = 0
    is_edge_found = False
    while not is_edge_found:
        max_depth += 1
        is_edge_found = DLS(root_node, max_depth)


def DLS(root_node, max_depth):
    """Perform depth limited search on the given graph node, up to the given max depth.
    """
    remaining_nodes_stack = [ (root_node, 0), ]
    visited_nodes = set()

    while len(remaining_nodes_stack) > 0:
        current_node, current_depth = remaining_nodes_stack.pop()
        if current_depth <= max_depth:
            print ("Node: %s, Depth: %s" % (current_node.val, current_depth))
            children = current_node.get_children()
            print("Children: %s" % (children))
            if len(children) > 0:
                for child_node in children:
                    if child_node not in visited_nodes:
                        visited_nodes.add(child_node)
                        remaining_nodes_stack.append((child_node, current_depth + 1))
            else:
                return True
        else:
            return False
    return True

if __name__ == "__main__":
    root_node = node("A")
    node_b = root_node.add_child("B")
    node_c = root_node.add_child("C")
    node_d = node_b.add_child("D")
    node_e = node_c.add_child("E")
    node_f = node_c.add_child("F")
    node_g = node_e.add_child("G")

    IDDFS(root_node)









