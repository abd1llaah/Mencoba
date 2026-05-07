import streamlit as st
import streamlit.components.v1 as components

# =========================
# NODE
# =========================
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# =========================
# BST
# =========================
class BST:
    def __init__(self):
        self.root = None

    # INSERT NODE
    def insert(self, root, value):

        # Jika tree kosong
        if root is None:
            return Node(value)

        # Masuk ke kiri
        if value < root.value:
            root.left = self.insert(root.left, value)

        # Masuk ke kanan
        else:
            root.right = self.insert(root.right, value)

        return root

    # =========================
    # PREORDER
    # =========================
    def preorder(self, root, result):

        if root:
            result.append(root.value)

            self.preorder(root.left, result)
            self.preorder(root.right, result)

    # =========================
    # INORDER
    # =========================
    def inorder(self, root, result):

        if root:
            self.inorder(root.left, result)

            result.append(root.value)

            self.inorder(root.right, result)

    # =========================
    # POSTORDER
    # =========================
    def postorder(self, root, result):

        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)

            result.append(root.value)


# =========================
# POSISI NODE
# =========================

def get_positions(root, x=0, y=0, pos=None, parent=None, gap=4):

    if pos is None:
        pos = []

    if root:

        pos.append((root.value, x, y, parent))

        if root.left:
            get_positions(
                root.left,
                x - gap,
                y + 1,
                pos,
                root.value,
                gap / 2
            )

        if root.right:
            get_positions(
                root.right,
                x + gap,
                y + 1,
                pos,
                root.value,
                gap / 2
            )

    return pos

# =========================
# VISUALISASI TREE
# =========================
def draw_tree(root):

    positions = get_positions(root)

    html = """
    <div style="
        position:relative;
        width:100%;
        height:500px;
        background:white;
    ">
    """

    center_x = 400
    center_y = 50

    coords = {}

    # =========================
    # POSISI NODE
    # =========================
    for value, x, y, parent in positions:

        left = center_x + (x * 150)
        top = center_y + (y * 100)

        coords[value] = (left, top)

    # =========================
    # GARIS PENGHUBUNG
    # =========================
    for value, x, y, parent in positions:

        if parent is not None:

            x1, y1 = coords[parent]
            x2, y2 = coords[value]

            html += f"""
            <svg style="
                position:absolute;
                left:0;
                top:0;
                width:100%;
                height:100%;
                overflow:visible;
            ">
                <line
                    x1="{x1+30}"
                    y1="{y1+30}"
                    x2="{x2+30}"
                    y2="{y2+30}"
                    stroke="black"
                    stroke-width="3"
                />
            </svg>
            """

    # =========================
    # NODE BULAT
    # =========================
    for value, x, y, parent in positions:

        left, top = coords[value]

        html += f"""
        <div style="
            position:absolute;
            left:{left}px;
            top:{top}px;
            width:60px;
            height:60px;
            border-radius:50%;
            background:#4CAF50;
            color:white;
            text-align:center;
            line-height:60px;
            font-size:24px;
            font-weight:bold;
        ">
            {value}
        </div>
        """

    html += "</div>"

    components.html(html, height=500)


# =========================
# STREAMLIT
# =========================
st.title("Binary Search Tree Visualization")

# DATA BST
data = [50, 30, 70, 20, 40, 60, 80]

# MEMBUAT BST
tree = BST()

for item in data:
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
# HASIL TRAVERSAL
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

draw_tree(tree.root)
