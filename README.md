# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri.

### Permasalahan Bisnis

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut. 

### Cakupan Proyek

Hasil akhir (output) yang diharapkan dari proyek ini diantaranya:
- Attrition analysis
- Business dashboard
- Prediction model

### Persiapan

Sumber data: [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment - Anaconda:

conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

## Business Dashboard

Link Dashboard: [Attrition Rate Dashboard](https://public.tableau.com/app/profile/tio.syaifuddin/viz/AttritionAnalysis_17163525302120/Dashboard1)

Dashboard ini berfungsi untuk melakukan analisis terhadap Attrition Rate dari pegawai. Dengan memfokuskan pembagian berdasarkan Job Role untuk melakukan analisis yang lebih terkhusus. Beberapa faktor yang telah dipilih melalui proses pengeksplorasian data yang telah dilakukan sebelumnya diantaranya sebagai berikut: 
- Tingkat kepuasan pegawai terhadap lingkungan/pekerjaan/relasi.
- Hubungan antara umur dengan pendapatan per bulan.
- Frekuensi bepergian untuk urusan kerja (business travel).
- Status pernikahan.
- Kerja lembur.

Dashboard ini terdiri chart utama, filter, dan chart tambahan.

2 Chart utama menampilkan gambaran secara umum:
- Pie chart yang menampilkan proporsi pegawai yang melakukan atrisi dengan yang tidak.
- Clustered Bar chart yang menampilkan jumlah pegawai yang melakukan atrisi yang dikelompokkan berdasarkan Job Role. Pengguna juga dapat melihat informasi dari tingkat kepuasan pegawai yang akan tampil pada bagian tooltip.

1 filter:
- Berfungsi untuk memfilter data berdasarkan Job Role. Untuk memfokuskan analisis kedalam Job Role tertentu.

4 Chart tambahan:
- Scatter plot yang menampilkan korelasi antara umur dengan pendapatan perbulan yang juga menampilkan trendline dari hubungan dua variabel tersebut.
- Pie chart

## Conclusion

Beberapa kesimpulan yang didapatkan diantaranya:
- Pegawai dengan usia muda (25 - 35 tahun) merupakan rentang umur yang paling banyak melakukan atrisi. Dengan pendapatan perbulan yang relatif rendah (di bawah trend line).
- Pegawai yang sering bepergian untuk urusan kerja lebih berpotensi untuk melakukan atrisi.
- Pegawai yang belum menikah (single) cenderung lebih sering melakukan atrisi.
- 1 dari 3 pegawai yang bekerja secara overtime (lembur) melukan atrisi.
- Sales Representative memliki tingkat atrisi yang paling tinggi (hampir mencapai 50 %). Dengan tingkat kepuasan kerja yang kurang baik bagi mereka yang melakukan atrisi.
- 6 dari 9 Job Role, pegawai yang melakukan atrisi merasa kurang nyaman dengan lingkungan kerjanya.

### Rekomendasi Action Items

- Sesuaikan uang kompensasi dengan usia dari pegawai. Pegawai dengan umur yang lebih tua cenderung membutuhkan biaya hidup yang lebih tinggi.
- Tingkatkan kualitas environment kerja. Seperti peningkatan sarana dan prasarana di kantor. Atau kegiatan kebersamaan yang dapat meningkatkan bonding antar karyawan.
- Karyawan dengan Job Role Sales Representative harus lebih diperhatikan. Bisa dengan mengusahakan untuk mengurangi adanya kerja overtime yang menjadi penyumbang yang cukup banyak dalam porsi karyawan yang melakukan atrisi.

## Cara Menggunakan Script Python Untuk Prediksi

- Buka file prediction.py menggunakan IDE yang anda punya.
- Install seluruh library yang tertulis pada file requirement.txt
- Ubah lokasi dari dataset sesuai dengan lokasi penyimpanan anda (terdapat comment line diatas baris kode tersebut). Note: file harus dalam ekstensi CSV.
- Jalankan scripty python tersebut.
- Done. Periksa file CSV anda, terdapat kolom prediksi yang berada di bagian kolom paling kanan.