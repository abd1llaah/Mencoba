import streamlit as st

# =========================
# NODE CLASS
# =========================
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# =========================
# BST CLASS
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
# VISUALISASI TREE TANPA GRAPHVIZ
# =========================
def tampil_tree(node, level=0, posisi="Root"):
    if node is not None:

        spasi = "&nbsp;" * 8 * level

        st.markdown(
            f"{spasi}📍 **{posisi}: {node.value}**",
            unsafe_allow_html=True
        )

        tampil_tree(node.left, level + 1, "L")
        tampil_tree(node.right, level + 1, "R")

# =========================
# STREAMLIT APP
# =========================
st.title("Binary Search Tree (BST)")

# Data awal
data_awal = [50, 30, 70, 20, 40, 60, 80]

# Input node tambahan
input_user = st.text_input(
    "Masukkan node tambahan (pisahkan koma)",
    "10,90,65"
)

# Konversi input
tambahan = []

if input_user:
    tambahan = [int(x.strip()) for x in input_user.split(",")]

# Membuat BST
tree = BST()

for item in data_awal:
    tree.root = tree.insert(tree.root, item)

for item in tambahan:
    tree.root = tree.insert(tree.root, item)

# =========================
# TRAVERSAL
# =========================
pre = []
ino = []
post = []

tree.preorder(tree.root, pre)
tree.inorder(tree.root, ino)
tree.postorder(tree.root, post)

# =========================
# TAMPILKAN HASIL
# =========================
st.subheader("Traversal")

st.write("Preorder")
st.code(" ".join(map(str, pre)))

st.write("Inorder")
st.code(" ".join(map(str, ino)))

st.write("Postorder")
st.code(" ".join(map(str, post)))

# =========================
# VISUALISASI TREE
# =========================
st.subheader("Visualisasi Tree")

tampil_tree(tree.root)
