class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

    def preorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            result.append(root.value)
            self.preorder(root.left, result)
            self.preorder(root.right, result)
        return result

    def inorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            self.inorder(root.left, result)
            result.append(root.value)
            self.inorder(root.right, result)
        return result

    def postorder(self, root, result=None):
        if result is None:
            result = []
        if root:
            self.postorder(root.left, result)
            self.postorder(root.right, result)
            result.append(root.value)
        return result


print("=" * 55)
print("       BINARY SEARCH TREE - TRAVERSAL")
print("=" * 55)

tree = BST()
data_awal = [50, 30, 70, 20, 40, 60, 80]

for item in data_awal:
    tree.root = tree.insert(tree.root, item)

print(f"\nData awal : {data_awal}")
print("-" * 55)
print("TRAVERSAL AWAL (sebelum penambahan node baru):")
print(f"  Preorder  : {tree.preorder(tree.root)}")
print(f"  Inorder   : {tree.inorder(tree.root)}")
print(f"  Postorder : {tree.postorder(tree.root)}")

# TUGAS 2: Tambahkan node baru: 10, 90, 65
print("\n" + "=" * 55)
print("MENAMBAHKAN NODE BARU: 10, 90, 65")
print("=" * 55)

node_baru = [10, 90, 65]
for item in node_baru:
    tree.root = tree.insert(tree.root, item)
    print(f"  [+] Node {item} berhasil ditambahkan")

# TUGAS 3: Tampilkan traversal setelah penambahan
print("\n" + "-" * 55)
print("TRAVERSAL SETELAH PENAMBAHAN NODE BARU:")
pre  = tree.preorder(tree.root)
ino  = tree.inorder(tree.root)
post = tree.postorder(tree.root)
print(f"  Preorder  : {pre}")
print(f"  Inorder   : {ino}")
print(f"  Postorder : {post}")



# TUGAS 4: Analisis perubahan hasil traversal
print("\n" + "=" * 55)
print("ANALISIS PERUBAHAN TRAVERSAL")
print("=" * 55)
print("""
  1. PREORDER (Root → Kiri → Kanan):
     Sebelum: [50, 30, 20, 40, 70, 60, 80]
     Sesudah: [50, 30, 20, 10, 40, 70, 60, 65, 80, 90]
     -> Node 10 muncul setelah 20 (anak kiri 20)
     -> Node 65 muncul setelah 60 (anak kanan 60)
     -> Node 90 muncul setelah 80 (anak kanan 80)

  2. INORDER (Kiri → Root → Kanan):
     Sebelum: [20, 30, 40, 50, 60, 70, 80]
     Sesudah: [10, 20, 30, 40, 50, 60, 65, 70, 80, 90]
     -> Selalu terurut NAIK (sifat utama BST)
     -> Node baru otomatis masuk di posisi yang benar

  3. POSTORDER (Kiri → Kanan → Root):
     Sebelum: [20, 40, 30, 60, 80, 70, 50]
     Sesudah: [10, 20, 40, 30, 65, 60, 90, 80, 70, 50]
     -> Root (50) selalu muncul paling akhir
     -> Setiap subtree diproses tuntas sebelum parent-nya

  ANALISIS KESIMPULAN:
     - Inorder selalu menghasilkan urutan terurut pada BST, dia ini tidak berubah, cuma bertambah 3 elemen baru di posisi yang benar
     - Preorder dan Postorder berubah karena path traversal melewati cabang baru (10 di bawah 20, 65 di bawah 60, 90 di bawah 80)
     - Penambahan node itu engga ngubah posisi node yang lama, tapi cuma nambahin cabang di leaf aja
""")



# TUGAS 5: Visualisasi tree (text-based)
print("=" * 55)
print("VISUALISASI TREE (setelah semua node ditambahkan)")
print("=" * 55)

def visualize_tree(root, prefix="", is_left=True):
    if root is None:
        return
    if root.right:
        visualize_tree(root.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(root.value))
    if root.left:
        visualize_tree(root.left, prefix + ("    " if is_left else "│   "), True)

print()
visualize_tree(tree.root)

print("\nStruktur posisi node:")
print("""
                  50          ← Root
                /    \\
              30      70
             /  \\    /  \\
           20   40  60   80
           /       \\      \\
          10        65     90
""")
print("Node baru: 10, 65, 90 (ditandai miring)")
print("=" * 55)
