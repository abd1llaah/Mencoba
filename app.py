import streamlit as st
import time

# ======================
# Circular Linked List
# ======================
class Node:
    def __init__(self, warna, durasi):
        self.warna = warna
        self.durasi = durasi
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, warna, durasi):
        node_baru = Node(warna, durasi)

        if not self.head:
            self.head = node_baru
            node_baru.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node_baru
            node_baru.next = self.head


# ======================
# Setup Lampu
# ======================
def buat_lampu():
    cll = CircularLinkedList()
    cll.tambah("Merah", 40)
    cll.tambah("Hijau", 20)
    cll.tambah("Kuning", 5)
    return cll


# ======================
# Streamlit UI
# ======================
st.title("Simulasi Lampu Lalu Lintas 🚦")

cll = buat_lampu()
node = cll.head

placeholder = st.empty()

# Loop simulasi
while True:
    if node.warna == "Merah":
        warna_emoji = "🔴"
    elif node.warna == "Hijau":
        warna_emoji = "🟢"
    else:
        warna_emoji = "🟡"

    placeholder.markdown(f"## Lampu {node.warna} {warna_emoji}")
    placeholder.write(f"Durasi: {node.durasi} detik")

    time.sleep(node.durasi)
    node = node.next
