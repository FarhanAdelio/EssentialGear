## Tugas 2 PBP Farhan Adelio Prayata 2306240162

- Cara saya mengimplementasikan checklist
1. Membuat sebuah proyek Django baru Pertama yang saya lakukan adalah membuat direktori baru dengan nama EssentialGear dan masuk ke dalamnya, lalu di dalam direktori tersebut saya menyalakan virtual environment setelah itu di dalam direktori yang sama saya membuat berkas requirements.txt yang berisi dependencies yang perlu diinstall. 
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
setelah file requirements tersebut saya buat saya melakukan pip install -r requirements.txt pada cmd. setelah itu saya menjalankan django-admin startproject EssentialGear . untuk membuat projek Django baru bernama EssentialGear
<br>
2. Membuat aplikasi dengan nama main pada proyek tersebut. Saya menjalankan python ```manage.py``` startapp main. Setelah perintah di atas dijalankan, direktori baru dengan nama main akan terbentuk.
<br>
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main. Pada direktori proyek EssentialGear, pada berkas ```settings.py``` saya menambahkan 'main' pada INSTALLED_APPS sehingga menjadi


```
    INSTALLED_APPS = [
    ...,
    'main'
    ...,
    ]
```

4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut. pada app main pada berkas ```models.py``` saya menambahkan


```
class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        stock = models.IntegerField()
        rating = models.IntegerField()
```
 setelah itu saya melakukan migrasi agar django dapat melacak perubahan pada model basis data yang kita miliki
<br>

5. Membuat sebuah fungsi pada ```views.py``` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas. Di dalam direktori main saya membuka ```views.py``` lalu saya isi dengan

```
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306240162',
        'name': 'Farhan Adelio',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
```
 Fungsi ini bertugas untuk menangani permintaan HTTP dan mengembalikan tampilan yang sesuai dengan context yang nantinya akan digunakan pada html.
<br>

6. Membuat sebuah routing pada ```urls.py``` aplikasi main untuk memetakan fungsi yang telah dibuat pada ```views.py``` Di dalam direktori main saya membuat berkas baru bernama ```urls.py``` yang berisi

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

kode ini berfungsi mengatur rute URL yang terkait dengan aplikasi main. selanjutnya kita akan menambahkan rute url dalam ```urls.py``` proyek untuk menghubungkannya dengan main. pada berkas ```urls.py``` pada direktori proyek EssentialGear saya menambahkan impor fungsi include lalu menambahkan pada url patterns menjadi
```
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```
```urls.py``` ini berfungsi untuk mengatur rute url tingkat proyek

<br>

7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses melalui Internet. Pada web PWS saya membuat project baru bernama EssentialGear lalu pada ```settings.py``` di projek saya menambahkan URL deployment PWS pada ALLOWED_HOSTS sehingga menjadi

```
ALLOWED_HOSTS = ["localhost", "127.0.0.1","farhan-adelio-Essentialgear.pbp.cs.ui.ac.id"]
```
setelah itu saya menjalankan command yang diberikan pada web pws
<br>

8. Membuat sebuah ```README.md``` yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut. Untuk membuat sebuah readme saya membuatnya pada notepad lalu saya save dalam bentuk file .md lalu saya add commit push pada repositori GitHub saya.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara ```urls.py```, ```views.py```, ```models.py```, dan berkas html.

![bagan](https://github.com/user-attachments/assets/f27afe3e-8ff3-49a3-adec-86df37111ffe)


```urls.py``` : berguna untuk menentukan views yang sesuai dengan request yang diberikan.
```views.py``` :berguna untuk berinteraksi dengan ```models.py``` lalu menjalankan logika yang diinginkan.
```models.py``` : berguna untuk memodelkan data yang ingin disimpan pada database serta digunakan pada HTML melalui ```views.py.```
```HTML : ```berguna untuk menampilkan data sesuai tampilan yang diinginkan.

8. Jelaskan fungsi git dalam pengembangan perangkat lunak!
- Sebagai penyimpanan source code dari project yang ingin kita buat.
- Sebagai version control karena mempunyai sistem commit yang dapat kita lihat sebagai control terhadap perubahan file yang dilakukan.
- Memudahkan kolaborasi karena kita dapat melakukan pull request yang membuat source code dapat dikerjakan sesuai bagian yang telah dibagikan.

9. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

- Kemudahan Penggunaan dan Konvensi: Django didesain dengan prinsip "batteries included" yang berarti banyak fitur penting, seperti otentikasi, manajemen database, dan routing, sudah disediakan langsung tanpa perlu konfigurasi tambahan. Ini memudahkan pemula untuk fokus pada logika aplikasi daripada harus membangun semuanya dari nol.
- Dokumentasi Lengkap: Django dikenal dengan dokumentasinya yang sangat lengkap dan ramah bagi pemula. Dokumentasi yang jelas membantu pengguna baru memahami konsep-konsep dasar framework tanpa terlalu banyak kebingungan.
- Community Support: Django memiliki komunitas yang besar dan aktif, sehingga jika pemula menghadapi masalah, mereka bisa dengan mudah menemukan solusi melalui forum, blog, atau Stack Overflow.

10. Mengapa model pada Django disebut sebagai ORM? 
- Karena Django menggunakan objek dalam Python untuk melakukan interaksi dengan database. Object Relational Mapper (ORM) pada Django merupakan library code yang berguna untuk otomatisasi data transfer yang disimpan pada relational database tables menjadi objek yang mudah diimplementasi dalam Python.