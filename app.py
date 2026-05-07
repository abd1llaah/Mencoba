import streamlit as st

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

    def insert(self, root, value):

        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        return root


# =========================
# POSISI NODE
# =========================
def get_positions(root, x=0, y=0, pos=None, level_gap=2):

    if pos is None:
        pos = []

    if root:
        pos.append((root.value, x, y))

        if root.left:
            get_positions(root.left, x - level_gap, y - 1, pos, level_gap / 2)

        if root.right:
            get_positions(root.right, x + level_gap, y - 1, pos, level_gap / 2)

    return pos


# =========================
# VISUALISASI TREE
# =========================
def draw_tree(root):

    positions = get_positions(root)

    html = """
    <div style='position:relative; width:100%; height:500px;'>
    """

    center_x = 400
    center_y = 50

    for value, x, y in positions:

        left = center_x + (x * 120)
        top = center_y + (-y * 100)

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

    st.markdown(html, unsafe_allow_html=True)


# =========================
# STREAMLIT
# =========================
st.title("Binary Search Tree Visualization")

# INPUT
input_data = st.text_input(
    "Masukkan angka (pisahkan koma)",
    "50,20,60"
)

# KONVERSI INPUT
data = [int(x.strip()) for x in input_data.split(",")]

# MEMBUAT TREE
tree = BST()

for item in data:
    tree.root = tree.insert(tree.root, item)

# TAMPILKAN TREE
st.subheader("Visualisasi Tree")

draw_tree(tree.root)
