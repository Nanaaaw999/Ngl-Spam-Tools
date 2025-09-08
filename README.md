
# NGL Spam Tool V1.0 - Pink Edition

![Pink Edition](https://img.shields.io/badge/Edition-Pink-pink)
![Version](https://img.shields.io/badge/Version-1.0-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellowgreen)

Alat ini dibuat menggunakan **Python** dan dirancang khusus untuk mengirim pesan anonim ke pengguna NGL dengan berbagai mode spam dan opsi yang dapat disesuaikan. Dengan antarmuka yang menarik dan fitur-fitur canggih, alat ini memberikan pengalaman yang unik.

## Fitur

- 🎨 **Tema Pink** - Antarmuka yang menarik dengan tema pink dan ASCII art anime
- ⚡ **Berbagai Mode Spam**:
  - Normal Spam (1.0s delay)
  - Fast Spam (0.5s delay)
  - Brutal Spam (0.1s delay)
  - Super Brutal Spam (0.01s delay)
  - Ultra Super Brutal Spam (0.0s delay)
  - Custom Mode (delay sesuai keinginan)
- 😊 **Emoji Acak** - Setiap pesan akan dikirim dengan emoji acak
- 📝 **Pencatatan Sesi** - Semua aktivitas akan dicatat ke file history.txt
- 🔒 **Rotasi Device ID** - Untuk anonimitas yang lebih baik
- 📊 **Progress Bar** - Menampilkan progress pengiriman pesan secara real-time

## Persyaratan Sistem

Sebelum menjalankan script ini, pastikan sistem Anda memenuhi persyaratan berikut:

- **Python 3.x** - Script ini dibuat dan dijalankan menggunakan bahasa pemrograman Python.
- Modul Python eksternal:
  - `requests` - Untuk melakukan permintaan HTTP ke server NGL.
  - `pystyle` - Untuk memberikan warna dan gaya pada teks di terminal.

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan alat ini:

1. Pastikan Anda telah menginstal Python 3.x di komputer Anda.
2. Clone atau download repositori ini ke komputer lokal Anda.
3. Buka terminal atau command prompt, arahkan ke direktori proyek.
4. Install modul Python yang diperlukan dengan perintah:
```bash
pip install requests pystyle
```
5. Setelah instalasi selesai, jalankan script Python dengan perintah:
```bash
python ngl_spam_tool.py
```

## Cara Penggunaan

1. Jalankan script dan masukkan username Anda saat diminta.
2. Anda akan melihat menu utama dengan pilihan berikut:
   - **Start Spam** - Untuk memulai sesi pengiriman pesan spam.
   - **View Information** - Untuk melihat informasi detail mengenai alat ini.
   - **Exit** - Untuk keluar dari program.

3. Jika Anda memilih "Start Spam":
   - Pilih mode spam yang diinginkan dari daftar yang tersedia.
   - Masukkan username target NGL.
   - Ketikkan pesan yang ingin Anda kirimkan.
   - Tentukan jumlah pesan yang akan dikirim.
   - Konfirmasi pilihan Anda untuk memulai pengiriman pesan.

## File yang Dihasilkan

- `history.txt` - File log yang secara otomatis dibuat untuk mencatat semua sesi spam yang telah Anda lakukan, termasuk waktu, target, pesan, dan status pengiriman.

## Peringatan

Alat ini dibuat untuk tujuan pembelajaran dan edukasi mengenai otomatisasi permintaan web. Gunakan dengan tanggung jawab penuh dan jangan menyalahgunakan untuk tujuan yang dapat merugikan atau mengganggu orang lain. Pengguna bertanggung jawab penuh atas segala tindakan yang dilakukan menggunakan alat ini.

**Disclaimer**: Spam pacarmu jika dia tidak membalas chatmu! 😉

## Pembuat

Dibuat oleh NANAW menggunakan Python.

## Lisensi

Proyek ini tidak memiliki lisensi khusus. Gunakan dengan bijak dan tanggung jawab.
```