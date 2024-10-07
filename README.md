**Deployed : http://farrel-reksa-reksasrecords.pbp.cs.ui.ac.id/**

# Tugas 2

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

# Tugas 3

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

# Tugas 4

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

- Authentication adalah proses untuk menentukan _siapa_ yang sedang menggunakan aplikasi atau sistem dan apakah _siapa_ tersebut merupakan orang yang sebenarnya.
- Contoh :
  - Saat mahasiswa login ke SCELE menggunakan user dan password mereka
  - Orang login ke akun Google dengan menginput email mereka dan menerima kode 2FA di SMS

2. **Authorization**

- Authorization adalah proses untuk menentukan _apa_ yang dapat dilakukan oleh pengguna setelah mereka berhasil terautentikasi, yaitu hak akses atau izin yang dimiliki oleh pengguna terhadap data atau fungsi dalam aplikasi atau sistem.
- Contoh :
  - Setelah mahasiswa berhasil login ke SCELE, sistem memeriksa apakah mereka memiliki izin untuk mengakses materi kuliah tertentu. Atau apakah mereka memiliki akses mengedit sebuah quiz / menilai tugas.
  - Jika pengguna login ke akun Google mereka, authorization menentukan apakah mereka memiliki akses untuk mengedit dokumen di Google Drive atau hanya bisa melihatnya, tergantung pada pengaturan perizinan yang diatur oleh pemilik dokumen.

3. **Implementasi Django**

- **Authentication**

  - Django menggunakan built-in authentication system yang memungkinkan pengguna untuk login, logout, dan mengelola session.
  - Library bawaan: `django.contrib.auth` untuk proses Auth.
  - Implementasi:

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

- Django mengingat pengguna yang telah login menggunakan _session management_ yang berbasis _cookies_. Setelah user berhasil login, Django menyimpan informasi session dalam cookie yang dikirimkan ke browser pengguna.

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

# Tugas 5

## A. Urutan Prioritas Pengambilan CSS Selector

Jika ada beberapa selector diterapkan ke elemen yang sama, prioritas dari selector tersebut yang akan menentukan style mana yang digunakan. Urutan prioritas ini bergantung pada tingkat specificity dan urutan penulisan. Urutannya adalah:

1. **!important**: Style yang ditandai dengan `!important` akan menjadi prioritas atas, kecuali jika ada style lain yang juga menggunakan `!important`, maka specificity dari selector juga menjadi konsiderasi.
2. **Inline styles**: Style yang ditulis langsung pada elemen HTML menggunakan atribut `style=""` akan memiliki prioritas tertinggi. Inline style akan selalu diterapkan, kecuali ada style lain dengan `!important`.
3. **Selector berbasis ID** (`#id`) memiliki prioritas lebih tinggi daripada selector lainnya, kecuali inline style atau `!important`.
4. **Class, pseudo-class, dan attribute selectors**: Selector berbasis class (`.class`), pseudo-class (`:hover`, `:focus`), dan attribute selector (`[type="text"]`) memiliki prioritas lebih rendah dibanding ID, tapi lebih tinggi dari tag/element selectors.
5. **Tag selectors (type selectors)**: Selector berbasis nama elemen/tag HTML (`div`, `p`, `h1`, dll.) memiliki prioritas terendah.
6. **Source order (Urutan penulisan)**: Jika dua selector memiliki specificity yang sama, style yang diterapkan adalah yang ditulis paling akhir dalam file CSS atau HTML.

---

## B. Kenapa Responsive Design Penting?

Responsive design menjadi konsep penting dalam pengembangan aplikasi web karena semakin beragamnya perangkat yang digunakan oleh pengguna untuk mengakses web. Pengguna tidak hanya mengakses aplikasi dari komputer desktop, tetapi juga dari perangkat mobile seperti smartphone dan tablet dengan ukuran layar, resolusi, dan orientasi yang berbeda.

### Contoh Responsive:

