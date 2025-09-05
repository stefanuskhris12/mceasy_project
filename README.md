Code ini tidak bisa berjalan di docker, karena keterbatasan kemampuan saya tentang docker, maka dari itu saya membuat secara native
Untuk client_app ini juga belum bisa berjalan sesuai dengan ketentuan (hanya bisa melakukan method get)
Untuk odoo app belum bisa menampilkan OWL 

Cara menjalankan code ini:
Untuk client app:
1. Masuk ke file directory client_app melalui terminal (/path_to/projet_mceasy/client_app)
2. Jalankan command "python3 -m venv venv" untuk membuat virtual environment python
3. Jalankan command "source venv/bin/activate" untuk mengaktifkan venv
4. Jalankan command "python3.12 -m pip install -r requirements.txt" untuk menginstall library yang dibutuhkan
   library yang dibutuhkan sudah tertera dalam file requirements.txt
   versi python disesuaikan keinginan (menggunakan python3 juga bisa)
6. Jalankan command "python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000" untuk menjalankan server
   Port bisa diganti sesuai keinginan
7. Jalankan command "curl <host:port>/external/sale/list" untuk melihat list SO
   Jalankan command "curl <host:port>/external/sale/<id>" untuk melihat detail per SO
   Harus dijalankan menggunakan tab terminal lain, biarkan server client_app tetap menyala

Untuk odoo app: (harus ada instance odoo di lokal)
1. Jalankan command "sudo su -s odoo17 -s /bin/bash" jika odoo menggunakan user berbeda
2. Jalankan command "python3.10 /<path_to_odoo>/odoo-bin -c /<path_to>/odoo.conf
   dalam kasus normal, odoo biasanya diinstall di opt/odoo17 dan untuk path directory odoo.conf berada di /project_mceasy/odoo.conf
   contoh command di lokal saya : python3.10 /opt/odoo17/odoo17-server/odoo-bin -c /project_mceasy/odoo.conf
3. Jalankan pada browser <host:port>
   jika sesuai dengan config saya, cukup menjalankan localhost:8017 saja
4. Lalu create new database dengan ketentuan:
   Db name  : mydb
   username : admin
   password : admin
   master password : 2 (jika menggunakan file config saya, jika tidak bisa dilihat pada file config)
   jangan lupa untuk checklist Demo data, supaya ada data dummy yg digenerate otomatis oleh odoo
   lakukan sesuai ketentuan diatas supaya tidak perlu merubah code, karena saya setting secara hardcode/statis pada code
5. Jika sudah membuat db
6. Jika sudah muncul halaman Odoo, login menggunakan username dan password
   Lalu masuk ke menu Apps, install terlebih dahulu modul external_invoice_request dan contacts
7. Masuk ke modul Contacs, lalu ubah tampilan dari kanban ke list dan checlist semua data partner yang ada
   Lalu pada tombol Action, klik Generate Token untuk generate unique token untuk masing-masing partner
8. Lalu ganti url yang ada pada browser dengan "localhost:8017/external/sale/<token>" untuk melihat tampilan OWL

Sementara tahap-tahap untuk testing yang saya kerjakan seperti diatas
Terimakasih dan mohon maaf belum bisa memenuhi ketentuan yang ada 
