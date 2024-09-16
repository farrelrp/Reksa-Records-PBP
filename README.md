Deployed : http://farrel-reksa-reksasrecords.pbp.cs.ui.ac.id/

## A. Step-by-step Implementasi Checklist

1. **Membuat Repository Git**
   - Buat repo baru di GitHub dan ambil URL Git-nya.
   - Buat direktori baru bernama `record-store` lalu jalankan command `git init` agar direktori tersebut menjadi folder Git.

2. **Inisiasi Remote Origin**
   - Tambahkan remote origin dengan URL Git repo yang sudah dibuat.

3. **Membuat Virtual Environment**
   - Jalankan `python -m venv env` di direktori yang sama untuk membuat file virtual environment.

4. **Mengaktifkan Virtual Environment**
   - Aktifkan virtual environment dengan command `env\Scripts\activate`.

5. **Menginstal Dependencies**
   - Buat file `requirements.txt` yang berisi semua package yang menjadi dependency untuk proyek ini.
   - Jalankan command `pip install -r requirements`.

6. **Membuat Proyek Django**
   - Buat proyek Django baru dengan nama `record-store` menggunakan command `django-admin startproject record-store .`.

7. **Membuat `.gitignore`**
   - Buat file `.gitignore` untuk mengabaikan file yang tidak ingin dilacak Git.

8. **Membuat App "Main"**
   - Jalankan `python manage.py startapp main` untuk membuat direktori aplikasi.

9. **Mendaftarkan App ke `INSTALLED_APPS`**
   - Tambahkan `'main'` ke `INSTALLED_APPS` di file `settings.py`.

10. **Membuat Model VinylRecord**
    - Isi file `models.py` dengan membuat objek `VinylRecord` beserta fieldsnya.

11. **Melakukan Migrasi Database**
    - Run command `python manage.py makemigrations` dan `python manage.py migrate` untuk meng-update database sesuai dengan model.

12. **Membuat Fungsi di Views**
    - Di `views.py`, buat fungsi untuk menerima input dari `VinylRecord` dengan method `.all` dan mengassign-nya ke sebuah variabel, lalu berikan konteks ke `main` dengan mengisi fungsi `show_main`.

13. **Menambahkan Routing pada Level Proyek**
    - Tambahkan `path('', include('main.urls'))` di `urlpatterns` pada `urls.py` direktori proyek.

14. **Menambahkan Routing pada Level App**
    - Tambahkan `path('', show_main, name='show_main')` di `urlpatterns` pada `urls.py` direktori aplikasi.

15. **Commit dan Push ke Repo GitHub**
    - Lakukan commit dan push ke repo di GitHub.

16. **Deploy ke PWS**
    - Buat proyek baru di PWS.
    - Tambahkan remote PWS dengan link yang didapatkan di PWS.

17. **Konfigurasi Settings untuk PWS**
    - Tambahkan URL PWS ke `ALLOWED_HOSTS` di `settings.py`.

18. **Push ke PWS**
    - Push ke PWS untuk memulai deployment.

---

## B. Bagan Request Client ke Web Aplikasi Django

![Diagram MVT)](https://github.com/user-attachments/assets/7ff49fc3-9445-4c69-a9d1-affde2390071)


---

## C. Jelaskan Fungsi git Dalam Pengembangan Perangkat Lunak!

Git berfungsi sebagai sebuah sistem version control yang dilakukan untuk melacak dan menunjukkan perubahan yang terjadi pada sebuah code base. Fungsi utama git adalah sebagai alat kolaborasi antar developer supaya dapat membuat versi - versi yang terpisah sesuai dengan kebutuhan (_branching_) tanpa risiko merusak versi utama (_main branch_). Git juga akan dilakukan untuk melakukan penggabungan versi - versi terpisah ini (_merging_) ketika semua perubahan telah direview (_pull request_).

---

## D. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Django merupakan framework yang sudah memiliki banyak fitur bawaan yang sangat berguna seperti CMS dengan django admin dan database bawaan.
- Django juga memiliki struktur yang jelas melalui sistem MVT (Model - View - Template) dimana kita dapat belajar bagaimana masing - masing komponen di sebuah website itu berjalan dengan jelas. 
- Django menggunakan bahasa python yang relatif mudah dan sudah kita dapat di DDP1.
- Django memiliki komunitas yang cukup aktif sehingga ketika kita memiliki pertanyaan atau mencari sumber belajar secara online cukup mudah.



## E. Mengapa Model pada Django Disebut sebagai ORM?

Model pada Django disebut sebagai ORM atau Object-Relational Mapping karena cara kerja model adalah menghubungkan objek-objek di dalam kode Python dengan tabel-tabel di dalam database relasional. Django juga menangani konversi dari objek Python ke data yang dapat diolah dengan SQL.
