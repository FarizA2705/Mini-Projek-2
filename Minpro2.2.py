list_pasien = [
    {
        "ID": 1,
        "data_tetap": ("Rizky", "Jl. Harapan 4", 23),
        "Penyakit": "Radang Tenggorokan",
        "Diagnosa": "Infeksi Bakteri",
        "Status": "Rawat Jalan"
    },
    {
        "ID": 2,
        "data_tetap": ("Aulia", "Jl. Kusuma 1", 25),
        "Penyakit": "Asam Lambung",
        "Diagnosa": "GERD",
        "Status": "Rawat Inap",
    },
    {
        "ID": 3,
        "data_tetap": ("Agus", "Jl. Pahlawan 6", 40),
        "Penyakit": "Hipertensi",
        "Diagnosa": "Tekanan darah ≥140/90",
        "Status": "Rawat Inap"
    }
]

# Menampilkan Semua Data
def tampilkan_semua():
    print("\nData Pasien")
    for pasien in list_pasien:
        print(f"\nID         :{pasien["ID"]}\nNama       :{pasien["data_tetap"][0]}\nAlamat     :{pasien["data_tetap"][1]}\nUmur       :{pasien["data_tetap"][2]}\nPenyakit   :{pasien["Penyakit"]}\nDiagnosa   :{pasien["Diagnosa"]}\nStatus     :{pasien["Status"]}")

# Password Manager Dan Karyawan
data = {
    "karyawan": {"Password": "User123", "role": "Karyawan"},
    "admin": {"Password": "Admin123", "role": "Admin"}
}

# Mencari dengan id
def cari_id(id_cari):
    "Mencari pasien berdasarkan ID."
    try:
        id_cari = int(id_cari)
        return next((p for p in list_pasien if p["ID"] == id_cari), None)
    except ValueError:
        return None

# Tambah Pasien
def tambah_pasien():
    try:
        id_baru = max(p["ID"] for p in list_pasien) + 1
        id_baru = 1 
        nama = (input("Nama: ")).strip()
        alamat = (input("Alamat: ")).strip()
        usia = int(input("Usia: "))
        penyakit = input("Penyakit: ").strip()
        diagnosa = input("Diagnosa: ").strip()
        status = input("Status (Rawat Jalan/Rawat Inap): ").strip()

        pasien_baru = {
            "ID": id_baru,
            "data_tetap": (nama,alamat,usia),
            "Penyakit": penyakit,
            "Diagnosa": diagnosa,
            "Status": status 
        }
        list_pasien.append(pasien_baru)
        print("\n== Data pasien berhasil ditambahkan.== ")
    except ValueError:
        print("Input Usia Harus Berupa Angka!")

# Update Data Pasien
def update_data():
    id_update = int(input("Masukkan ID Pasien :"))
    pasien = next((p for p in list_pasien if p["ID"] == id_update), None)
    if pasien is None:
        print("Data Pasien Tidak Di Temukan")
        return
    
    print(f"Data saat ini: Penyakit: {pasien['Penyakit']}, Diagnosa: {pasien['Diagnosa']}, Status: {pasien['Status']}")
    Penyakit_Baru = (input("Masukkan Penyakit Baru: "))
    Diagnosa_Baru = (input("Masukkan Diagnosa Baru: "))
    Status_Baru = (input("Masukkan Status Baru: "))

    if Penyakit_Baru:
        pasien["Penyakit"] = Penyakit_Baru
    if Diagnosa_Baru:
        pasien["Diagnosa"] = Diagnosa_Baru
    if Status_Baru:
        pasien["Status"] = Status_Baru
    print("Data Pasien Berhasil Di Update")

# Menghapus Data Pasien
def hapus_data():
    try:
        id_hapus = input("\nMasukkan ID Pasien yang dihapus: ")
        pasien = cari_id(id_hapus)
        if pasien is None:
            print("Data Pasien Tidak Ditemukan.")
            return

        yakin = input(f"Yakin hapus ID {pasien["ID"]} ({pasien["data_tetap"][0]})? (ya/tidak): ")
        if yakin == 'ya':
            list_pasien.remove(pasien)
            print(f"Data Pasien ID **{pasien["ID"]} Berhasil Dihapus.")
        else:
            print("Pembatalan penghapusan data.")
    except ValueError:
        print("Terjadi kesalahan saat menghapus data: ")

def tampilkan_menu(akses):
    while True:
        if akses == "Admin":
            print("-" * 50)
            print(f"\n==== MENU UTAMA ====")
            print("-" * 50)
            print("1. Tampilkan semua data pasien (READ)")
            print("2. Tambah data pasien (CREATE)")
            print("3. Update data pasien (UPDATE)")
            print("4. Hapus data pasien (DELETE)")
            print("5. Logout")
            print("6. Keluar")
            print("-" * 50)
        
            try:
                menu = int(input("Pilih Menu 1-6: "))
                if menu == 1:
                    tampilkan_semua()
                elif menu == 2:
                    tambah_pasien()
                elif menu == 3:
                    update_data()
                elif menu == 4:
                    hapus_data()
                elif menu == 5:
                    print("Berhasil Log out")
                    break
                elif menu == 6:
                    print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")
                else:
                    print("Pilihan Tidak Valid, Mohon Masukkan Angka 1-6")
            except ValueError:
                print("Hanya Bisa Mneginput Angka")
        
        elif akses == "Karyawan":
            print("-" * 50)
            print(f"==== MENU UTAMA ====")
            print("-" * 50)
            print("1. Tampilkan semua data pasien (READ)")
            print("2. Tambah data pasien (CREATE)")
            print("3. Logout")
            print("4. Keluar")
            print("-" * 50)
            try:
                menu = int(input("Pilih Menu 1-4: "))
                if menu == 1:
                    tampilkan_semua()
                elif menu == 2:
                    tambah_pasien()
                elif menu == 3:
                    print("Berhasil Log out")
                    break
                elif menu == 4:
                    print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")
                else:
                    print("Pilihan Tidak Valid, Mohon Masukkan Angka 1-6")
            except ValueError:
                print("Hanya Bisa Mneginput Angka")


def login_system():
    print("="*40)
    print("  Sistem Informasi Pasien (Klinik)")
    print("="*40)
    
    while True:
        username = input("Username: ").lower().strip()
        password = input("Password: ").strip()
        
        if username in data and data[username]["Password"] == password:
            akses = data[username]["role"]
            print(f"\nLogin Berhasil! Selamat datang, **{akses}**.")
            tampilkan_menu(akses) 
            print("\nSilakan Login Kembali") 
        else:
            print("Username atau Password salah. Coba lagi.")

if __name__ == "__main__":
    login_system()