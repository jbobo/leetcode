"""Python3 program to check if a given Binary Tree is symmetric or not
"""

class newNode:
    """Helper function that allocates a new node with the given data and None
    left and right pairs.
    """

    def __init__(self, key):
        """Constructor to create a new node.
        """
        self.key = key
        self.left = None
        self.right = None


# function to check if a given
# Binary Tree is symmetric or not
def isSymmetric(root):
    # if tree is empty
    if (root == None):
        return True

    # If it is a single tree node,
    # then it is a symmetric tree.
    if (not root.left and not root.right):
        return True

    queue = []

    # Add root to queue two times so that
    # it can be checked if either one
    # child alone is NULL or not.
    queue.append(root)
    queue.append(root)

    # To store two nodes for checking
    # their symmetry.
    leftNode = 0
    rightNode = 0

    while (not len(queue)):

        # Remove first two nodes to
        # check their symmetry.
        leftNode = queue[0]
        queue.pop(0)

        rightNode = queue[0]
        queue.pop(0)

        # if both left and right nodes
        # exist, but have different
        # values-. inequality, return False
        if leftNode.key != rightNode.key:
            return False

        # append left child of left subtree
        # node and right child of right
        # subtree node in queue.
        if leftNode.left and rightNode.right:
            queue.append(leftNode.left)
            queue.append(rightNode.right)

        # If only one child is present
        # alone and other is NULL, then
        # tree is not symmetric.
        elif leftNode.left or rightNode.right:
            return False

        # append right child of left subtree
        # node and left child of right subtree
        # node in queue.
        if leftNode.right and rightNode.left:
            queue.append(leftNode.right)
            queue.append(rightNode.left)

        # If only one child is present
        # alone and other is NULL, then
        # tree is not symmetric.
        elif leftNode.right or rightNode.left:
            return False

    return True


if __name__ == "__main__":
    """Driver Code"""
    # Let us construct the Tree
    # shown in the above figure
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(2)
    root.left.left = newNode(3)
    root.left.right = newNode(4)
    root.right.left = newNode(4)
    root.right.right = newNode(3)
    if isSymmetric(root):
        print("The given tree is Symmetric")
    else:
        print("The given tree is not Symmetric")
