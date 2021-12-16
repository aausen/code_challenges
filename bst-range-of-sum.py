#given class TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def rangeSumBST(root, low, high):
        # new list of nums in the given range
        # traverse the bst
        # check if each node falls between range of low and high
        # if in the range, add to new list
        # loop through new list and add them all together
        # return the sum of the new list
        nums_in_range = []
        
        to_visit = [root]
        
        while to_visit:
            current = to_visit.pop()
            
            
            if current.val <= high and current.val >= low:
                nums_in_range.append(current.val)
            if current.left is not None:
                to_visit.append(current.left)
            if current.right is not None:
                to_visit.append(current.right)
    
        return sum(nums_in_range)