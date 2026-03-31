# 📊 DRAM Simulation Dashboard

Simulation tool for the **Dynamic Misalignment Mechanism of Regulatory Fatigue (DRAM)** built using Streamlit.

---

## 🚀 Overview

This application simulates how the gap between:

* **Intentional Direction (ID)**
* **Affective Regulation (AR)**

creates **misalignment** and accumulates into **fatigue over time**.

---

## 🧰 Requirements

Pastikan sudah terinstall:

* Python 3.8 atau lebih baru
* pip (Python package manager)

Cek versi Python:

```bash
python --version
```

---

## 📦 Step 1 — Clone / Download Project

Kalau pakai Git:

```bash
git clone https://github.com/your-repo/dram-simulation.git
cd dram-simulation
```

Atau download manual lalu masuk ke folder project:

```bash
cd dram-simulation
```

---

## 📦 Step 2 — Buat Virtual Environment (Recommended)

```bash
python -m venv venv
```

Aktifkan:

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

---

## 📦 Step 3 — Install Dependencies

```bash
pip install streamlit pandas matplotlib
```

---

## 📁 Step 4 — Pastikan Struktur File

```bash
.
├── app.py
└── README.md
```

---

## ▶️ Step 5 — Jalankan Aplikasi

```bash
streamlit run app.py
```

---

## 🌐 Step 6 — Buka di Browser

Biasanya otomatis terbuka. Kalau tidak:

```
http://localhost:8501
```

---

## ⚙️ Cara Menggunakan

Di sidebar, kamu bisa ubah parameter:

* **Initial ID** → nilai awal tujuan
* **Initial AR** → regulasi awal
* **α (Adjustment Rate)** → kecepatan adaptasi AR
* **Δ (Constraint)** → perubahan ID tiap iterasi
* **Iterations** → jumlah langkah simulasi

---

## 📈 Output yang Ditampilkan

* Grafik:

  * ID
  * AR
  * Fatigue
* Tabel data simulasi
* Tombol download CSV

---

## 📥 Export Data

Klik tombol:

```
📥 Download CSV
```

Untuk menyimpan hasil simulasi.

---

## 🧠 Model Formula

* AR update:

  ```
  AR = AR + α(ID - AR)
  ```

* ID update:

  ```
  ID = ID + Δ
  ```

* Misalignment:

  ```
  ID - AR
  ```

* Fatigue:

  ```
  Fatigue += |Misalignment|
  ```

---

## 👨‍💻 Author

* Jumadil Awal
* Abdul Azis

---

## 💡 Notes

* Cocok untuk simulasi behavioral system
* Bisa dikembangkan jadi research model
* Bisa ditambahkan export grafik / PDF

---

## 🛠 Troubleshooting

### ❌ streamlit not recognized

```bash
pip install streamlit
```

### ❌ Port already in use

```bash
streamlit run app.py --server.port 8502
```

---

Enjoy exploring DRAM 🚀
