
# CASE 1: Red node with red child
#   - if uncle is red: make grandpa red, and both it's children black
#       - then check if the grandpa or uncle causes a violation

# CASE 2: red node with red child
#   - if uncle node is black
#   - if the new node is the left child of a right child, or right child of a left child
#       - then rotate the parent with the new node. then apply CASE 3

# CASE 3: red node with red child
#   - if uncle is black
#   - if the new node is a left child of a left child, or right child of a right child
#       - then rotate the parent with the grandparent, and flip their colors


class Node:

    def __init__(self, val=None, parent=None, left=None, right=None, is_red=True):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.is_red = is_red

    def set_left(self, node):
        self.left = node
        node.parent = self

    def set_right(self, node):
        self.right = node
        node.parent = self

    def __str__(self):
        string = ("Node: %s; Is Red: %s; " % (self.val, self.is_red))
        if self.parent:
            string += ("Parent: %s; " % (self.parent.val))
        if self.left:
            string += ("Left: %s; " % (self.left.val))
        if self.right:
            string += ("Right: %s; " % (self.right.val))
        return (string)


class RBT:

    def __init__(self, root=None):
        self.root = root

    def rotate(self, node):
        """Perform a left or right rotation.
        """
        # set the parent nodes.
        print("Rotating %s" % (node))
        parent = node.parent
        grandparent = parent.parent
        if grandparent:
            print("Found Grandparent: %s\nNode: %s" % (grandparent, node))
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node
            node.parent = grandparent
        else:
            node.parent = None
            self.root = node
        parent.parent = node

        if parent.left == node:
            parent.left = node.right
            node.right = parent
        else:
            parent.right = node.left
            node.left = parent

        node_color = node.is_red
        parent_color = parent.is_red

        node.is_red = parent_color
        parent.is_red = node_color
        print(node)
        print("Parent: %s" % (parent))
        if parent.left:
            self._validate(parent.left)
        if parent.right:
            self._validate(parent.right)
        return parent

    def _uncle_is_red(self, node):
        """Make the grandparent red, the uncle black, and the parent black.
        """
        if node != self.root:
            node.parent.parent.is_red = True
            node.parent.parent.left.is_red = False
            node.parent.parent.right.is_red = False
        # recurse on grandparent
        self._validate(node.parent.parent)

    def _uncle_is_black_triangle(self, node):
        """Rotate the parent with the new node, then apply zig-zag.
        """
        node = self.rotate(node)
        # parent_node.parent = node
        self._uncle_is_black_straight(node)

    def _uncle_is_black_straight(self, node):
        """Rotate the parent with the grandparent, and flip their colors.
        """
        self.rotate(node.parent)

    def _validate(self, node):
        if node.is_red and node.parent and node.parent.is_red:
            print("Not Valid: %s" % (node))
            if node.parent.parent and node.parent.parent.left and node.parent.parent.right:
                print("Uncle found for %s" % (node))
                if node.parent.parent.left.is_red and node.parent.parent.right.is_red:
                    print("Uncle is red.")
                    # CASE 1: Uncle is RED.
                    self._uncle_is_red(node)
                elif node.val < node.parent.val < node.parent.parent.val \
                        or node.val > node.parent.val > node.parent.parent.val:
                    print("Uncle is black. Path to node is straight.")
                    # CASE 2: Uncle is BLACK - straight grandchild.
                    self._uncle_is_black_straight(node)
                else:
                    print("Uncle is black. Path to node is triangle.")
                    # CASE 3: Uncle is BLACK - triangle grandchild.
                    self._uncle_is_black_triangle(node)
            elif node.parent.parent:
                print("No uncle found for %s" % (node))
                if node.val < node.parent.val < node.parent.parent.val \
                        or node.val > node.parent.val > node.parent.parent.val:
                    print("Straight grandchild.")
                    # CASE 5: No uncle - straight grandchild.
                    self._uncle_is_black_straight(node)
                else:
                    print("Triangle grandchild.")
                    # CASE 5: No uncle - triangle grandchild.
                    self._uncle_is_black_triangle(node)
        if self.root.is_red:
            self.root.is_red = False
        return node

    def insert(self, val):
        if not self.root:
            new_node = Node(val, is_red=False)
            self.root = new_node
            return new_node
        else:
            new_node = Node(val)
            current_node = self.root
            while not new_node.parent:
                if new_node.val == current_node.val:
                    return None
                elif new_node.val < current_node.val:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.set_left(new_node)
                        self._validate(new_node)
                        return new_node
                elif new_node.val > current_node.val:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.set_right(new_node)
                        self._validate(new_node)
                        return new_node

    def get(self, val):
        """TODO: Do the thing.
        """
        pass


if __name__ == "__main__":
    red_black_tree = RBT()
    print(red_black_tree.insert(4))
    # print(red_black_tree.insert(2))
    print(red_black_tree.insert(5))
    # print(red_black_tree.insert(3))
    print(red_black_tree.insert(6))
    print(red_black_tree.insert(8))
