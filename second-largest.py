# Class given
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

#________________________________________________________

def find_largest(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right

def find_second_largest(root_node):
    if (root_node is None or 
            (root_node.left is None and root_node.right is None)):
            raise ValueError("Tree must have at least two nodes")

    current = root_node

    while current:
        if current.left and not current.right:
            return find_largest(current.left)
        
        if (current.right and 
                not current.right.left and
                not current.right.right):
            return current.value
        current = current.right

# to find the second largest root node, we must find the largest root node
# since it is a bst the largest will be all the way down on the
# right side. To get there we start at the root node and 
# use current.right to keep traversing to the right.
# When there is no long a current.right.right and the current.left does not 
# have another right, our current will the the second largest.
# if there is only a left branch, we must find the largest of that
# section to find the second largest (because it would be less than
# the ancestor, so the largest in this branch would be the second largest)
# to find the largest, we create a helper funciton that uses current to find the 
# right most node