"""First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree."""

from graph_and_trees import BinaryTreeNode


def fst_common_anc(
    root: BinaryTreeNode, node1: BinaryTreeNode, node2: BinaryTreeNode
) -> BinaryTreeNode:
    """return the first common ancestor of two nodes"""

    a, b, node = fst_anc_rec(root, node1, node2)
    return node


def fst_anc_rec(root: BinaryTreeNode, node1: BinaryTreeNode, node2: BinaryTreeNode):

    left_found_n1, left_found_n2, left_anc = None, None, None
    right_found_n1, right_found_n2, right_anc = None, None, None
    if root.left:
        left_found_n1, left_found_n2, left_anc = fst_anc_rec(root.left, node1, node2)

    if root.right:
        right_found_n1, right_found_n2, right_anc = fst_anc_rec(
            root.right, node1, node2
        )

    if left_anc is not None:
        return left_found_n1, left_found_n2, left_anc
    if right_anc is not None:
        return right_found_n1, right_found_n2, right_anc

    found_n1 = left_found_n1 or right_found_n1
    found_n2 = left_found_n2 or right_found_n2

    ancestor = None
    if found_n1 and found_n2:
        ancestor = root

    found_n1 = found_n1 or root.value == node1
    found_n2 = found_n2 or root.value == node2

    return found_n1, found_n2, ancestor


def _gen_tree_1():
    tree = BinaryTreeNode(1)
    tree.left = BinaryTreeNode(2)
    tree.right = BinaryTreeNode(9)
    tree.right.left = BinaryTreeNode(10)
    tree.left.left = BinaryTreeNode(3)
    tree.left.right = BinaryTreeNode(7)
    tree.left.right.right = BinaryTreeNode(5)
    tree.left.left.left = BinaryTreeNode(6)
    tree.left.right.left = BinaryTreeNode(12)
    tree.left.right.left.left = BinaryTreeNode(16)
    tree.left.right.left.right = BinaryTreeNode(0)
    return tree


test_cases = [
    (_gen_tree_1, 7, 12, 2),
]


def test_first_ancestor():
    for root, n1, n2, result in test_cases:
        assert result == fst_common_anc(root(), n1, n2).value


if __name__ == "__main__":
    test_first_ancestor()
