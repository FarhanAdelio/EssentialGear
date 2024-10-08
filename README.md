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

---
## Tugas 3 PBP Farhan Adelio Prayata 2306240162

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? 

- Data delivery penting dalam pengimplementasian platform karena dengan dengan data delivery kita bisa menargetkan, memodelkan, dan optimisasi pengunjung di platform kita ataupun dari platform lainnya di perangkat lain. Dengan kata lain, data delivery berpengaruh besar dalam meningkatkan performa platform kita. Beberapa aspek yang terpengaruh dengan adanya data delivery adalah skalabilitas data yang masuk, keamanan data, user experience, akurasi data, dan membantu kemudahan dalam analisis data.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? 

- Menurut saya, XML dan JSON memiliki kelebihannya masing masing dan dapat saling dibutuhkan di situasi tertentu. Contohnya adalah, disaat kita ingin menyimpan berbagai tipe data dengan banyak variables, maka sebaiknya gunakan XML. Karena, XML lebih baik dalam mengecek error pada data yang kompleks secara efisien dibandingkan JSON. Kemudian, kita menggunakan JSON untuk APIs, aplikasi mobile, storage data, karena JSON dirancang untuk interchange data dan memnawarkan format yang lebih simple dan pasti.

Ada beberapa alasan lain dari mengapa JSON cenderung lebih baik dan lebih populer dibandingkan XML adalah:

- JSON sangat flekksibel sehingga bisa digunakan untuk hampir semua bahasa komputer
- Kemudahan JSON dalam parsing data
- Data modeling yang lebih komprehensif karena struktur JSON yang memfasilitasi enkoding dari data hierarchical
- JSON lebih mudah dibaca oleh manusia karena tidak menggunakan tags seperti pada XML
- JSON memiliki file size yang lebih kecil dibandingkan XML
- JSON memiliki transimisi data yang lebih cepat dibandingkan XML

Karena hal hal inilah JSON lebih populer untuk dipakai.

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

- method is_valid() adalah method yang digunakan untuk memvalidasi setiap field di form. Selain itu, method is_valid ini juga dibutuhkan agar kita bisa melihat error yang ada pada form Django kita. Terutama disaat adanya data eksternal yang akan diinput ke platform kita. Apabila tidak ada is_valid maka bisa saja data yang masuk itu tidak aman dan memiliki format yang salah. Selain itu, is_valid juga membantu membuat workflow yang lebih terstruktur.

## 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

- CSRF token di buat oleh Django setiap kali seorang user sedang mengunjungi website kita. Token pada CSRF mengandung forms atau request yang dikirim oleh user dan kemudian di check oleh server apakah request datang dari user yang terpercaya dan bukan dari sumber yang membahayakan. Jadi, CSRF token penting untuk dibuat saat membuat form di Django, karena dapat menghindari dari serangan siber yang membahayakan. Apabila kita tidak menambahkan csrf_token pada form Django, maka disaat adanya request dari user seperti submisi form, server website tidak akan menjalankan action yang di request oleh user. 
<br1>
Tidak adanya csrf_token sering dimanfaatkan oleh penyerang. Karena bisa saja ada penyerang yang melakukan berbagai request atau tindakan yang seolah-olah tindakan tersebut berasal dari user aslinya, padahal sebenarnya user aslinya tidak melakukan tindakan tersebut. Beberapa tindakan yang bisa dilakukan oleh penyerang mentransfer dana, mengubah detail akun, atau mengubah pengaturan.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

- Saya memulai dengan mengimplementasi Skeleton sebagai kerangka Views. Disini, saya membuat ``base.html`` yang berisi css untuk design komponen website saya. Kemudian saya mengubah ``settings.py`` dan memodifikasi ``main.html ``saya yang disesuaikan dengan ``base.html``.

- Setelah itu saya delete ``db.sqlite ``saya, memodifikasi file ``models.py`` dengan menambah ``import uuid ``kemudian saya migrate models saya yang telah saya buat di tugas sebelumnya.

- Setelah berhasil migrate models saya, saya mulai membuat form dengan membuat berkas dinamakan ``forms.py`` dengan nama model ``Product`` dan fields nya yang berisi ``name``, ``price``, ``description``, ``stock``, ``rating``. Kemudian saya memodifikasi berkas ``views.py`` dengan ``import django.shortcuts``, ``ProductForm``, dan ``Product``. Setelah itu saya menambah fungsi baru yaitu ``create_gear_entry`` dengan form ``ProductForm`` dan return nya yang sama seperti tutorial.

