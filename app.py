import streamlit as st
import time

st.title("Simulasi Lampu Lalu Lintas 🚦")

# Data lampu: (nama, durasi, emoji)
lampu = [
    ("Merah", 5, "🔴"),
    ("Hijau", 3, "🟢"),
    ("Kuning", 2, "🟡")
]

placeholder = st.empty()

# Tombol start
if st.button("Start"):
    for _ in range(3):  # jumlah putaran
        for warna, durasi, emoji in lampu:
            for sisa in range(durasi, 0, -1):
                placeholder.markdown(f"## {warna} {emoji}")
                placeholder.write(f"Sisa waktu: {sisa} detik")
                time.sleep(1)