**X.com**  
Tampilan X.com akan berubah tergantung dengan ukuran dan orientasi web, dengan perubahan paling terlihat ada pada sidebar yang menjadi bottom-bar dan konten yang hanya terfokus pada tampilan utama.
![image](https://github.com/user-attachments/assets/be615a93-e72c-445e-80c2-fc46c608b186)

![image](https://github.com/user-attachments/assets/883b25dc-023b-41dc-b1cb-189e996c4183)

### Contoh Unresponsive:

**SiakNG**  
Website SiakNG tidak responsive karena tampilan pada mobile dan desktop sama persis. Hal ini membuat user experience di mobile menjadi buruk karena ukuran tombol yang relatif sangat kecil.
![image](https://github.com/user-attachments/assets/48add3c9-323a-4ebf-99e9-31ce4270d7c7)
![image](https://github.com/user-attachments/assets/f2e38b5b-ceb8-4434-b2ed-41cc04629bbd)

---

## C. Perbedaan dan Implementasi Margin, Padding, Border

- **Margin**: Margin adalah ruang kosong di luar elemen, yang memisahkan elemen tersebut dari elemen lainnya. Margin tidak mempengaruhi ukuran elemen itu sendiri, tetapi memberikan jarak antar elemen di sekitarnya. Margin bersifat transparan dan tidak dapat diberi warna.

  **Contoh**:

  ```css
  div {
    margin: 20px;
  }

  div {
    margin-top: 10px;
    margin-right: 15px;
    margin-bottom: 20px;
    margin-left: 5px;
  }
  ```

- **Border**: Border adalah garis yang mengelilingi elemen di luar padding tetapi di dalam margin. Border bersifat visual dan dapat memiliki warna, ketebalan, serta style. Border dapat digunakan untuk memberi struktur pada pemberian informasi di web.

  **Contoh**:

  ```css
  div {
    border: 1px solid black;
  }
  div {
    border-top: 1px dashed blue;
    border-right: 2px solid green; /* Border kanan hijau solid */
    border-bottom: 3px dotted red; /* Border bawah merah dotted */
    border-left: 4px double purple; /* Border kiri ungu double */
  }
  ```

- **Padding**: Padding adalah ruang kosong di dalam elemen, antara konten elemen dan border. Padding menambah jarak antara konten elemen dengan batasan elemen (border). Bersifat transparan, tetapi akan meningkatkan ukuran keseluruhan dari elemen.

  **Contoh**:

  ```css
  div {
    padding: 20px;
  }

  div {
    padding-top: 10px;
    padding-right: 15px;
    padding-bottom: 20px;
    padding-left: 5px;
  }
  ```

## D. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

1. **Flexbox**

Flexbox adalah model layout untuk mengatur elemen di dalam container dalam satu baris (horizontal) atau satu kolom (vertikal). Flexbox cocok untuk mengatur tata letak yang dinamis dan fleksibel. Cocok juga apabila elemen-elemen di dalam container harus berubah ukuran secara proporsional tergantung ukuran layarnya. Flexbox cocok untuk desain yang lebih simpel dan mementingkan aliran atau fluidity dari desain.

2. **Grid Layout**

Grid Layout adalah model layout dua dimensi yang lebih rigid daripada flexbox. Grid Layout memungkinkan kita untuk mengatur elemen di sumbu horizontal (baris) dan juga vertikal (kolom) secara langsung . Grid sangat cocok untuk mengatur layout halaman web yang lebih terstruktur dan kompleks.

## E. Implementasi Step by Step

1. **Membuat view untuk edit dan hapus**

- Membuat edit_vinyl.html yang berisi sama dengan create_vinyl tetapi memiliki button untuk menghapus yang akan direct ke view edit dan delete.
- Di views.py, menambah view

```python
 def edit_vinyl(request, id):
    vinyl = VinylRecord.objects.get(id=id)
    form = VinylRecordForm(request.POST or None, instance=vinyl)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    context = {'form': form, 'vinyl': vinyl, 'aplikasi': "Reksa's Records"}
    return render(request, 'edit_vinyl.html', context)

def delete_vinyl(request, id):
    vinyl = VinylRecord.objects.get(id=id)
    vinyl.delete()
    return redirect('main:show_main')
```

- View ini akan dipanggil untuk menampilkan edit_vinyl.html dan melakukan operasi edit dan delete pada vinyl yang dipilih. View ini akan dipanggil saat user klik button edit dan delete pada tiap card.
- Pada urls.py, import view baru dan assign path yang sesuai

```python
 path('edit_vinyl/<str:id>/', edit_vinyl, name='edit_vinyl'),
 path('delete_vinyl/<str:id>/', delete_vinyl, name='delete_vinyl'),
```

2. **Membuat navbar responsive**

- Menambahkan CDN Tailwind untuk menggunakan Tailwind CSS
- Di base.html menambahkan

```html
<script src="https://cdn.tailwindcss.com">
```

Hal ini supaya codebase kita memiliki akses ke class - class yang dibutuhkan untuk tailwind

- Mengubah design header
  Di main.html, me-wrap informasi nama user, title, dan last login di dalam satu div
- Memberi class warna background, warna text, dan membuat header menjadi flexbox dan membuat elemen berada di tengah

```html
<div
  class="bg-blue-500 text-white py-8 px-4 mb-4 flex flex-col items-center"
></div>
```

3. **Membuat card**

- Membuat komponen html baru spesifik untuk card yang akan merepresentasikan satu vinyl
- Membuat file baru, vinyl-card-main.html dan vinyl-card-fav.html
- Vinyl-card-main berisi html dengan class css untuk menunjukkan judul, artist, image-url,price, state favorit, button edit.
- Viny-card-fav berisi html dengan class css untuk menunjukkan yang sama tanpa button edit
- Pada main.html, iterasikan semua vinyl yang dipass oleh view menggunakan command

```html
{% for vinyl in vinyls %} {% include "components/vinyl-card-main.html" %}
```

- Pada favorite.html lakukan yang sama untuk vinyl-card-fav.html

4. **Membuat navbar**

- Membuat komponen header.html yang berisi logo, judul web, search bar, button favorite, button add vinyl, dan button log out
- Untuk membuat menjadi responsive, membuat dua versi navbar, versi pertama adalah desktop yang diberi class media query supaya akan hidden kecuali layar lebih dari 768px

```css
class=”hidden md:flex”
```

- Versi kedua adalah versi mobile yang diberi class media query yang akan hidden apabila layar melebihi 768px

```css
class=”flex md:hidden”
```

- Pada navbar versi mobile, menambahkan elemen burger-menu yang dibuat dengan elemen svg dan path yang sesuai
- Pada navbar versi mobile, menambahkan sedikit javascript untuk menampilkan dan menutup tampilan menu ketika membuka burger-menu dengan

```html
<script>
  document.addEventListener("DOMContentLoaded", function () {
    const burgerMenu = document.getElementById("burger-menu");
    const mobileMenu = document.getElementById("mobile-menu");

    const toggleMenu = () => {
      mobileMenu.classList.toggle("hidden");
      document.body.classList.toggle("overflow-hidden"); // Tidak bisa scroll jika menu terbuka
    };

    burgerMenu.addEventListener("click", toggleMenu);

    // Close mobile menu jika klik luar menu
    document.addEventListener("click", function (event) {
      if (
        !mobileMenu.contains(event.target) &&
        !burgerMenu.contains(event.target)
      ) {
        if (!mobileMenu.classList.contains("hidden")) {
          toggleMenu();
        }
      }
    });

    // Close mobile menu jika ukuran window >= 768px
    window.addEventListener("resize", function () {
      if (
        window.innerWidth >= 768 &&
        !mobileMenu.classList.contains("hidden")
      ) {
        toggleMenu();
      }
    });
  });
</script>
```

5. **Mengubah tampilan login,register, dan tambah vinyl**

- Pada login.html, register.html, dan create_vinyl.html, ubah tampilan form dengan menggunakan tailwind class dan widget-tweaks untuk memberi CSS styling pada fields form.
- Perubahan design lebih fokus pada tata letak dan padding. Membuat semuanya lebih rapi dengan menggunakan flexbox supaya elemen berada di tengah.
- Pada login, membuat fields memiliki warna text yang lebih gelap dan font-weight yang lebih bold, menambah placeholder, dan membuat button submit lebih responsive dengan mengubah warna background dan hover nya.
- Hal yang sama juga dilakukan pada register.
- Pada create_vinyl, membuat input form berada di tengah dan membuat ukuran input lebih responsive.

# Tugas 6

## A. Manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web

Javascript yang sangat berguna dalam membuat web lebih dinamis dan interaktif karena kita dapat melakukan operasi - operasi yang tidak bisa dilakukan hanya dengan HTML dan CSS. Contohnya, ketika kita ingin menampilkan sesuatu hanya jika user telah mengklik sebuah button, kita dapat menggunakan JavaScript untuk menampilkan elemen tersebut. Inti dari JavaScript adalah untuk memberi elemen interaktivitas yang membuat sebuah website jauh lebih menarik dan nyaman untuk digunakan.

## B. Fungsi await ketika fetch dan apa yang terjadi jika tidak menggunakan await

Fungsi await dan fetch adalah fungsi asynchronous. Fungsi asynchronous adalah fungsi yang tidak langsung menunggu hasilnya, melainkan mengeksekusi fungsi tersebut secara berurutan. Fungsi `await` digunakan untuk menunggu hasil dari fungsi asynchronous tersebut. Jika tidak menggunakan `await`, fungsi tersebut akan langsung dieksekusi tanpa menunggu hasilnya.

Await umumnya digunakan saat kita ingin menerima sebuah data dari API. Ekspektasinya adalah kita mengirim sebuah request dan menunggu response dari API tersebut untuk kita kemudian olah. Namun, jika tidak menggunakan `await`, fungsi 'pengolahan' ini akan langsung dieksekusi tanpa menunggu data dari API selesai dikirim.

## C. Kebutuhan decorator csrf_exempt pada view untuk membuat AJAX POST

Decorator `@csrf_exempt` diperlukan karena AJAX POST yang kita buat tidak akan membawa cookie (csrf token) sehingga membuat server tidak percaya bahwa request tersebut berasal dari aplikasi kita. Dengan decorator tersebut, kita memberi otorisasi kepada server untuk menganggap request tersebut legal bahkan tanpa CSRF verification.

Hal ini sebenarnya bukan merupakan solusi yang ideal, karena menghapus kebutuhan CSRF verification akan memberi celah dan kesempatan untuk serangan - serangan pada web kita.

## D. Mengapa pembersihan data (strip_tags) dilakukan di backend dan bukan frontend?

Pembersihan data dilakukan di backend karena bagian frontend dimana user melakukan input sangat mudah untuk dimanipulasi. Banyak sekali cara untuk memanipulasi elemen HTML dan Javascript yang ditampilkan pada frontend.

Oleh karena itu, pembersihan data dilakukan di backend untuk menghindari manipulasi data oleh user lewat frontend. Dengan melakukan di backend, kita dapat memastikan bahwa semua data yang akan diproses adalah data yang valid dan bebas dari manipulasi yang tidak diinginkan.

## E. Implementasi Step by Step

1. **Memanggil Card dengan AJAX**

Di main html,

- Mengubah cara memanggil card dari yang sebelumnya

```html
{% for vinyl in vinyls %} {% include "components/vinyl-card-main.html" %} {%
endfor %}
```

menjadi

```javascript
<div id="vinyl-cards"></div>;

async function getVinylEntries(query = "") {
  let url = "{% url 'main:show_json' %}";
  if (query) {
    url += `?q=${encodeURIComponent(query)}`;
  }
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error("Network response was not ok");
  }
  console.log(response);
  return await response.json();
}

async function refreshVinylEntries(query = "") {
  try {
    const vinylEntries = await getVinylEntries(query);
    console.log(vinylEntries);
    renderVinylCards(vinylEntries);
  } catch (error) {
    console.error("Error fetching vinyl records:", error);
    vinylCardsContainer.innerHTML =
      '<p class="text-red-500">An error occurred while fetching vinyl records.</p>';
  }
}

function renderVinylCards(vinyls) {
  // Clear existing vinyl cards
  vinylCardsContainer.innerHTML = "";

  if (vinyls.length === 0) {
    vinylCardsContainer.innerHTML = `
          <div class="flex justify-center items-center w-full flex-col">
            <p class="text-2xl font-bold text-center">No vinyl records found.</p>
            <img src="{% static 'images/sad-face.svg' %}" alt="Sad Face" class="w-24 h-24 mt-4">
          </div>
        `;
    return;
  }

  vinyls.forEach((vinyl) => {
    const vinylCardHTML = createVinylCard(vinyl);
    vinylCardsContainer.insertAdjacentHTML("beforeend", vinylCardHTML);
  });
}

vinylCardsContainer.addEventListener("click", async function (event) {
  const button = event.target.closest(".favorite-toggle");

  if (button) {
    event.preventDefault();
    console.log("Favorite toggle clicked");

    const vinylId = button.dataset.vinylId;
    const isFavorited = button.dataset.favorited === "true";
    const url = isFavorited
      ? `/remove_from_favorites_ajax/${vinylId}/`
      : `/add_to_favorites_ajax/${vinylId}/`;
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({ vinylId }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      refreshVinylEntries();
    } catch (error) {
      console.error("Error toggling favorite:", error);
    }
  }
});

function createVinylCard(vinyl) {
  const isFavorited = vinyl.fields.favorited_by.includes(parseInt(currentUser));

  return `
      <div class="vinyl-card bg-white shadow-md rounded-lg overflow-hidden w-64 h-auto transform transition-transform hover:scale-110 hover:shadow-xl relative">
        <button class="absolute top-2 right-2 text-yellow-500 favorite-toggle" data-vinyl-id="${
          vinyl.pk
        }" data-favorited="${isFavorited}">
          ${
            isFavorited
              ? `
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 fill-current" viewBox="0 0 20 20" fill="currentColor">
              <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.286 3.957a1 1 0 00.95.69h4.15c.969 0 1.371 1.24.588 1.81l-3.357 2.44a1 1 0 00-.364 1.118l1.286 3.957c.3.921-.755 1.688-1.54 1.118l-3.357-2.44a1 1 0 00-1.175 0l-3.357 2.44c-.784.57-1.838-.197-1.54-1.118l1.286-3.957a1 1 0 00-.364-1.118L2.465 9.384c-.783-.57-.38-1.81.588-1.81h4.15a1 1 0 00.95-.69l1.286-3.957z" />
            </svg>
          `
              : `
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.286 3.957a1 1 0 00.95.69h4.15c.969 0 1.371 1.24.588 1.81l-3.357 2.44a1 1 0 00-.364 1.118l1.286 3.957c.3.921-.755 1.688-1.54 1.118l-3.357-2.44a1 1 0 00-1.175 0l-3.357 2.44c-.784.57-1.838-.197-1.54-1.118l1.286-3.957a1 1 0 00-.364-1.118L2.465 9.384c-.783-.57-.38-1.81.588-1.81h4.15a1 1 0 00.95-.69l1.286-3.957z" />
            </svg>
          `
          }
        </button>
        <div class="vinyl-card-image">
          <img src="${mediaUrl}${
    vinyl.fields.image
  }" alt="Vinyl Image" class="vinyl-image w-full h-48 object-fit" />
        </div>
        <div class="vinyl-info p-4">
          <h3 class="vinyl-title text-lg font-semibold mb-0.5">${
            vinyl.fields.album_name
          }</h3>
          <h4 class="vinyl-artist text-gray-400"> by ${vinyl.fields.artist}</h4>
          <h4 class="vinyl-price text-green-800 font-semibold mt-2">$${
            vinyl.fields.price
          }</h4>
        </div>
        <a href="/edit_vinyl/${
          vinyl.pk
        }/" class="absolute bottom-2 right-2 bg-blue-500 text-white rounded-full p-2 hover:bg-blue-700">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="white" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
          </svg>
        </a>
      </div>
      `;
}
```

Sistem untuk menampilkan card berdasarkan query pencarian diatas adalah dengan menggunakan fungsi `getVinylEntries` yang akan mengirim request ke url `{% url 'main:show_json' %}` dan menampilkan hasilnya menggunakan fungsi `renderVinylCards` untuk menampilkan card-card tersebut. Lakukan juga `refreshVinylEntries` untuk menampilkan card-card yang baru saja di tambahkan.

2. **Membuat form tambah vinyl menggunakan AJAX**

Di main.html,

- Menambahkan modal untuk menambahkan vinyl baru
- Membuat form untuk menambahkan vinyl baru
- Membuat fungsi untuk menambahkan vinyl baru menggunakan AJAX

Pertama kita membuat view baru untuk menambahkan vinyl baru dengan menggunakan AJAX, `create_vinyl_ajax`. Kemudian, kita membuat urls.py untuk mengassign pathnya.

```python
@csrf_exempt
@require_POST
@login_required(login_url='/login')
def create_vinyl_ajax(request):
    album_name = strip_tags(request.POST.get("album_name"))
    artist = strip_tags(request.POST.get("artist"))
    genre = strip_tags(request.POST.get("genre"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    image = request.FILES.get("image")

    if not all([album_name, artist, genre, price, description, image]):
        return JsonResponse({'errors': 'All fields are required.'}, status=400)

    vinyl = VinylRecord(
        album_name=album_name,
        artist=artist,
        genre=genre,
        price=price,
        description=description,
        user=request.user,
        image=image
    )

    vinyl.save()

    data = {
        'vinyl': {
            'id': vinyl.id,
            'album_name': vinyl.album_name,
            'artist': vinyl.artist,
            'genre': vinyl.genre,
            'price': str(vinyl.price),
            'description': vinyl.description,
            'image_url': vinyl.image.url,
            'favorited_by': [user.username for user in vinyl.favorited_by.all()],
        }
    }

    return JsonResponse(data, status=201)
```

Tambahkan routing untuk `create_vinyl_ajax` di urls.py.

```python
path('create_vinyl_ajax/', create_vinyl_ajax, name='create_vinyl_ajax'),
```

Di header, ubah button create vinyl menjadi button yang memiliki class `open-create-vinyl-modal` dan ketika diklik akan memanggil fungsi `openCreateVinylModal` untuk menampilkan modal.

Di main.html, buatlah modal untuk menambahkan vinyl baru dengan id `create-vinyl-modal`. Berikan class `hidden` untuk menghilangkan modal tersebut secara default.

```html
<div
  id="create-vinyl-modal"
  class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 hidden"
  role="dialog"
  aria-modal="true"
  aria-labelledby="create-vinyl-title"
>
  <div
    class="bg-white rounded-lg shadow-lg w-full max-w-xl p-6 relative max-h-full overflow-y-auto"
  >
    <button
      id="close-create-vinyl-modal"
      class="absolute top-2 right-2 text-red-600 hover:text-red-800 font-extrabold text-4xl"
      aria-label="Close Modal"
    >
      &times;
    </button>
    <h2
      id="create-vinyl-title"
      class="text-2xl  font-bold mb-4 text-center justify-center items-center"
    >
      Create New Vinyl Record
    </h2>
    <form id="create-vinyl-form" class="space-y-2">
      {% csrf_token %}
      <div>
        <label for="album_name" class="block text-lg font-semibold"
          >Album Name:</label
        >
        <input
          type="text"
          id="album_name"
          name="album_name"
          class="bg-gray-200 p-2 rounded-lg w-full"
          placeholder="Album Name"
          required
        />
      </div>

      <div>
        <label for="artist" class="block text-lg font-semibold">Artist:</label>
        <input
          type="text"
          id="artist"
          name="artist"
          class="bg-gray-200 p-2 rounded-lg w-full"
          placeholder="Artist Name"
          required
        />
      </div>

      <div>
        <label for="genre" class="block text-lg font-semibold">Genre:</label>
        <select
          id="genre"
          name="genre"
          class="bg-gray-200 p-2 rounded-lg w-full"
          required
        >
          {% for value,display in genres %}
          <option value="{{ value }}">{{ display }}</option>
          {% endfor %}
        </select>
      </div>

      <div>
        <label for="price" class="block text-lg font-semibold">Price:</label>
        <input
          type="number"
          id="price"
          name="price"
          class="bg-gray-200 p-2 rounded-lg w-full"
          placeholder="Retail Price"
          step="0.01"
          required
        />
      </div>

      <div>
        <label for="description" class="block text-lg font-semibold"
          >Description:</label
        >
        <textarea
          id="description"
          name="description"
          class="bg-gray-200 p-2 rounded-lg w-full"
          placeholder="Album Description"
          required
        ></textarea>
      </div>

      <div>
        <label for="image" class="block text-lg font-semibold"
          >Album Cover:</label
        >
        <input
          type="file"
          id="image"
          name="image"
          class="bg-gray-200 p-2 rounded-lg w-full"
          accept="image/*"
          required
        />
      </div>

      <div class="flex justify-end gap-4">
        <button
          type="button"
          id="cancel-create-vinyl"
          class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded"
        >
          Cancel
        </button>
        <button
          type="submit"
          class="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
        >
          Create Vinyl Record
        </button>
      </div>
    </form>
  </div>
</div>
```

Form juga digunakan untuk mengambil data dari user dan mengirimkannya ke `create_vinyl_ajax` menggunakan AJAX. Dengan menggunakan `FormData`, kita dapat mengirim data tersebut ke server.

JavaScript untuk menampilkan modal dan menangani form tambah vinyl baru.

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const openCreateVinylModalButtons = document.querySelectorAll('.open-create-vinyl-modal');
    const createVinylModal = document.getElementById('create-vinyl-modal');
    const closeCreateVinylModalButton = document.getElementById('close-create-vinyl-modal');
    const cancelCreateVinylButton = document.getElementById('cancel-create-vinyl');
    const createVinylForm = document.getElementById('create-vinyl-form');

    function openCreateVinylModal() {
      createVinylModal.classList.remove('hidden');
      createVinylForm.querySelector('input, textarea').focus();

      if (!mobileMenu.classList.contains('hidden')) {
        toggleMenu();
  }
    }

    function closeCreateVinylModal() {
      createVinylModal.classList.add('hidden');
      createVinylForm.reset();
    }

    openCreateVinylModalButtons.forEach(button => {
      button.addEventListener('click', openCreateVinylModal);
    });
    closeCreateVinylModalButton.addEventListener('click', closeCreateVinylModal);
    cancelCreateVinylButton.addEventListener('click', closeCreateVinylModal);
```

3. **Memastikan input dilakukan dengan aman**

Kita menggunakan decorator library strip_tags untuk memastikan bahwa input dilakukan dengan aman. Tambahkan verifikasi strip_tags setelah user mengirim data ke view `create_vinyl_ajax`.

```python
album_name = strip_tags(request.POST.get("album_name"))
artist = strip_tags(request.POST.get("artist"))
genre = strip_tags(request.POST.get("genre"))
price = request.POST.get("price")
description = strip_tags(request.POST.get("description"))
```

Hal ini memastikan bahwa input dilakukan dengan aman dan tidak ada tag HTML yang dimasukkan untuk mencegah serangan XSS (Cross-Site Scripting).
