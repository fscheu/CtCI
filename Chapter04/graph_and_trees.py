""" Data Structures implementations"""


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None, parent=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.value}\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()


class BinaryTree:
    def __init__(self, head=None) -> None:
        self.root = head

    def add(self, value, parent) -> BinaryTreeNode:

        new_node = BinaryTreeNode(value)
        if self.root is None:
            self.root = new_node
            return self.root

        if parent.left is None:
            parent.left = new_node
            new_node.parent = parent
        elif parent.right is None:
            parent.right = new_node
            new_node.parent = parent
        else:
            raise Exception("No more than two childs allowed")
        return new_node

class BinarySearchTree:
    def __init__(self, head=None) -> None:
        self.root = head
    
    def add(self, value=None):
        new_node = BinaryTreeNode(value)
        if not self.root:
            self.root = new_node
            return new_node

        parent = self.root
        while parent:
            if parent.value > value:
                if not parent.left:
                    parent.left = new_node
                    new_node.parent = parent
                    return new_node
                parent = parent.left
            else:
                if not parent.right:
                    parent.right = new_node
                    new_node.parent = parent
                    return new_node
                parent = parent.right

    def get_node(self,value):
        current = self.root
        while current:
            if current.value == value:
                return current
            if current.value > value:
                current = current.left
            else:
                current = current.right
        return None


class Node:
    def __init__(self, value=None, neighbors=None) -> None:
        self.value = value
        self.neighbors = [] if neighbors is None else neighbors


class Graph:
    def __init__(self, nodes=None) -> None:
        self.nodes = [] if nodes is None else nodes

    def add_node(self, node: Node):
        self.nodes.append(node)
