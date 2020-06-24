# Python3 program to find largest subtree
# sum in a given binary tree.

# Function to create new tree node.
class NewNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# Helper function to find largest
# subtree sum recursively.
def findLargestSubtreeSumUtil(node, ans):
    # If current node is None then
    # return 0 to parent node.
    if (node == None):
        return 0

    # Subtree sum rooted at current node.
    curr_sum = (node.data + findLargestSubtreeSumUtil(node.left, ans) + findLargestSubtreeSumUtil(node.right, ans))

    # Update answer if current subtree
    # sum is greater than answer so far.
    ans = max(ans, curr_sum)

    # Return current subtree sum to
    # its parent node.
    return curr_sum

# Function to find largest subtree sum.
def findLargestSubtreeSum(root):

    # If tree does not exist,
    # then answer is 0.
    if not root:
        return 0

    # Variable to store maximum subtree sum.
    ans = -999999999999

    # Call to recursive function to
    # find maximum subtree sum.
    findLargestSubtreeSumUtil(root, ans)

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

    print(findLargestSubtreeSum(root))
