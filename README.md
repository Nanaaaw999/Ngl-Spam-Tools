
# NGL Spam Tool V1.0 - Pink Edition

![Pink Edition](https://img.shields.io/badge/Edition-Pink-pink)
![Version](https://img.shields.io/badge/Version-1.0-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellowgreen)

Alat ini dirancang untuk mengirim pesan anonim ke pengguna NGL dengan berbagai mode spam dan opsi yang dapat disesuaikan.

## Preview

### 1. Tampilan Utama Program
![Tampilan Utama](images/preview-1-main-screen.png)

### 2. Menu Utama
![Menu Utama](images/preview-2-main-menu.png)

### 3. Pemilihan Mode Spam
![Mode Spam](images/preview-3-spam-modes.png)

### 4. Proses Pengiriman Spam
![Proses Pengiriman](images/preview-4-progress-bar.png)

### 5. Laporan Selesai
![Laporan Selesai](images/preview-5-completion-log.png)

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

## Persyaratan

- Python 3.x
- Modul Python:
  - `requests`
  - `pystyle`

## Instalasi

1. Clone atau download repositori ini
2. Install modul yang diperlukan:
```bash
pip install requests pystyle
```
3. Jalankan script:
```bash
python ngl_spam_tool.py
```

## Cara Penggunaan

1. Jalankan script dan masukkan username Anda
2. Pilih opsi dari menu utama:
   - **Start Spam** - Mulai mengirim pesan spam
   - **View Information** - Lihat informasi tentang alat ini
   - **Exit** - Keluar dari program

3. Jika memilih "Start Spam":
   - Pilih mode spam yang diinginkan
   - Masukkan username target
   - Masukkan pesan yang ingin dikirim
   - Masukkan jumlah pesan yang ingin dikirim
   - Konfirmasi untuk memulai pengiriman

## File yang Dihasilkan

- `history.txt` - File log yang berisi semua sesi spam yang telah dilakukan

## Peringatan

Alat ini hanya untuk tujuan pendidikan. Gunakan dengan tanggung jawab dan jangan menyalahgunakan untuk tujuan yang merugikan orang lain.

**Disclaimer**: Spam pacarmu jika dia tidak membalas chatmu! 😉

## Pembuat

Dibuat oleh NANAW

## Lisensi

Proyek ini tidak memiliki lisensi khusus. Gunakan dengan bijak.
```