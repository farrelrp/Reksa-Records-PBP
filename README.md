**Deployed : http://farrel-reksa-reksasrecords.pbp.cs.ui.ac.id/**

# Tugas 1

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

# Tugas 2

## A. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Dalam platform modern yang seringkali membutuhkan satu komponen untuk berbicara dengan komponen lain, perlu ada sistem yang dapat membantu proses itu terjadi. Tanpa data delivery, platform tersebut tidak akan dapat menyajikan informasi yang dibutuhkan pengguna. Dalam contoh di projek ini, data delivery dibutuhkan supaya user dapat mendapatkan informasi yang paling baru tentang item apa saja yang dijual. Selain itu, pengguna juga perlu tahu apakah item tersebut ada di stok atau tidak.

Di sisi lain, pengguna juga butuh mengirim data ke website berupa order yang dia buat. Dengan pengguna mengirim data order tersebut, website dapat menerima data dan melakukan operasi untuk _handle_ kejadian tersebut. Mungkin dengan mengirim sebuah notifikasi ke penjual atau dengan mengubah database.

## B. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON jauh lebih baik untuk digunakan dalam skenario yang mengharuskan pengiriman / penerimaan data yang memiliki struktur tidak terlalu kompleks. Cara JSON ditulis, membuatnya lebih mudah untuk dibaca manusia dibandingkan XML, tetapi kemudahan ini membuatnya kurang cocok untuk _parsing_ data yang memiliki hierarki kompleks. Selain lebih mudah dibaca, ternyata menurut [AWS](https://aws.amazon.com/compare/the-difference-between-json-xml/#:~:text=JSON%20has%20smaller%20file%20sizes,and%20results%20in%20bulky%20files.) JSON lebih cepat di _parse_ dan memiliki file size lebih kecil daripada XML.

#### Mengapa JSON lebih populer?

- Kesederhanaan: JSON lebih mudah dipahami dan ditulis oleh developer.
- Kecepatan: JSON lebih ringan dan cepat untuk diambil dan diolah, terutama dalam aplikasi web yang membutuhkan respons cepat.
- Kompatibilitas dengan JavaScript: JSON terintegrasi langsung dengan JavaScript, yang membuatnya sangat cocok untuk aplikasi web dengan framework yangg menggunakan JS seperti React dan Vue.js.

## C. Fungsi dari Method is_valid() pada Form Django

Method is_valid() pada form Django digunakan untuk:

- Validasi Input Pengguna: Method ini memeriksa apakah semua data yang dikirimkan melalui form memenuhi kriteria validasi yang telah didefinisikan (misalnya tipe data yang benar, tidak ada field kosong untuk field yang bersifat _required_, dll).

- Mencegah Kesalahan: Jika form tidak valid, is_valid() akan mengembalikan **False**, sehingga kita bisa menghindari penyimpanan atau pemrosesan data yang tidak sah.

- Mengakses Data yang Bersih: Jika is_valid() mengembalikan **True**, kita dapat mengakses data form yang sudah "dibersihkan" (melalui method cleaned_data), yang berarti data tersebut sudah diverifikasi dan siap digunakan

#### Mengapa kita butuh menggunaakn is_valid()?

Karena jika tidak menggunakan is_valid(), saat kita membuat form yang dapat diinput oleh pengguna, apabila input pengguna tidak valid, code yang mengolah input tersebut bisa terjadi error. Contohnya, di form dengan salah satu fieldsnya berupa "Harga", dimana pengguna diekspektasikan untuk menginput nomer karena code dibelakang akan menjumlahkan harga tersebut untuk menciptakan total. Apabila pengguna menginput karakter alfabet, maka pasti terjadi error.

## D. Mengapa Kita Membutuhkan csrf_token di Django?

CSRF (Cross-Site Request Forgery) adalah _cyberattack_ di mana penyerang mencoba memalsukan permintaan pengguna yang sah atau legal kepada server.

- Fungsi csrf_token:\
  csrf_token berfungsi sebagai token keamanan yang disertakan dalam setiap permintaan POST (yang sering digunakan untuk mengirim data form) untuk memverifikasi bahwa permintaan tersebut berasal dari pengguna yang sah dan bukan dari situs web eksternal yang mencoba menyamar.

- Apa yang Terjadi Jika Tanpa csrf_token?\
  Tanpa csrf_token, web akan rentan terhadap serangan CSRF, di mana penyerang bisa mengirimkan permintaan yang terlihatnya sah ke server dengan atas nama pengguna yang sudah login. Jika penyerang berhasil melakukan ini, maka dia akan memiliki akses full terhadap akun yang dia serang.

- Bagaimana Penyerang Memanfaatkan Ini?\
  Penyerang dapat membuat situs berbahaya yang mengirimkan permintaan ke server target, dengan pengguna yang sudah login sebagai korban. Jika csrf_token tidak ada, server tidak memiliki cara untuk membedakan permintaan sah dari permintaan berbahaya.

