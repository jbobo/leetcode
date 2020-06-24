#!/usr/bin/env python3
""" Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):
    current_level = []  # stack
    next_level = []  # stack
    zig_zag_order = []

    is_clockwise = True

    if root:
        current_level.append(root)

    while current_level or next_level:
        zig_zag_order.append([])
        for i in range(len(current_level)):
            current_node = current_level.pop()
            zig_zag_order[-1].append(current_node.val)

            if is_clockwise:
                if current_node.left:
                    next_level.append(current_node.left)
                if current_node.right:
                    next_level.append(current_node.right)
            else:
                if current_node.right:
                    next_level.append(current_node.right)
                if current_node.left:
                    next_level.append(current_node.left)
        is_clockwise = (not is_clockwise)
        current_level = next_level
        next_level = []
    return zig_zag_order


if __name__ == "__main__":
    test_tree = TreeNode(3)
    test_tree.left = TreeNode(9)
    test_tree.right = TreeNode(20)
    test_tree.right.left = TreeNode(15)
    test_tree.right.right = TreeNode(7)

    print(zigzagLevelOrder(test_tree))
