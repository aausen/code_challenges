# Given BST class
class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def is_binary_search_tree(root):
    # move through the tree
    # check if each left node is less than ancestor
    # check if each right node is greater than ancestor
    # if all yes, return true
    # if not, return false

    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False

        if node.left:
            node_and_bounds_stack.append((node.left, lower_bound, node.value))

        if node.right:
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    return True

# What I did:
# the binary search tree class was given
# create a stack to keep track of which node we are on and 
# the upper and lower bounds in a set
# use a while loop while there is something in the stack
# assign the variables
# if the node is less than the lower bound or greater
# than the upper bound, then it is not a valid bst
# if it is the left node, append it to the stack and update the lower bound
# if it is the right node, append it to the stack and update the upper bound
# if all passes, return true