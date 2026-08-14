# Laporan Project 10 — Data Cleaning dan Normalisasi Nama Presenter

## 1. Tujuan

Project 10 bertujuan untuk membersihkan dataset yang berisi data presenter dan project/news package. Fokus utama proses cleaning adalah memperbaiki inkonsistensi penulisan nama presenter sehingga data dapat digunakan untuk analisis lebih lanjut.

Proses dilakukan menggunakan Python dan Pandas di Google Colab.

## 2. Dataset

Dataset yang digunakan adalah `sample-file.csv`.

Data awal memiliki:

* Jumlah baris: 399
* Jumlah kolom: 3
* Kolom:

  * `Timestamp`
  * `Name of person presenting`
  * `Name of project/news package`

Pada pemeriksaan awal tidak ditemukan missing value pada ketiga kolom.

## 3. Pemeriksaan Data Awal

Pemeriksaan awal dilakukan untuk mengetahui kondisi dataset sebelum proses cleaning.

### Missing Value

Hasil pemeriksaan:

| Kolom                        | Missing |
| ---------------------------- | ------: |
| Timestamp                    |       0 |
| Name of person presenting    |       0 |
| Name of project/news package |       0 |

Tidak ditemukan missing value pada dataset awal.

### Duplicate Data

Ditemukan 53 data duplicate pada pemeriksaan awal.

Hal ini menunjukkan bahwa terdapat beberapa baris yang memiliki data yang sama dan perlu diperhatikan dalam proses cleaning.

## 4. Cleaning Dasar

Tahap pertama dilakukan dengan membersihkan whitespace pada kolom `Name of person presenting`.

Tujuannya adalah menghilangkan perbedaan yang hanya disebabkan oleh spasi tambahan, misalnya:

* `Leona Medina`
* `Leona Medina `

Kedua nilai tersebut secara substantif merujuk pada nama yang sama sehingga dapat distandarisasi.

Setelah cleaning dasar, ditemukan 89 nilai nama unik.

## 5. Identifikasi Nama yang Tidak Konsisten

Setelah cleaning dasar, ditemukan berbagai bentuk penulisan nama yang berbeda.

Contohnya:

* `Tim`
* `Timmy`
* `Timothy Campbell`
* `Tim Campbell`

Contoh lainnya:

* `Gordon Barry`
* `Gordon Berry`
* `Gordon Bary`
* `Gordon Bery`

Selain perbedaan ejaan, ditemukan pula variasi berupa nama pendek, inisial, penggunaan tanda baca, serta kesalahan pengetikan.

Karena itu, proses normalisasi tidak dilakukan hanya berdasarkan kemiripan teks. Konteks pada baris data juga digunakan untuk menghindari penggabungan nama orang yang berbeda.

## 6. Normalisasi Nama

Normalisasi dilakukan menggunakan mapping dengan Pandas.

Beberapa contoh normalisasi:

| Nama awal          | Nama hasil normalisasi |
| ------------------ | ---------------------- |
| Alexander          | Alex Castillo          |
| Alexander Castillo | Alex Castillo          |
| Evelyn             | Evelyn Wong            |
| Gordon Berry       | Gordon Barry           |
| Jacqueline Estrada | Jackie Estrada         |
| Jacqueline         | Jacqueline Jacobs      |
| Jacqueline J       | Jacqueline Jacobs      |
| Sam Terry          | Samantha Terry         |
| Teresa Coats       | Theresa Coates         |
| Kari               | Kari Ballard           |
| Kari B.            | Kari Ballard           |

Mapping dilakukan berdasarkan pola data dan konteks presenter, bukan hanya berdasarkan kemiripan karakter.

## 7. Validasi Kelompok Nama

Setelah proses normalisasi, dilakukan pemeriksaan terhadap kelompok nama yang memiliki kemiripan.

Tahap ini penting karena tidak semua nama yang terlihat mirip harus digabung.

Beberapa nama yang tetap dipertahankan sebagai entitas berbeda adalah:

* `Deanna Zimmerman`
* `Diana Zimmerman`
* `Carrie Ballard`
* `Kari Ballard`