- Lalu, saya ke ``views.py`` dan memodifikasi fungsi ``show_main`` dengan menulis ``gear_entries = Product.objects.all()`` dan di dalam context menambah ``gear_entries: gear_entries``. Langkah ini dilakukan untuk mengambil seluruh objek di ``Product`` yang tersimpan pada database.



- Saya kemudian modifikasi ``urls.py`` dengan import ``create_gear_entry``. Lalu menambahkan path URL ke dalam variabel urlpatterns seperti ``path('create-gear-entry'``, ``create_gear_entry``, ``name='create_gear_entry'``)

- Lalu saya membuat berkas ``create_gear_entry.html`` pada direktori main/templates dengan isi kode untuk mengisi data produk baru.

- Kemudian saya buka ``main.html`` dan menambahkan kode yang akan menampilkan kumpulan hasil data input di dalam desc-box.

- Disini aplikasi saya sudah ada forms untuk menambah product baru dan hasilnya akan ditampilkan di home page.

- Untuk mengembalikan data dalam bentuk ``xml``, saya buka ``views.py`` untuk import ``HTTPResponse`` dan ``Serializer``. Kemudian saya menambahkan fungsi baru dengan nama ``show_xml`` yang akan meyimpan hasil query dari seluruh data yang ada pada ``Product``. Dan saya juga menambahkan return function yang berupa HttpResponse yang memiliki serilizer yang berfungsi untuk translate objek model menjadi format ``xml``. Kemudian saya import fungsi ``show_xml`` pada ``urls.py`` dan menambahkan path url.

- Untuk mengembalikan data dalam bentuk ``JSON``, saya melakukan alur yang sama seperti sebelumnya saat setting xml, namun bedanya disini fungsinya bernama ``show_json`` dan return type nya ``content_type=“application/json”``. Kemudian saya menambahkan imoort pada ``urls.py`` dan menambahkan path url di url patterns.

 - Untuk mengembalikan data berdasarkan ``ID`` dalam bentuk ``XML`` dan ``JSON``, saya memasuki 2 fungsi baru yang menerima parameter ``request`` dan ``ID`` di ``views.py``. Isi dari fungsi nya seperti yang ada pada tutorial. Kemudian saya menambah import pada ``urls.py`` dan menambahkan path url di url patterns.

 - Sehingga, pada akhirnya ada 5 fungsi baru di ``views.py`` yaitu fungsi ``create_gear_entry``, ``show_xml``, ``show_json``, ``show_xml_by_id``. ``show_json_by_id``, dan path url baru di urlpatterns.

## Screenshot hasil akses URL pada Postman

