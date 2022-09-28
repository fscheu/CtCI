"""Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node
in a binary search tree. You may assume that each node has a link to its parent."""

from graph_and_trees import BinaryTreeNode, BinarySearchTree


def left_most_child(node):
    """Return the left most child of a given node"""
    next_node = node
    while next_node.left:
        next_node = next_node.left
    return next_node


def find_successor(node: BinaryTreeNode):
    """return the next node in-order traversal"""
    if node.right:
        # if it has a right child, return the left most node
        return left_most_child(node.right)

    if node.parent:

        if node == node.parent.left:
            # if this node was a left child the next node is the parent
            return node.parent

        # if this node was the right child the next node is the next
        # right-left most sibling
        next_node = node.parent
        while next_node.parent and next_node == next_node.parent.right:
            next_node = next_node.parent
        return next_node.parent

    return None

def test_in_order_successor():
    bst = BinarySearchTree()
    bst.add(20)
    bst.add(9)
    bst.add(25)
    bst.add(5)
    bst.add(12)
    bst.add(11)
    bst.add(14)

    # Test all nodes
    inputs = [5, 9, 11, 12, 14, 20, 25]
    outputs = inputs[1:]
    outputs.append(None)

    for x, y in zip(inputs, outputs):
        test = bst.get_node(x)
        succ = find_successor(test)
        if succ is not None:
            assert succ.value == y
        else:
            assert succ == y

if __name__ == "__main__":
    test_in_order_successor()            