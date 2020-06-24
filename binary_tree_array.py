#!/usr/bin/env python3
""" Implement a binary tree using an array.
"""
# i = node index
# left = (2 * i) + 1
# right = 2 * (i + 1)


class BinaryTree:

    def __init__(self, size):
        self.tree = [-1] * size

    def get(self, val):
        index = 0
        while index < len(self.tree) and self.tree[index] > -1:
            if val == self.tree[index]:
                return (index, val)
            elif val < self.tree[index]:
                # get left
                index = (2 * index) + 1
            elif val > self.tree[index]:
                # get right
                index = 2 * (index + 1)
        return (-1, val)

    def insert(self, val):
        index = 0
        while index < len(self.tree):
            if self.tree[index] == -1:
                self.tree[index] = val
                return (index, val)
            elif val < self.tree[index]:
                # get left
                index = (2 * index) + 1
            elif val > self.tree[index]:
                # get right
                index = 2 * (index + 1)
        return (-1, val)


if __name__ == "__main__":
    # TODO: Do the thing.
    bin_tree = BinaryTree(7)
    print(bin_tree.tree)
    bin_tree.insert(3)
    bin_tree.insert(1)
    bin_tree.insert(5)
    bin_tree.insert(0)
    bin_tree.insert(6)
    bin_tree.insert(2)
    bin_tree.insert(4)
    print(bin_tree.tree)

    print(bin_tree.get(2))