## E. Step-by-Step Implementasi Checklist

1. **Membuat file forms.py**

   - Di direktori main, buat file forms.py
   - Isi file tersebut dengan meng-import model yang sudah ada di models.py dan juga library ModelForm
   - Buatlah class yang menerima parameter ModelForm yang berisi model apa yang akan digunakan serta form tersebut akan menerima fields apa saja.
   - Di file settings.py di root directory, tambahkan CSRF_TRUSTED_ORIGIN yang berisi link utama web

2. **Menambah fungsi di views.py**

   - Import form yang telah dibuat di forms.py.
   - Import library yang dibutuhkan seperti HttpResponse dan serializers
   - Tambahkan fungsi show_json, show_xml, show_xml_by_id, show_json_by_id
   - Fungsi show_json dan show_xml akan mengambil semua data yang ada di model dengan method model.objects.all()
   - Fungsi show_json_by_id dan show_xml_by_id akan menerima parameter id yang akan dipass ke method model.objects.filter(id=) supaya dapat mengembalikan item yang sesuai
   - Lakukan serialisasi ke data yang sudah didapatkan dengan library serializers
   - _Parse_ data yang sudah diserialisasi kepada sebuah HttpResponse dan sesuaikan content_type

3. **Menambahkan Routing**
   - Di file urls.py di direktori main, tambahkan path baru di urlpatterns
   - Sesuaikan path baru ini dengan views yang diinginkan, buatlah routing yang sesuai juga, jika ingin memanggil view json maka gunakan routing "json/"
   - Pastikan nama yang dispesifikasi juga sesuai dengan nama fungsi
   - Untuk fungsi yang menerima parameter seperti fungsi show_xml_by_id, gunakan formatting < str:id > (tanpa spasi) setelah path yang dituju, contohnya "json/< str:id>" supaya views dapat menerima parameter id dan mengembalikan data yang sesuai.

