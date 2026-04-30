import streamlit as st
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# ======================
# UI AWAL (HARUS MUNCUL DULU)
# ======================
st.title("📊 Sorting Benchmark")
st.write("Bandingkan Bubble, Selection, dan Insertion Sort")

# ======================
# SORTING
# ======================
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

# ======================
# BENCHMARK
# ======================
def benchmark(sort_func, data):
    times = []
    for _ in range(3):
        arr = data.copy()
        start = time.time()
        sort_func(arr)
        end = time.time()
        times.append(end - start)
    return sum(times) / 3

# ======================
# SIMPAN HASIL
# ======================
if "results" not in st.session_state:
    st.session_state.results = []

# ======================
# PILIH DATA
# ======================
sizes = [100, 1000, 10000, 50000]

st.subheader("⚙️ Jalankan per ukuran data")

for size in sizes:
    if st.button(f"Run n = {size}"):

        with st.spinner(f"Processing n={size}... jangan panik 😭"):

            # generate data DI DALAM tombol (ini penting!)
            data = [random.randint(1, 100000) for _ in range(size)]

            # benchmark
            bubble = benchmark(bubble_sort, data)
            selection = benchmark(selection_sort, data)
            insertion = benchmark(insertion_sort, data)

            # simpan
            st.session_state.results.append({
                "Ukuran": size,
                "Bubble": bubble,
                "Selection": selection,
                "Insertion": insertion
            })

            st.success(f"Selesai n={size}")

# ======================
# TAMPILKAN HASIL
# ======================
if st.session_state.results:
    df = pd.DataFrame(st.session_state.results)

    st.subheader("📋 Tabel Benchmark")
    st.dataframe(df)

    # ======================
    # GRAFIK
    # ======================
    st.subheader("📈 Grafik")

    fig, ax = plt.subplots()
    ax.plot(df["Ukuran"], df["Bubble"], label="Bubble")
    ax.plot(df["Ukuran"], df["Selection"], label="Selection")
    ax.plot(df["Ukuran"], df["Insertion"], label="Insertion")

    ax.set_xlabel("Ukuran Data")
    ax.set_ylabel("Waktu (detik)")
    ax.legend()

    st.pyplot(fig)

    # ======================
    # ANALISIS
    # ======================
    st.subheader("🧠 Analisis")

    avg = df[["Bubble", "Selection", "Insertion"]].mean()
    fastest = avg.idxmin()

    st.write(f"🏆 Algoritma tercepat: **{fastest}**")

    st.write("""
📌 **Mengapa?**  
Insertion Sort lebih efisien dalam pergeseran data dibanding Bubble dan Selection, sehingga sering lebih cepat pada data kecil-menengah.

📌 **Apakah sesuai Big O?**  
Ya. Ketiga algoritma memiliki kompleksitas O(n²).  
Namun dalam praktik, waktu eksekusi bisa berbeda karena jumlah operasi nyata tiap algoritma tidak sama.
""")
