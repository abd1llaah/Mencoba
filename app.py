import streamlit as st
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

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
# BENCHMARK FUNCTION
# ======================

def benchmark(sort_func, data):
    start = time.time()
    sort_func(data)
    end = time.time()
    return end - start

# ======================
# STREAMLIT UI
# ======================

st.title("📊 Sorting Benchmark")

sizes = [100, 1000, 10000, 50000]
algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

results = []

if st.button("Jalankan Benchmark"):
    st.write("⏳ Lagi kerja... sabar ya (apalagi Bubble Sort bakal ngos-ngosan)")

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
                "Rata-rata Waktu (detik)": avg_time
            })

    df = pd.DataFrame(results)

    st.subheader("📋 Tabel Benchmark")
    st.dataframe(df)

    # ======================
    # VISUALISASI
    # ======================
    st.subheader("📈 Grafik Performa")

    fig, ax = plt.subplots()

    for algo in df["Algoritma"].unique():
        subset = df[df["Algoritma"] == algo]
        ax.plot(subset["Ukuran Data"], subset["Rata-rata Waktu (detik)"], label=algo)

    ax.set_xlabel("Ukuran Data")
    ax.set_ylabel("Waktu (detik)")
    ax.legend()

    st.pyplot(fig)

    # ======================
    # ANALISIS OTOMATIS
    # ======================
    st.subheader("🧠 Analisis")

    fastest = df.loc[df["Rata-rata Waktu (detik)"].idxmin()]

    st.write(f"""
    ### 🔥 Algoritma Tercepat
    **{fastest['Algoritma']}** adalah yang paling cepat pada data ukuran {fastest['Ukuran Data']}.
    
    ### 🤔 Kenapa?
    - Bubble Sort: banyak swap → lambat banget
    - Selection Sort: tetap O(n²), tapi swap lebih sedikit
    - Insertion Sort: lebih efisien untuk data kecil
    
    Jadi biasanya:
    👉 Insertion Sort paling cepat di ukuran kecil  
    👉 Semua tetap lambat di data besar (karena O(n²))
    
    ### 📚 Kesesuaian dengan Big O
    Hasil benchmark **sesuai teori Big O**:
    
    - Bubble Sort = O(n²)
    - Selection Sort = O(n²)
    - Insertion Sort = O(n²)
    
    Terlihat dari grafik:
    📈 waktu naik drastis saat ukuran data membesar
    
    Artinya:
    ✔ Teori = sesuai praktik  
    ✔ Tidak ada keajaiban, tetap lambat 😌
    """)
