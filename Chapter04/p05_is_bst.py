''' A binary search tree is a binary tree in which every node fits a specific ordering property:
all left descendents <= n < all right descendents. This must be true for each node n.
Validate BST: Implement a function to check if a binary tree is a binary search tree.'''

from graph_and_trees import BinaryTreeNode

def is_bst(root:BinaryTreeNode, min_val=None, max_val=None):

    if root is None:
        return True

    if (min_val and root.value < min_val) or (max_val and root.value >= max_val):
        return False

    return is_bst(root.left,min_val,root.value) and is_bst(root.right,root.value,max_val)
