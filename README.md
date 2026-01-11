## ANGGOTA KELOMPOK
1. Geugeut Nyarikawanti Surahmat (103132400002)
   Bertanggungjawab atas pembuatan poster dan membangun source code
3. Wahyuni Salsabila (103132400010)
   Bertanggungjawab atas penentuan dan analisis dataset serta membangun source code

---

## Deskripsi
Program ini merupakan implementasi Sistem Pendukung Keputusan untuk menentukan kelayakan rumah tinggal menggunakan metode Fuzzy Mamdani. Sistem fuzzy digunakan untuk menangani ketidakpastian dalam penilaian kelayakan berdasarkan beberapa kriteria yang bersifat linguistik.

---

## Study Case
Penentuan kelayakan rumah tinggal sering kali tidak bersifat tegas (layak atau tidak layak), melainkan berada pada tingkat tertentu. Faktor seperti pendapatan, usia rumah, dan jumlah ruangan biasanya dinilai secara subjektif. Oleh karena itu, pendekatan fuzzy logic digunakan untuk meniru cara berpikir manusia dalam pengambilan keputusan.

---

## Dataset
Dataset yang digunakan merupakan **House Price Prediction Dataset** yang diambil dari Kaggle.
Pada implementasi ini, hanya tiga atribut yang digunakan, yaitu:
- Avg. Area Income
- Avg. Area House Age
- Avg. Area Number of Rooms

Atribut lain seperti harga rumah, alamat, jumlah kamar tidur, dan populasi area tidak digunakan karena tidak berpengaruh langsung terhadap penilaian kelayakan hunian.

---

## Metode Fuzzy
Sistem fuzzy dibangun menggunakan pendekatan **Fuzzy Mamdani** dengan tahapan sebagai berikut:
1. Membaca data dari file CSV
2. Fuzzifikasi nilai input
3. Inferensi menggunakan aturan IF–THEN
4. Defuzzifikasi menggunakan metode Centroid (Center of Gravity)
5. Menyimpan hasil output ke dalam file
   
---

## Analisis Sistem Fuzzy
Sistem fuzzy diimplementasikan dengan tiga atribut utama, yaitu pendapatan, usia rumah, dan jumlah ruangan, karena ketiganya secara langsung mempengaruhi kelayakan hunian serta mudah direpresentasikan dalam bentuk linguistik. Fungsi keanggotaan segitiga digunakan untuk setiap atribut input dan output agar transisi antar kategori berlangsung secara halus dan tidak kaku. Aturan inferensi dirancang untuk meniru pola penalaran manusia, di mana kombinasi pendapatan tinggi, usia rumah yang masih baru, dan jumlah ruangan yang cukup menghasilkan tingkat kelayakan yang tinggi. Proses defuzzifikasi menggunakan metode Centroid (Center of Gravity) karena metode ini mempertimbangkan seluruh area keanggotaan output, sehingga menghasilkan nilai kelayakan yang stabil dan representatif. Dengan desain tersebut, sistem mampu memberikan perubahan nilai kelayakan secara bertahap ketika nilai input berubah, sesuai dengan prinsip fuzzy logic.

---

## Cara Menjalankan Program
Buka terminal pada folder project kemudian jalankan perintah "python main.py" 