Keputusan tersebut dibuat untuk menghindari penggabungan data yang tidak memiliki bukti cukup bahwa nama tersebut merujuk pada orang yang sama.

## 8. Penanganan Data Tidak Valid

Ditemukan satu nilai yang tidak sesuai dengan konteks kolom presenter:

`Out of Eden Walk`

Pemeriksaan terhadap baris tersebut menunjukkan:

| Kolom                        | Nilai             |
| ---------------------------- | ----------------- |
| Timestamp                    | 4/20/17 17:14     |
| Name Original                | Out of Eden Walk  |
| Name of person presenting    | Out of Eden Walk  |
| Name of project/news package | Jacqueline Jacobs |

`Out of Eden Walk` bukan nama presenter dan merupakan nilai yang salah masuk ke kolom `Name of person presenting`.

Karena tidak terdapat bukti yang cukup untuk menentukan siapa presenter sebenarnya, nilai tersebut tidak dipaksakan menjadi nama tertentu. Nilai tersebut ditandai sebagai missing value.

Pendekatan ini dipilih untuk menjaga integritas data.

## 9. Hasil Akhir

Setelah seluruh proses cleaning dan normalisasi dilakukan, diperoleh:

* Jumlah baris: 399
* Jumlah kolom: 3
* Nama presenter unik: 25
* Missing presenter: 1

Distribusi presenter akhir:

| Presenter                       | Jumlah |
| ------------------------------- | -----: |
| Sheila Rhodes and Jacob Wheeler |     21 |
| Andrew Vasquez                  |     20 |
| Theresa Coates                  |     19 |
| Gordon Barry                    |     19 |
| Candice Washington              |     19 |
| Shana Lindsey                   |     18 |
| Samantha Terry                  |     18 |
| Jackie Estrada                  |     18 |
| Tim Campbell                    |     17 |
| Hattie Garrett                  |     17 |
| Evelyn Wong                     |     17 |
| Lizzie Hodges                   |     16 |
| Jacqueline Jacobs               |     16 |
| Olga Woods                      |     16 |
| Rod Velasco                     |     16 |
| Alex Castillo                   |     16 |
| Katrina Singleton               |     16 |
| Wilma Husseini-Howard           |     16 |
| Leona Medina                    |     16 |
| Natasha Roberson                |     16 |
| Deanna Zimmerman                |     15 |
| Sonya Mann                      |     15 |
| Carrie Ballard                  |      8 |
| Kari Ballard                    |      7 |
| Diana Zimmerman                 |      6 |

## 10. Output

Dataset hasil cleaning disimpan sebagai:

`project10_final_clean.csv`

File tersebut merupakan dataset yang telah melalui proses:

1. Pemeriksaan struktur dataset.
2. Pemeriksaan missing value.
3. Pemeriksaan duplicate.
4. Pembersihan whitespace.
5. Identifikasi variasi nama.
6. Normalisasi nama menggunakan mapping.
7. Validasi nama berdasarkan konteks.
8. Identifikasi data presenter yang tidak valid.
9. Penanganan nilai presenter yang tidak dapat ditentukan.
10. Validasi akhir jumlah nama unik.

## 11. Kesimpulan

Project 10 menunjukkan bahwa proses data cleaning tidak hanya berupa menghapus data kosong atau duplicate. Pada dataset ini, masalah utama terdapat pada inkonsistensi penulisan nama presenter.

Dengan menggunakan Pandas, variasi nama dapat distandarisasi melalui mapping yang dibuat berdasarkan pola dan konteks data. Proses validasi juga digunakan agar nama yang berbeda tidak secara sembarangan digabungkan.

Hasil akhir menghasilkan 25 nama presenter yang valid dengan 1 nilai presenter yang ditandai sebagai missing karena tidak dapat ditentukan secara akurat dari data yang tersedia.

Dataset hasil cleaning kemudian disimpan sebagai `project10_final_clean.csv` dan dapat digunakan sebagai dataset yang lebih siap untuk tahap analisis berikutnya.
