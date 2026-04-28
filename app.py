import streamlit as st
import random
import time
import pandas as pd

# ======================
# SORTING ALGORITHMS
# ======================

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
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
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

# ======================
# BENCHMARK
# ======================

def benchmark(sort_func, data):
    start = time.time()
    sort_func(data)
    end = time.time()
    return end - start

# ======================
# UI
# ======================

st.title("📊 Sorting Benchmark (Tanpa Matplotlib, santai aja)")

sizes = [100, 1000, 10000, 50000]
algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

results = []

if st.button("Jalankan Benchmark"):
    st.write("⏳ Lagi jalan... jangan berharap Bubble Sort cepat ya.")

    for size in sizes:
        data = [random.randint(1, 100000) for _ in range(size)]

        for name, func in algorithms.items():
            times = []
            for _ in range(3):
                t = benchmark(func, data)
                times.append(t)

            avg_time = sum(times) / len(times)

            results.append({
                "Ukuran Data": size,
                "Algoritma": name,
                "Waktu": avg_time
            })

    df = pd.DataFrame(results)

    # ======================
    # TABEL
    # ======================
    st.subheader("📋 Tabel Benchmark")
    st.dataframe(df)

    # ======================
    # GRAFIK (Streamlit)
    # ======================
    st.subheader("📈 Grafik Performa")

    chart_data = df.pivot(index="Ukuran Data", columns="Algoritma", values="Waktu")
    st.line_chart(chart_data)

    # ======================
    # ANALISIS
    # ======================
    st.subheader("🧠 Analisis")

    fastest = df.loc[df["Waktu"].idxmin()]

    st.write(f"""
    ### 🔥 Algoritma Tercepat
    **{fastest['Algoritma']}** adalah yang paling cepat.

    ### 🤔 Kenapa?
    - Bubble Sort → terlalu banyak swap → paling lambat
    - Selection Sort → tetap O(n²), tapi lebih stabil
    - Insertion Sort → efisien di data kecil

    Jadi:
    👉 Insertion Sort biasanya menang di ukuran kecil  
    👉 Semua tetap melemah di ukuran besar

    ### 📚 Big O
    Semua algoritma ini punya kompleksitas:
    - O(n²)

    Dari grafik:
    ✔ Waktu meningkat drastis saat data bertambah  
    ✔ Sesuai teori Big O  

    Kesimpulan:
    Tidak ada plot twist. Semua tetap lambat 😌
    """)
