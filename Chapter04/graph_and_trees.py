''' Data Structures implementations'''

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

class Node:
    def __init__(self, value=None, neighbors=None) -> None:
        self.value = value
        self.neighbors = [] if neighbors is None else neighbors

class Graph:
    def __init__(self, nodes=None) -> None:
        self.nodes = [] if nodes is None else nodes

    def add_node(self, node:Node):
        self.nodes.append(node)
