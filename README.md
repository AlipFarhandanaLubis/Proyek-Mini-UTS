# Proyek-Mini-UTS
Program ini digunakan untuk mengonversi jumlah uang dalam Rupiah (IDR) ke beberapa mata uang asing, yaitu:
- USD (Dollar Amerika)
- SGD (Dollar Singapura)
- EUR (Euro)

### 📌 Cara Kerja Program
User memasukkan jumlah uang dalam IDR, kemudian program otomatis menghitung nilai konversi berdasarkan kurs yang telah ditentukan.

### 🧮 Kurs yang Digunakan
| Mata Uang | Nilai Kurs (IDR) |
|----------|------------------|
| USD      | 15.000           |
| SGD      | 11.000           |
| EUR      | 16.000           |

### 💻 Contoh Kode Program

# Sistem Konversi Mata Uang

mata_uang = ["USD", "SGD", "EUR"]
kurs_usd = 15000
kurs_sgd = 11000
kurs_eur = 16000

idr = int(input("Masukkan jumlah uang dalam IDR: "))
for m in mata_uang:
    if m == "USD":
        hasil = idr / kurs_usd
    elif m == "SGD":
        hasil = idr / kurs_sgd
    elif m == "EUR":
        hasil = idr / kurs_eur
    print(f"{m}: {hasil:.2f}")
![WhatsApp Image 2025-11-07 at 22 32 54_cf92a68a uts](https://github.com/user-attachments/assets/0cc31ed4-5610-4ade-b10d-39cf6003fff9)
