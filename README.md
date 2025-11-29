BISA BANGET ✨
Aku bikin README yang **lebih rapih, profesional, minimalis, dan enak dibaca**.
Silakan copas ini untuk repo kamu ya 👇

---

### 📌 README.md — Hitung Nilai Akhir & Grade

````markdown
# 🧮 Program Hitung Nilai Akhir & Grade

Program ini menghitung nilai akhir siswa berdasarkan tiga komponen penilaian:

| Komponen | Bobot |
|---------|-------|
| Tugas   | 30%   |
| UTS     | 30%   |
| UAS     | 40%   |

Setelah nilai dihitung, program menentukan kategori **grade** sebagai berikut:

| Nilai Akhir | Grade | Keterangan |
|------------:|:-----:|------------|
| ≥ 85        | A     | Sangat Baik |
| 70 – 84     | B     | Baik |
| 60 – 69     | C     | Cukup |
| 50 – 59     | D     | Kurang |
| 40 – 49     | E     | Sangat Kurang |

Selain menampilkan grade, program juga mencetak huruf grade sesuai jumlah pengulangan tertentu:
- A → dicetak **1 kali**
- B → **2 kali**
- C → **3 kali**
- D → **4 kali**
- E → **5 kali**

---

## 🧑‍💻 Kode Program

```python
def hitungNilai(tugas, uts, uas):
    nilaiAkhir = (0.3*tugas) + (0.3*uts) + (0.4*uas)
    
    if nilaiAkhir >= 85:
        grade = 'A'
    elif nilaiAkhir >= 70 and nilaiAkhir <= 84:
        grade = 'B'
    elif nilaiAkhir >= 60 and nilaiAkhir <= 69:
        grade = 'C'
    elif nilaiAkhir >= 50 and nilaiAkhir <= 59:
        grade = 'D'
    elif nilaiAkhir >= 40 and nilaiAkhir <= 49:
        grade = "E"

    ulang = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
    for i in range(ulang[grade]):
        print(grade)

hitungNilai(78, 67, 75)
````

---

## ▶️ Cara Menjalankan Program

1. Install Python (jika belum ada)
2. Simpan kode dalam file: `nilai.py`
3. Jalankan lewat terminal / CMD:

```bash
python nilai.py
```

---

## 📌 Contoh Output

```
B
B
```

Karena nilai akhir masuk kategori **B** → dicetak 2 kali.

---

## ✍️ Identitas

* **Nama** : Rishy Khoerunnisa
* **Kelas** : XI DKV
* **Mata Pelajaran** : Dasar Pemrograman
* **Project** : Tugas Hitung Nilai Akhir

---

## 🚀 Pengembangan Selanjutnya

Program dapat ditingkatkan dengan fitur:

* Input nilai dari user
* Validasi nilai (0–100)
* Menampilkan predikat dan status kelulusan

---
ntuk project lain juga? Tinggal bilang repo mana ✨
```
