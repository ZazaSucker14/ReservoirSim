# Reservoir Fluid Simulation

## Deskripsi
Reservoir Fluid Simulation adalah program untuk mensimulasikan penurunan tekanan dalam reservoir berdasarkan parameter seperti permeabilitas, viskositas fluida, laju aliran, dan panjang reservoir.

## Fitur
1. **Input Data Reservoir:** Membaca data dari file CSV.
2. **Simulasi Penurunan Tekanan:** Menghitung penurunan tekanan menggunakan hukum Darcy.
3. **Visualisasi Hasil:** Menampilkan grafik hasil simulasi.
4. **Ekspor Data:** Menyimpan hasil simulasi dalam file CSV.

## Cara Menjalankan
1. Pastikan Python 3 terinstal.
2. Install dependensi:
   ```bash
   pip install pandas matplotlib
   ```
3. Jalankan program:
   ```bash
   python main.py
   ```

## Struktur Folder
```
ReservoirFluidSimulation/
├── data/
├── src/
└── main.py