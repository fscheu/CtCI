'''Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that t
he heights of the two subtrees of any node never differ by more than one.'''

from graph_and_trees import BinaryTreeNode

def is_balanced(root:BinaryTreeNode):

    if root is None:
        return True, 0

    left_balanced, left_height = is_balanced(root.left)
    right_balanced, right_height = is_balanced(root.right)

    new_balance = left_balanced and right_balanced and abs(left_height - right_height) <= 1
    new_height = max(left_height, right_height)+1
    return new_balance, new_height

def _gen_balanced_1():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    return root


def _gen_balanced_2():
    root = BinaryTreeNode(7)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(8)
    root.right.right = BinaryTreeNode(9)
    root.right.right.right = BinaryTreeNode(10)
    return root


def _gen_unbalanced_1():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.left.right.right = BinaryTreeNode(6)
    root.left.right.right.right = BinaryTreeNode(7)
    root.right = BinaryTreeNode(3)
    root.right.left = BinaryTreeNode(8)
    root.right.right = BinaryTreeNode(9)
    root.right.right.right = BinaryTreeNode(10)
    root.right.right.right.right = BinaryTreeNode(11)
    return root


def _gen_unbalanced_2():
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
    (_gen_balanced_1, True),
    (_gen_balanced_2, True),
    (_gen_unbalanced_1, False),
    (_gen_unbalanced_2, False),
]

def test_is_balanced():
    for tree_gen, expected in test_cases:
        error_msg = f"{is_balanced.__name__} failed on {tree_gen.__name__}"
        balance, height = is_balanced(tree_gen())
        assert balance == expected, error_msg

if __name__ == "__main__":
    test_is_balanced()
