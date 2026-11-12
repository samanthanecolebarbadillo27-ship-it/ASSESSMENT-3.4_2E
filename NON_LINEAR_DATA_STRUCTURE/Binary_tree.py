
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = deque()
        queue.append(self.root)

        while len(queue) > 0:
            current = queue.popleft()

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def bfs(self):
        order = []
        queue = deque()
        queue.append(self.root)

        while len(queue) > 0:
            current = queue.popleft()
            order.append(current)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return order

    def dfs(self, node, order):
        if node is None:
            return
        order.append(node.data)
        self.dfs(node.left, order)
        self.dfs(node.right, order)


tree = BinaryTree()
tree.insert("B1")
tree.insert("A1")
tree.insert("R")
tree.insert("B2")
tree.insert("A2")
tree.insert("D")
tree.insert("I")
tree.insert("L1")
tree.insert("L2")
tree.insert("O")

print("=== BINARY TREE ===")
bfs_nodes = tree.bfs()
for node in bfs_nodes:
    children = []
    if node.left is not None:
        children.append(node.left.data)
    if node.right is not None:
        children.append(node.right.data)

    if len(children) > 0:
        print(node.data + ": " + ", ".join(children))
    else:
        print(node.data + ": -")

bfs_order = []
for node in bfs_nodes:
    bfs_order.append(node.data)

dfs_order = []
tree.dfs(tree.root, dfs_order)

print("BFS: " + " -> ".join(bfs_order))
print("DFS: " + " -> ".join(dfs_order))