- ## XML:
![Screenshot 2024-09-17 at 23 53 44](https://github.com/user-attachments/assets/ca0eaf79-0745-4ad4-bccd-252b9d79af0f)

- ## JSON:
![Screenshot 2024-09-17 at 23 54 32](https://github.com/user-attachments/assets/572627aa-f03d-444b-aaf9-dec650491eb3)

- ## XML ID:
![Screenshot 2024-09-17 at 23 55 12](https://github.com/user-attachments/assets/b2eb6bd8-8e80-4ffb-86f0-655b65f2b75b)


- ## JSON ID:
![Screenshot 2024-09-17 at 23 55 40](https://github.com/user-attachments/assets/817f9b40-f14a-483b-8c43-7e751cc71431)

---

## Tugas 4 PBP Farhan Adelio Prayata 2306240162

## 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
- HttpResponseRedirect() hanya mengambil single argumen yaitu URL. Sedangkan redirect() pada akhirnya akan return HttpResponseRedirect, dan dapat menerima model, view, URL sebagai argumen "to".

- Redirect sedikit lebih fleksibel dalam hal ke mana ia bisa "redirect" user.


## 2. Jelaskan cara kerja penghubungan model Product dengan User!

- Adanya ForeignKey. ForeignKey ini akan kita taruh di potongan kode pada model kita sehingga akan menghubungan model Product dengan User. Selain itu, kode akan dilengkapi dengan on_delete=models.CASCADE yang artinya dalah jika User dihapus, maka semua produk yang dimiliki pengguna itu juga akan dihapus. Adanya ForeignKey ini dapat menghubungkan setiap produk ke satu user dan satu pengguna bisa memiliki banyak produk (hubungan many-to-one)

- Menetapkan user yang membuat entri produk baru dengan mengisi field user di model Product dengan pengguna yang sedang login. Hal ini dilakukan dengan modifikasi fungsi create_product_entry. user yang sedang log in bisa membuat entry baru dengan form yang sudah dibuat. Adanya commit=False akan menambahkan informasi user sebelum objek disimpan ke database. Hal ini dilakukan agar kita bisa memodifikasi objek terlebih dahulu sebelum disimpan ke database.

- Pada fungsi show_main akan akan ada product_entries = Product.objects.filter(user=request.user), potongan kode ini berfungsi untuk menampilkan objek pada Product yang berhubungan dengan user yang sedang logged in.

## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

- Authentication akan memverifikasi bahwa pengguna adalah benar - benar siapa yang yang di klaim. Authentication umumnya memasukkan informasi kredensial seperti username dan password. Sedangkan authorization menentukan apa yang diizinkan untuk dilakukan oleh pengguna yang telah di authenticate.<br>
Django mengimplementasikan konsep authentication dengan cara menggunakan sistem built-in untuk login, logout, dan register. DJango akan memverifikasi kredensial (username dan password) dan membandingkannya dengan data yang ada di database. Apabila cocok, user akan diberikan session ID untuk melacak status login mereka.<br>
Setelah itu, pada proses authorization, Django akan menentukan apa yang dapat dilakukan oleh user tersebut berdasarkan dengan izin yang sudah ditetapkan diawal, contohnya @login_required

## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

- Django mengingat pengguna yang telah login dengan Session ID yang disimpan sebagai cookie. Session merupakan suatu token yang mengenali session unik pada aplikasi web tertentu. Session ID yang disimpan di cookies akan dihubungkan dengan data session yang disimpan di server. Akan selalu request dan setiap request berikutnya yang dilakukan oleh pengguna, cookies akan dikirim bersama request http. Django akan memerika cookies untuk mendapatkan session ID kemudian mencari data session di server. Apabila session ID valid dan sesuai dengan data di server, Django akan tahu bahwa pengguna tersebut masih autheticated.<br>
Beberapa kegunaan lain dari cookies adalah cookies menyimpan preferesni pengguna seperti bahasa pilihan, tema pilihan, dan lain - lain. Selain itu, cookies juga bisa digunakan untuk melacak aktivitas pengguna sehingga bisa dimanfaatkan untuk analitik dan pengelolaan iklan.<br>
Namun, tidak semua cookies aman digunakan. Cookies yang kurang aman digunakan diantaranay adalah third-party cookies dan cookies yang tidak dienkripsi dan dikirimkan melalui koneksi http. Ada beberapa cookie yang biasanya dimanfaatkan sehingga seorang hacker bisa impersonate cookie sehingga mereka bisa akses akun user karena cookies tidak menyimpen password. Kejadian ini juga bisa mengarahkan kita kepada beberapa masalahh siber lainnya seperti cross-site scripting dan cross site request forgery.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat fungsi dan form registrasi dengan memodifikasi ``views.py`` dan import formulir bawaan dalam aplikasi web. Kemudian menambahkan fungsi ``register``.

```
from django.forms import ModelForm
from main.models import GearEntry

class GearEntryForm(ModelForm):
    class Meta:
        model = GearEntry
        fields = ["name", "price", "description","stock","rating"]
```

- Membuat berkas ``register.html`` untuk menampilkan laman register dan menambahkan path url di ``urlpatterns``

```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}

```
<br>

```
from django.urls import path
from main.views import show_main, create_gear_entry,show_xml,show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-gear-entry', create_gear_entry, name='create_gear_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]

```




- Setelah itu, saya lanjut membuat fungsi login dengan proses yang sama yaitu import fungsi bawaan django yaitu import ``authenticate``, ``login``, dan ``AuthenticationForm`` pada ``views.py`` . Kemudian, menambahkan fungsi ``login_user``, membuat berkas ``login.html`` untuk membuat template laman untuk login dan melakukan url path untuk laman tersebut.

```
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
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```
<br>

```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>
{% endblock content %}
```

- Saya lanjut dengan membuat fungsi logout dengan import ``logout`` pada ``views.py`` dan menambahkan fungsi ``view.py`` untuk melakukan mekanisme logout. Kemudian, saya memodifikasi berkas ``main.html`` untuk menambahkan hyperlink tag untuk logout. Lalu, saya menambahkan path url di url patterns untuk logout.

```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

- Setelah berhasil membuat form dan fungsi register, login, dan logout, saya lanjut merestriksi akses halaman main dengan import ``login_required``. Saya juga menaruh ``@login_required(login_url='/login')`` agar halaman main hanya dapat diakses oleh pengguna yang sudah login.

```
@login_required(login_url='/login')
```



- Kemudian, saya lanjut setup agar bisa melihat data dari cookies. Hal ini dilakukan dengan menambahkan import ``HttpResponseRedirect``, ``reverse``, dan ``datetime`` pada ``views.py``. Saya juga memodifikasi fungsi ``login_user`` pada blok ``if form.is_valid()`` yang berfungsi untuk melakukan login terlebih dahulu, untuk membuat respose, dan membuat cookie last_login menambahkan ke response. Kemudian saya menambahkan variabel ``'last_login': request.COOKIES['last_login']`` pada context agar kita bisa melihat informasi cookie last_login pada web. Kemudian saya memodifikasi fungsi ``logout_user`` untuk menghapus cookie ``last_login`` saat pengguna melakukan logout. Saya kemudian menambahkan potongan kode ``last_login`` pada ``main.html`` untuk menampilkan informasi cookies di aplikasi web saya.

<br1>

- Untuk menghubungkan Model Product deengan User, saya mulai dengan import User pada models.py Kemudian, pada model Product yang sudah saya buat, saya menambahkan potongan kode seperti user = models.ForeignKey(User, on_delete=models.CASCADE) untuk menghubungkan satu product dengan satu user melalui sebuah relationship, dimana sebuah product pasti terasosiasikan dengan seorang user.

```
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
```

<br1>

- Saya kemudian membuka ```views.py``` dan memodifikasi create_product_entry seperti yang ada pada tutorial. Perubahan ini dilakukan untuk untuk membantu proses penyimpanan objek pada form ke user yang logged in.

```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Gear Entry</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Gear Entry" />
      </td>
      </tr>
    </table>
    </form>

{% endblock %}
```

<br1>

- Kemudian saya ubah value product_entries agar aplikasi hanya menambilkan objek Product yang terasosiakan dengan pengguna yang sedang login dan modifikasi pada context yaitu 'name': request.user.username, untuk menampilakn nama user yang sedang logged in

```
        'name': request.user.username,
```

- Setelah itu, saya makemigrations dan migratesesuai.

- Terakhir, saya buka ```settings.py``` untuk import os dan mengubah variabel DEBUG menjadi

```PRODUCTION = os.getenv("PRODUCTION", False) DEBUG = not PRODUCTION```

---

## Tugas 5 PBP Farhan Adelio Prayata 2306240162

## 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Dalam web developmentm terdapat istilah yang dinamakan CSS specificity. Terdapat beberapa cara untuk mengkalkulasi CSS specificity yaitu menggunakan selektor dan menggunakan decimal number system. Bagi CSS selector, urutan prioritasnya adalah (Prioritas tertinggi-rendah):

- ```!important``` rule. ```!important``` Rule akan mengesampingkan aturan lainnya termasuk inline style.
- Inline Style (Atribut ```style``) Style yang digunakan langsung pada elemen HTML menggunakana tribut style memiliki prioritas lebih tinggi daripada semua selector CSS.
- ID Selector (#) ID ini diterapkan pada elemen yang memiliki atribut ```id```
- Class selector ```(.)```. Class selector merupakan elemen yang memiliki atribut ```class```. Class selector memiliki prioritas yang lebih tinggi daripada selector elemen
- Element Type Selector: Elemen ini mengacu pada tag HTML seperti ```div```, ```p```, ```h1```, dan lain lain.
- Universal Selector ```(*)```
- Pseudo-Class Selector ```(:)```. Selector ini diaplikasikan pada elemen dalam kondisi spesifik seperti ```:hover```, ```:active``` , ```:nth-child()```
- Attribute Selector ```([])``` Selector ini berdasarkan atribut elemen HTML, seperti ```[type="text"]``` atau ```[href]```

## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Design yang responsive telah menjadi konsep yang penting dalam pengembangan aplikasi web karena alasan - alasan berikut:

- User Experience yang Baik. User experience yang baik sangat penting, terutama jika aplikasi web digunakan sebagai alat pemasaran. Dengan desain yang responsif dan tampilan yang optimal di setiap perangkat, pengalaman brand akan meningkat, yang pada akhirnya meningkatkan reputasi dan daya tarik.
- Low Maintenance. Dulu, kita harus membuat versi berbeda untuk setiap perangkat. Dengan desain responsif, satu situs dapat menyesuaikan tampilannya di semua perangkat, sehingga lebih mudah dikelola.
- Loading time yang lebih cepat. 53% pengguna meninggalkan situs jika memuat lebih dari tiga detik. Desain responsif hanya memuat sumber daya yang diperlukan, membuat situs lebih cepat tanpa perlu pengalihan ke versi lain.
- Beragamnya devices di masa kini. Zaman sekarang, aplikasi web sering di akses dari berbagai perangkat mulai dari handphone, laptop, tv, dan lain - lain. Oleh karena itu, design aplikasi web yang responsive menjadi sangat penting agar pengguna menjadi lebih nyaman dalam mengakses suatu aplikasi web.
<br>
- Contoh aplikasi yang SUDA menerapkan responsive design: Shopee
- Contoh aplikasi yang BELUM menerapkan responsive design: SIAKng

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

Berikut adalah penjelasan dan contohnya masing - masing:

- Padding
Padding adalah ruang kosong yang berada di antara konten elemen dan batas (border) elemen tersebut. Padding memberikan jarak internal sehingga konten tidak langsung menempel pada border atau tepi elemen.

```
div {
    padding: 20px; /* Memberikan ruang padding 20px di semua sisi */
    padding-top: 10px; /* Hanya memberikan padding di atas */
    padding-right: 15px; /* Hanya memberikan padding di kanan */
    padding-bottom: 10px; /* Hanya memberikan padding di bawah */
    padding-left: 15px; /* Hanya memberikan padding di kiri */
}
```

- Border
Border adalah garis pembatas yang mengelilingi elemen. Border dapat diatur ketebalan, jenis garis (seperti solid, dashed, dotted), dan warnanya. Border membantu dalam membedakan atau menonjolkan elemen pada halaman web.

```
div {
    border: 2px solid black; /* Membuat border setebal 2px, jenis solid, dan berwarna hitam */
    border-top: 3px dashed red; /* Membuat border bagian atas setebal 3px dengan garis putus-putus berwarna merah */
}

```

- Margin
Margin adalah ruang luar yang mengelilingi elemen, digunakan untuk mengatur jarak antara elemen satu dengan elemen lainnya. Margin membantu dalam mengatur tata letak agar elemen tidak terlalu berdekatan.

```
div {
    margin: 20px; /* Memberikan margin 20px di semua sisi */
    margin-top: 10px; /* Hanya memberikan margin di atas */
    margin-right: 15px; /* Hanya memberikan margin di kanan */
    margin-bottom: 10px; /* Hanya memberikan margin di bawah */
    margin-left: 15px; /* Hanya memberikan margin di kiri */
}
```

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- CSS Flexbox adalah tata letak satu dimensi. Ini berguna untuk mengalokasikan dan menyelaraskan ruang di antara item dalam sebuah grid container. Flexbox bekerja dengan berbagai jenis perangkat tampilan dan ukuran layar. Tata letak Flex memudahkan desain dan pembuatan halaman web responsif tanpa menggunakan banyak properti float dan position dalam kode CSS.
<br1>
Sedangkan, CSS Grid Layout adalah sistem tata letak berbasis grid dua dimensi dengan baris dan kolom. Ini berguna untuk membuat tata letak yang lebih kompleks dan terorganisir.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- Awalnya, saya menambahkan Tailwind ke dalam aplikasi dengan mengedit file `base.html`, termasuk menambahkan tag `<meta name="viewport">` dan `<script src="https://cdn.tailwindcss.com">`.
- Selanjutnya, saya menambahkan fitur untuk mengedit produk. Saya memulai dengan mengubah `views.py` dan membuat fungsi `edit_product` yang menerima `request` dan `id` sebagai parameter. Saya juga menambahkan import `reverse` dan `HttpResponseRedirect`.
- Kemudian, saya membuat file `edit_product.html` untuk memungkinkan pengguna mengubah data produk. Desainnya mirip dengan `create_product_entry.html`. Saya juga menambahkan jalur URL baru dalam `urls.py`.
- Saya juga membuat navbar dengan latar belakang putih dalam file `navbar.html`, yang berisi tautan ke halaman seperti "Home, Description, Categories", ucapan selamat datang dengan nama pengguna, dan tombol logout.
- Setelah itu, saya menambahkan fitur navigasi, edit, dan hapus produk. Untuk menangani berkas statis, saya mengonfigurasi `settings.py` dengan menambahkan `whitenoise.middleware.WhiteNoiseMiddleware` di MIDDLEWARE, serta mengatur `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL`.
- Saya juga menambahkan file `global.css` di folder static/css untuk menerapkan desain khusus, dan menghubungkannya dengan `base.html` agar digunakan di seluruh aplikasi.
- Kemudian, saya memperbarui tampilan pada file `login.html`, `register.html`, dan `create_product_entry` dengan menggunakan Tailwind. Pada halaman login, saya menampilkan gambar statis bernama `login-photo.png` di samping kolom login.
- Saya juga membuat file `card_gear.html`, yang menampilkan kartu produk baru untuk setiap entri produk, termasuk tombol untuk mengedit dan menghapus produk.
- Setelah semua berkas HTML selesai, saya akhirnya memodifikasi `main.html` agar dapat mengintegrasikan semua halaman HTML lainnya dengan baik.

## Tugas 6: JavaScript dan AJAX

## 1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web! 

- JavaScript membantu programmer web untuk menambahkan interaksi user dengan web dimana JavaScript sebagai bahasa pemrograman tentunya menyediakan fitur untuk membuat logika yang dapat dibuat sebagai fungsi yang mengatur jalannya interaksi antara user dengan web application. Tanpa adanya JavaScript, programmer web akan sulit untuk membuat fitur interaksi dengan web application karena HTML dan CSS tidak mempunyai fitur logika pemrograman yang dapat diimplementasi ke dalam web application sebagai fitur interaksi.

## 2. Jelaskan fungsi dari penggunaan ```await ``` ketika kita menggunakan ```fetch()```! Apa yang akan terjadi jika kita tidak menggunakan ```await`` ?

- Penggunaan dari ```await``` adalah agar fungsi ```fetch()``` dijalankan sebagai fungsi asinkronus dimana fungsi ```fetch()``` dijalankan tanpa menunggu adanya response dari endpoint yang kita passing sebagai argument dalam fungsi ```fetch()```. Hal ini memungkinkan programmer untuk menjalankan beberapa proses dalam suatu waktu tanpa harus menunggu fungsi fetch() me-return data dari endpoint. Fungsi ```fetch()``` dengan ```await``` akan me-return sebuah object ```Promise``` yang akan berubah menjadi object data ```JSON``` saat fungsi ```fetch()``` menerima response dari web application (endpoint).


## 3. Mengapa kita perlu menggunakan decorator ```csrf_exempt``` pada ```view``` yang akan digunakan untuk AJAX ```POST```? 

- Untuk exclude ```view``` dari pengecekan ```csrf token```, karena saat kita menggunakan AJAX ```POST``` kita tidak bisa memasukkan input ```csrf token``` yang otomatis ter-generate oleh sistem backend dari django karena kita melakukan fetch tidak dari sistem django. Sehingga kita perlu meng-exclude ```view``` tersebut.

## 4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

- Untuk mencegah masuknya data yang dapat mengganggu sistem baik sistem backend maupun frontend. Karena saat kita membersihkan data input pada backend kitaa memastikan bahwa data input tersebut sudah tidak mengandung data yang menyebabkan gangguan pada sistem sebelum kita memasukkan data tersebut ke database dari web application yang kita miliki.


## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- ```AJAX GET```
 Ubahlah kode cards data product agar dapat mendukung AJAX GET. Lakukan pengambilan data product menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
 <br>

  - Untuk mendapatkan data dari product dalam database kita perlu untuk membuat fungsi untuk mengambil data dari url API yang kita punya. untuk mendapatkan url API kita perlu membuat fungsi pada ```views.py``` yang berguna untuk mereturn response dalam bentuk JSON yang berisikan data product pada database sesuai keinginan kita yaitu product yang dimiliki oleh sebueh user. Setelah itu kita perlu mendefinisikan url yang sesuai sebagai url API yang nantinya kita panggil untuk mendapatkan data dari database.

  ```
  def show_json(request):
  data = Product.objects.filter(user=request.user) # memilih data yang dimiliki oleh user
  return HttpResponse(serializers.serialize("json", data), content_type="application/json")
  ```

   - Membuat fungsi untuk mendapatkan data dari database melalui url API yang telah kita definisikan sebelumnya. Hal ini dapat dilakukan dengan membuat fungsi berikut ini pada tag script dalam main.html. Kita menggunakan fungsi async agar kita tidak perlu menunggu response dari url API untuk melanjutkan program yang lain (asinkronus/non-blocking).

```
   async function getProducts(){
    return fetch("{% url 'main:show_json' %}").then((res) => res.json());
}
```

   - Untuk membuat cards yang nantinya dapat membuat data yang kita dapatkan menggunakan AJAX GET kita perlu mengubah yang sebelumnya kita menggunakan card_product.html sekarang kita memerlukan javascript untuk menghandle tampilan dari card product. Hal tersebut dapat kita buat dengan memasukkan kode yang kita miliki di dalam card_product.html ke dalam sebuah fungsi yaitu refreshProduct()

```
async function refreshGearEntries() {
    document.getElementById("gear_entry_cards").innerHTML = "";
    document.getElementById("gear_entry_cards").className = "";
    const gearEntries = await getGearEntries();
    let htmlString = "";
    let classNameString = "";

    if (gearEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'img/empty-cart.png' %}" alt="empty" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada data gear pada EssentialGear.</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        gearEntries.forEach((item) => {
            const name = DOMPurify.sanitize(item.fields.name);
            const description = DOMPurify.sanitize(item.fields.description);
            htmlString += `
            <div class="relative max-w-7xl mx-auto p-6">
              <!-- Content Section -->
              <div class="relative bg-white rounded-lg shadow-lg overflow-hidden">
                
                <!-- Header -->
                <div class="relative p-8">
                  <h3 class="text-4xl font-bold mb-4 text-center">${name}</h3>
                </div>

                <!-- Image Gallery Section with Larger Image -->
                <div class="flex justify-center space-x-8 mb-8">
                  <img src="{% static '/img/cardlogo.png' %}" alt="Shopping Cart Icon" class="w-2/5 h-auto shadow-lg shadow-white">
                </div>
                
                <!-- Main Content -->
                <div class="p-8">
                  <!-- My Gear Section -->
                  <div class="mb-6">
                    <p class="font-bold text-xl mb-2">My Gear</p>
                    <span class="inline-block text-sm font-semibold py-1 px-3 rounded-full bg-brown-200 text-brown-700">${name}</span>
                  </div>

                  <!-- Description Section -->
                  <div class="mb-6">
                    <p class="font-bold text-xl mb-2">Description</p>
                    <p class="text-black text-lg">${description}</p>
                  </div>

                  <!-- Price Section -->
                  <div class="mb-6">
                    <p class="font-bold text-xl mb-2">Price</p>
                    <span class="inline-block py-1 px-3 rounded-full bg-brown-200 text-brown-700">${item.fields.price}</span>
                  </div>
                </div>
                
                <!-- Action Buttons -->
                <div class="absolute top-4 right-4 flex space-x-3">
                  <!-- Edit Button -->
                  <a href="edit-gear/${item.pk}" class="bg-emerald-700 text-black rounded-full p-3 hover:bg-emerald-500 transition duration-300">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M16.862 2.538c.669-.669 1.762-.669 2.431 0l2.169 2.169c.669.669.669 1.762 0 2.431l-11.482 11.48-5.5 1.101a.75.75 0 01-.884-.884l1.102-5.5 11.483-11.481zm-1.122 4.12l-9.462 9.463-.658 3.29 3.29-.659 9.463-9.462-2.633-2.632zm2.21-2.21l-1.097 1.098 2.633 2.632 1.098-1.098-2.634-2.632z" />
                    </svg>
                  </a>
                  
                  <!-- Delete Button -->
                  <a href="delete/${item.pk}" class="bg-red-700 text-white rounded-full p-3 hover:bg-red-500 transition duration-300">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 24 24" fill="currentColor">
                      <path fill-rule="evenodd" d="M5.25 4.5A.75.75 0 016 3.75h12a.75.75 0 010 1.5h-.419l-.579 10.39A3.75 3.75 0 0113.256 19.5h-2.512a3.75 3.75 0 01-3.746-3.86L5.419 4.5H5.25zm3.614 11.898A2.25 2.25 0 0010.744 18h2.512a2.25 2.25 0 002.25-2.32l.575-10.18H8.289l.575 10.18zM9 9.75a.75.75 0 011.5 0v6a.75.75 0 01-1.5 0v-6zm4.5-.75a.75.75 0 00-.75.75v6a.75.75 0 001.5 0v-6a.75.75 0 00-.75-.75z" clip-rule="evenodd" />
                    </svg>
                  </a>
                </div>
              </div>
            </div>
            `;
        });
    }
    document.getElementById("gear_entry_cards").className = classNameString;
    document.getElementById("gear_entry_cards").innerHTML = htmlString;
}
```

- ``AJAX POST``
  - Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan product.
  
  - Membuat button pada main.html dengan menambahkan prop onclick yang berisikan "showModal();". Nantinya fungsi showModal() akan berisikan.

```
function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');
      modal.classList.remove('hidden'); 

```

  - Nantinya element dengan id crudModal akan berisikan modal yang ada kita tampilkan yaitu seperti dibawah ini.

```
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
    <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
    <!-- Modal header -->
      <div class="flex items-center justify-between p-4 border-b rounded-t">
        <h3 class="text-xl font-semibold text-gray-900">
          Add New Gear Entry
        </h3>
        <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
          <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
          </svg>
          <span class="sr-only">Close modal</span>
        </button>
      </div>
      <div class="px-6 py-4 space-y-6 form-style">
        <form id="gearEntryForm">
          <div class="mb-4">
            <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
            <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-black" placeholder="Enter your Gear" required>
          </div>
          <div class="mb-4">
            <label for="price" class="block text-sm font-medium text-gray-700">Price</label>
            <input type="text" id="price" name="price" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-black" placeholder="price" required>
          </div>
          <div class="mb-4">
            <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
            <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-black" placeholder="description" required></textarea>
          </div>
          <div class="mb-4">
            <label for="stock" class="block text-sm font-medium text-gray-700">Gear stock</label>
            <input type="number" id="stock" name="stock" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-black" required>
          </div>
          <div class="mb-4">
            <label for="rating" class="block text-sm font-medium text-gray-700">Gear rating (1-10)</label>
            <input type="number" id="rating" name="rating" min="1" max="10" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-black" required>
          </div>
          <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
            <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
            <button type="submit" id="submitGearEntry" form="gearEntryForm" class="bg-black hover:bg-slate-500 text-white font-bold py-2 px-4 rounded-lg">Save</button>
          </div>
        </form>
      </div>
    </div>
```

- Buatlah fungsi view baru untuk menambahkan product baru ke dalam basis data. Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.

  - Membuat fungsi pada views.py pada folder main yang berisikan.

```
@csrf_exempt
@require_POST
def add_gear_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    price = strip_tags(request.POST.get("price")) # strip HTML tags!
    description = request.POST.get("description")
    stock = request.POST.get("stock")
    rating = request.POST.get("rating")
    user = request.user


    new_gear = GearEntry(
            name=name, 
            price = price,
            description=description,
            stock=stock,
            rating=rating,
            user = request.user
    )

    new_gear.save()

    return HttpResponse(b"CREATED", status=201)
```

  - Mendefinisikan url pada urls.py dengan menambahkan block kode berikut pada urlpatterns

```
urlpatterns=[
    ...,
    path('create-ajax', create_product_with_ajax, name='create_product_with_ajax'),
]
```

- Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/. Untuk menghubungkan form yang telah dibuat pada modal kita perlu menambahkan fungsi javascript yang digunakan untuk melakukan POST ke dalam server lalu memanggil fungsi refreshProduct() setelah fetch berhasil dilakukan. Nantinya kita perlu menambahkan event listener ke dalam productForm yaitu saat button submit ditekan. Hal ini dapat dilakukan dengan menambahkan fungsi dibawah ini pada tag script di file main.html.

```
function addGearEntry() {
    fetch("{% url 'main:add_gear_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#gearEntryForm')),
    })
    .then(response => refreshGearEntries());

    document.getElementById("gearEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }

  document.getElementById("gearEntryForm").addEventListener("submit", (e) => {
    e.preventDefault();
    addGearEntry();
  })
  ```

- Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar product terbaru tanpa reload halaman utama secara keseluruhan. Kita dapat menambahkan kode dibawah ini untuk membuat fungsi yang berguna untuk merefresh tampilan dari halaman utama

- kita juga perlu memanggil fungsi refreshProduct() setelah kita melakukan submit form product dengan menambahkan

```
fetch("{% url 'main:add_gear_entry_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#gearEntryForm')),
    })
    .then(response => refreshGearEntries());
```