# Python3 program to find largest subtree
# sum in a given binary tree.

# Function to create new tree node.
class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None


# A iterative function to do postorder traversal of
# a given binary tree
def postOrderIterative(node):
    # Check for empty tree
    if node is None:
        return

    ans = []
    stack = []

    while (True):
        while (node):
            # Push node's right child and then node to stack
            if node.right is not None:
                stack.append(node.right)
            stack.append(node)
            # Set node as node's left child
            node = node.left

        # Pop an item from stack and set it as node
        node = stack.pop()
        # If the popped item has a right child and the
        # right child is not processed yet, then make sure
        # right child is processed before node
        if node.right is not None and peek(stack) == node.right:
            stack.pop()  # Remove right child from stack
            stack.append(node)  # Push node back to stack
            node = node.right  # change node so that the
            # righ childis processed next

        # Else print node's data and set node as None
        else:
            ans.append(node.data)
            node = None

        if len(stack) <= 0:
            break
    return ans


# Driver Code
if __name__ == "__main__":
    root = NewNode(1)
    root.left = NewNode(-2)
    root.right = NewNode(3)
    root.left.left = NewNode(4)
    root.left.right = NewNode(5)
    root.right.left = NewNode(-6)
    root.right.right = NewNode(2)

    print("Post Order traversal of binary tree is", postOrderIterative(root))
