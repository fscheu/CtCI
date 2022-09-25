""" A binary search tree is a binary tree in which every node fits a specific ordering property:
all left descendents <= n < all right descendents. This must be true for each node n.
Validate BST: Implement a function to check if a binary tree is a binary search tree."""

from graph_and_trees import BinaryTreeNode
from p02_minimal_height import create_binary


def is_bst(root: BinaryTreeNode, min_val=None, max_val=None):
    """Checks if a BinaryTree is a binary search tree. Returns True or False"""
    if root is None:
        return True

    if (min_val and root.value < min_val) or (max_val and root.value >= max_val):
        return False

    return is_bst(root.left, min_val, root.value) and is_bst(
        root.right, root.value, max_val
    )


test_cases = [
    ([1, 2, 3, 4, 5, 6, 7], True),
    ([7, 3, 8, 4, 9, 1, 10, 0, 2, 5, 6], False),
]


def test_is_bst():

    for tree, result in test_cases:
        root = create_binary(tree, 0, len(tree) - 1)
        assert is_bst(root) == result


if __name__ == "__main__":
    test_is_bst()
