# Mini-Projek-2
Fariz Aufarizky, 2509116004, Sistem Informasi A, Praktikum Dasar-Dasar Pemrograman

<img width="954" height="652" alt="Screenshot 2025-09-28 201601" src="https://github.com/user-attachments/assets/40cc24d4-6ec0-482c-bf85-983f20e07394" />
Ini adalah variabel global list_pasien, yaitu daftar list atau (dictionary) untuk menampung seluruh data pasien, ini merupakan data pasien dimana kata kunci sepeerti ID, penyakit, nama, dan lain-lain, dan juga nama, alamat dan usia tidak bisa di ubah atau bisa di sebut tuple (data tidak dapat di ubah)

<img width="2023" height="186" alt="Screenshot 2025-09-28 203201" src="https://github.com/user-attachments/assets/8de513bf-2577-45e3-ac7b-8b1c5fd78d1b" />
definisikan sebagai fungsi list, untuk memanggil data yang ada di list_pasien, kemudian melakukan perulangan untuk setiap data pasien, dan print di gunakan untuk memanggil atau mencetak data pasien dari dictionary menggunakan(...{pasien["ID"]} dan bisa juga mengakses data tuple (...{pasien[data_tetap]}[0]]) untuk memanggil nama, alamat dan usia

<img width="938" height="666" alt="Screenshot 2025-09-28 203907" src="https://github.com/user-attachments/assets/36dd74b2-13e4-473c-915d-082bd7b03316" />
ini program untuk menambahkan data pasien, def sendiri di definiskan sebagai fungsi untuk menambahkan data pasien baru,dan untuk id_baru = max(p["ID"] for p in list_pasien) + 1	untuk menghitung ID baru dengan mencari nilai ID maks yang sudah ada, dan ditambah 1. dan untuk list_pasien.append(pasien_baru) berfungsi untuk menambahkan data pasien baru ke dictionary

<img width="1581" height="598" alt="Screenshot 2025-09-28 205315" src="https://github.com/user-attachments/assets/a4d5c081-850f-487f-b352-c22ea4b32040" />
definisikan fungsi untuk mengubah data penyakit, diagnosa, dan status pasien, meminta ID pasien yang ingin diubah data nya. Jika pasien tidak ditemukan, proses akan dihentikan (return). lalu admin diminta untuk menginput data baru dari data pasien yang lama. Memeriksa apakah pengguna mengisi input (bukan string kosong). Jika diisi, nilai kunci "Penyakit" di dictionary pasien akan diupdate.

<img width="1218" height="517" alt="Screenshot 2025-09-28 210223" src="https://github.com/user-attachments/assets/ed349866-a848-489f-b130-9dbbe16d6f32" />
def hapus_data():	 berfungsi untuk menghapus data pasien. pasien = cari_id(id_hapus)	Memanggil fungsi cari_id untuk mendapatkan data pasien yang akan dihapus. yakin = input(...)Meminta konfirmasi penghapusan dari pengguna.
if yakin == 'ya': list_pasien.remove(pasien)	Jika pengguna menjawab 'ya', objek pasien dihapus dari list_pasien, dan jika tidak maka akan cetak pembatalan penghapusan data pasien.

<img width="901" height="959" alt="Screenshot 2025-09-28 210604" src="https://github.com/user-attachments/assets/204c280b-b5c5-44ba-bd57-dbc876960e1e" />
sistem ini berfungsi untuk memanggil atau menampilkan menu setiap peran/akses setiap pengguna yang login, memproses Input menerima pilihan pengguna dan memanggil fungsi CRUD (Create, Read, Update, Delete) yang relevan. ketika pengguna memutuskan untuk Log out (kembali ke layar login) atau Keluar (mengakhiri program).

<img width="946" height="475" alt="Screenshot 2025-09-28 214952" src="https://github.com/user-attachments/assets/2a87d682-026a-431c-809a-82efe2aaad08" />
Sistem login disini menggunakan while True agar pengguna dapat login berulang kali, lalu di minta untuk menginput username dan password,akses = data[username]["role"]	Menyimpan peran ("Admin" atau "Karyawan") yang berhasil login.if __name__ == "__main__": login_system()	Bagian ini memastikan bahwa fungsi login_system() hanya akan dieksekusi ketika script dijalankan sebagai program utama.

**OUTPUT CODE**
<img width="2560" height="1600" alt="Screenshot 2025-09-28 220212" src="https://github.com/user-attachments/assets/8ba31b36-1b15-44ea-829d-60b25b43cc89" />
<img width="2560" height="1600" alt="Screenshot 2025-09-28 220343" src="https://github.com/user-attachments/assets/2863cee2-800f-4f58-a0f6-a6109306cc22" />
<img width="2560" height="1600" alt="Screenshot 2025-09-28 220414" src="https://github.com/user-attachments/assets/874357a1-52d6-4e9f-8708-67158055d642" />
<img width="2560" height="1600" alt="Screenshot 2025-09-28 220428" src="https://github.com/user-attachments/assets/d21a8c1f-b4ac-4bc8-a907-34a129965f20" />
<img width="2560" height="1600" alt="Screenshot 2025-09-28 220428" src="https://github.com/user-attachments/assets/0c70e6aa-831a-411c-bcc4-1493a1d9563c" />
<img width="2560" height="1600" alt="Screenshot 2025-09-28 220515" src="https://github.com/user-attachments/assets/8085851d-f8dc-4974-95dd-401ad27d6941" />

**FLOWCHART**
<img width="1915" height="1148" alt="Screenshot 2025-09-28 200125" src="https://github.com/user-attachments/assets/a20a6f48-f1dd-482b-8397-5dff460e2828" />
Sistem dimulai dengan login kemudian, user menginput Username dan Password, kemudian decision apakah user valid apa tidak, jika ya maka akan di arah kan ke decision selanjutnya yaitu apakah kamu admin apa bukan, jika ya akan di tampilkan berbagai menu yang bisa di akses dan admin memiliki akses penuh, Seperti Create, Read, update, Delete. tidak seperti admin karyawan hanya bisa mengakses beberapa menu saja seperti, menmbahkan data pasien, dan menampilkan seluruh data pasien, tidak seperti keluar log out itu tidak akan mengakhiri program tetapi akan kembali ke bagian login, kalau keluar itu berfungsi untuk mengakhiri program 
