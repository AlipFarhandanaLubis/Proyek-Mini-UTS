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
