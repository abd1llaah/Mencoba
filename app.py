import streamlit as st
from graphviz import Digraph

# =========================
# Node Class
# =========================
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# =========================
# BST Class
# =========================
class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root

    # PREORDER
    def preorder(self, root, result):
        if root:
            result.append(root.value)
            self.preorder(root.left, result)
            self.preorder(root.right, result)

    # INORDER
    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append(root.value)
            self.inorder(root.right, result)

    # POSTORDER
    def postorder(self, root, result):
        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result.append(root.value)

# =========================
# Fungsi Visualisasi Tree
# =========================
def draw_tree(node, graph=None):
    if graph is None:
        graph = Digraph()
        graph.attr("node", shape="circle")

    if node:
        graph.node(str(node.value))

        if node.left:
            graph.edge(str(node.value), str(node.left.value))
            draw_tree(node.left, graph)

        if node.right:
            graph.edge(str(node.value), str(node.right.value))
            draw_tree(node.right, graph)

    return graph

# =========================
# STREAMLIT APP
# =========================
st.title("Visualisasi Binary Search Tree (BST)")

# Data awal
data_awal = [50, 30, 70, 20, 40, 60, 80]

# Input tambahan
input_user = st.text_input(
    "Masukkan node tambahan (pisahkan dengan koma)",
    "10,90,65"
)

# Proses input
tambahan = []

if input_user:
    tambahan = [int(x.strip()) for x in input_user.split(",")]

# Membuat BST
tree = BST()

for item in data_awal:
    tree.root = tree.insert(tree.root, item)

for item in tambahan:
    tree.root = tree.insert(tree.root, item)

# Traversal
pre = []
ino = []
post = []

tree.preorder(tree.root, pre)
tree.inorder(tree.root, ino)
tree.postorder(tree.root, post)

# Tampilkan hasil traversal
st.subheader("Hasil Traversal")

st.write("Preorder:")
st.code(" ".join(map(str, pre)))

st.write("Inorder:")
st.code(" ".join(map(str, ino)))

st.write("Postorder:")
st.code(" ".join(map(str, post)))

# Visualisasi BST
st.subheader("Visualisasi Tree")

graph = draw_tree(tree.root)

st.graphviz_chart(graph)