## F. Screenshot Postman
**json/**
![image](https://github.com/user-attachments/assets/836c8819-1132-409d-b1ae-831d3814f349)
**xml/**
![image](https://github.com/user-attachments/assets/338e1e2b-296c-4831-add7-6380a76840ee)

**json/id**
![image](https://github.com/user-attachments/assets/eaf27c34-fdd5-4348-b7b8-5d4c5027f44c)

**xml/id**
![image](https://github.com/user-attachments/assets/d58f851c-4bc7-40d4-9d0a-ee95eead6f06)

# Tugas 3

## A. Perbedaan antara HttpResponseRedirect() dan redirect()
1. HttpResponseRedirect()
- Hanya menerima string yang berisi URL sebuah page dan akan melakukan redirect ke page tersebut. 
- Fungsi ini lebih sederhana karena hanya menerima URL, sehingga apabila ingin mengearah ke sebuah view harus menggunakan fungsi reverse().

2. redirect()
- Menerima string URL, nama view, atau objek model.
- Redirecting ke URL yang sesuai dilakukan oleh Django sehingga lebih fleksibel dan dinamis.


## B. Menghubungkan VinylRecord dengan User
1. Tambahkan konteks user ke model VinylRecord
- Import from django.contrib.auth.models import User ke file models. 
- Asosiasikan tiap item dengan satu user dengan menambah field user ke dengan code `user = models.ForeignKey(User, on_delete=models.CASCADE)`

2. Simpan konteks user penambah vinyl tiap kali penambahan vinyl
- Tambahkan `vinyl_form.user = request.user` dan `vinyl_form.save()` pada view penambahan vinyl supaya tiap item Vinyl terasosiasi dengan user yang menambahkannya

3. Tampilkan vinyl yang sesuai dengan user di main
- Pada view main, tambahkan filter pada objek vinyl yang diambil yang mencari berdasarkan user dengan menambah `vinyls = VinylRecord.objects.filter(user=request.user)` 
 
## C. Perbedaan Authentication dan Authorization
1. **Authentication**
- Authentication adalah proses untuk menentukan *siapa* yang sedang menggunakan aplikasi atau sistem dan apakah *siapa* tersebut merupakan orang yang sebenarnya.
- Contoh :
    - Saat mahasiswa login ke SCELE menggunakan user dan password mereka
    - Orang login ke akun Google dengan menginput email mereka dan menerima kode 2FA di SMS

2. **Authorization**
- Authorization adalah proses untuk menentukan *apa* yang dapat dilakukan oleh pengguna setelah mereka berhasil terautentikasi, yaitu hak akses atau izin yang dimiliki oleh pengguna terhadap data atau fungsi dalam aplikasi atau sistem.
- Contoh : 
    - Setelah mahasiswa berhasil login ke SCELE, sistem memeriksa apakah mereka memiliki izin untuk mengakses materi kuliah tertentu. Atau apakah mereka memiliki akses mengedit sebuah quiz / menilai tugas.
    - Jika pengguna login ke akun Google mereka, authorization menentukan apakah mereka memiliki akses untuk mengedit dokumen di Google Drive atau hanya bisa melihatnya, tergantung pada pengaturan perizinan yang diatur oleh pemilik dokumen.

3. **Implementasi Django**
- **Authentication**
    -   Django menggunakan built-in authentication system yang memungkinkan pengguna untuk login, logout, dan mengelola session.
    -   Library bawaan: `django.contrib.auth` untuk proses Auth.
    -   Implementasi:
    ```python
    python from django.contrib.auth import authenticate, login

    def my_view(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    ```
- **Authorization**
    - Django menggunakan permission system untuk menentukan akses pengguna terhadap tindakan dan data tertentu.
    - Library bawaan untuk decorator: `from django.contrib.auth.decorators`
    - Dapat mengguanakan decorators seperti `@login_required` dan `@permission_required` untuk membatasi akses ke view tertentu berdasarkan apakah pengguna sudah login dan apakah mereka memiliki izin yang sesuai.
    - Implementasi:
    ```python
    @login_required(login_url='/login')
    def show_main(request):
        vinyls = VinylRecord.objects.filter(user=request.user)
        context = {
            'name': request.user.username,
            'npm': '2306275286',
            'kelas': 'A',
            'aplikasi': "Reksa's Records",
            'vinyls': vinyls,
            'last_login': request.COOKIES.get('last_login')
        }
    return render(request, "main.html", context)

    ```


## D. Bagaimana Django Mengingat Pengguna, Kegunaan dan Keamanan Cookies
### Cara Django Mengingat Pengguna
- Django mengingat pengguna yang telah login menggunakan *session management* yang berbasis *cookies*. Setelah user berhasil login, Django menyimpan informasi session dalam cookie yang dikirimkan ke browser pengguna.
### Kegunaan Lain dari Cookies
- Pelacakan : Menyimpan data lokasi terakhir
- Pengaturan Preferensi : Menyimpan preferensi user seperti dark mode / light mode
- _Shopping Cart_ : Pada website E-commerce, cookies digunakan untuk menyimpan user sudah menambah item apa saja pada cart mereka.
### Keamanan Cookies
- Jika cookies tidak di-seting dengan benar, data pada cookies bisa dicuri oleh pihak ketiga menggunakan teknik seperti _session hijacking_. Misalnya, jika cookie tidak dienkripsi dan dikirim melalui koneksi HTTP yang _unsecured_, data bisa di _intercept_ oleh hacker.

## E. Implementasi Step-by-Step Checklist
1. **Membuat view untuk page Auth di views.py**
- Tambahkan library untu autentikasi
```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
```
- Buat view untuk handle login user
```python
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

```
View ini akan mengirim form yang akan disediakan di template login.html, lalu melakukan verifikasi pada login dengan function `login(request, user)`. Jika login berhasil (akun valid), maka akan me-redirect ke view main.
- Buat view untuk handle logout user
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')
```
View ini akan memanggil fungsi `logout` yang akan membuang session user, kemudian meredirect user ke view login.
- Membuat view untuk handle register
```python
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)
```
View ini akan mengirim UserCreationForm ke template dan menerima response valid. Response tersebut akan menciptakan sebuah user baru disistem yang dapat digunakan saat login. 

2. **Membuat template untuk tiap view baru**
- Buat login.html untuk view login_user, di dalam tempalte ini akan menampilkan form yang dikirim oleh view. 
- Buat register.html untuk view register, di dalam template ini akan menampilkan form yang dikirim oleh view.

3. **Menambah Routing**
- Pada urls.py di direktori app tambahkan path untuk tiap view yang baru dibuat
```python
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

```

3. **Menggunakan Cookies untuk Menampilkan Last Login**
- Di views.py, import library datetime untuk mendapatkan waktu terkini dengan `import datetime`
- Pada view login_user, ketika user berhasil login, simpan waktu mereka login pada cookies dengan menambahkan `response.set_cookie('last_login', str(datetime.datetime.now()))` pada objek response yang akan mengarah ke main.
- Pada view show_main, ubah pengiriman nama dengan memanggil `request.user.username` dan pass parameter baru untuk cookies last_login dengan `'last_login' : request.COOKIES.get('last_login')`

4. **Menampilkan user last login di main**

Pada tempalte main.html,
- Panggil objek username yang dikirim oleh view untuk memanggil username dari user.
- Panggil objek last_login yang dikirim oleh view saat kita login dengan `{{ last_login }}` untuk menggunakan cookies untuk menampilkan waktu terakhir login.

5. **Menghubungkan VinylRecord dengan User**
- Pada models.py di model VinylRecord, tambahkan library untuk meneirma User dengan `from django.contrib.auth.models import User`. 
- Tambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` untuk mengasosiakian tiap item vinyl dengan user yang menciptakannya
- Pada views.py, pada view show_main, ubah cara pemanggilan item vinyl untuk filter berdasarkan user yang terasosiasi dengan vinyl tersebut dengan `vinyls = VinylRecord.objects.filter(user=request.user)
