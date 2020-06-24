#! /usr/bin/env python3


class DisjointSet:
    def __init__(self):
        self.vertices = set()
        self.parent = {}

    def add(self, node):
        if node not in self.vertices:
            self.vertices.add(node)
            self.parent[node] = node

    # TODO: implement iteratively
    def find(self, node):
        temp_node = node
        while self.parent.get(temp_node) != temp_node:
            temp_node = self.parent.get(temp_node)
        self.parent[node] = temp_node
        return temp_node

    def union(self, parent_node, child_node):
        parent_root = self.find(parent_node)
        child_root = self.find(child_node)
        self.parent[child_root] = parent_root


if __name__ == "__main__":
    disjoint_set = DisjointSet()
    disjoint_set.add("A")
    disjoint_set.add("B")
    disjoint_set.add("C")
    disjoint_set.add("D")

    disjoint_set.union("D", "B")
    disjoint_set.union("B", "A")

    print(disjoint_set.find("A"))

    disjoint_set.union("C", "A")

    print(disjoint_set.find("C"))
    print(disjoint_set.find("A"))
