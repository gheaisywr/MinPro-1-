print("===========================================")
print("Nama: Ghea Aisyah Windraswari")
print("NIM: 2509116022")
print("Prodi : Sistem Informasi (A)")
print("Praktikum : Dasar Dasar Pemrograman")
print("Program: Mini Project 1 ")
print("===========================================")

# Program Sistem Pencatat Password Aplikasi

Menu = ("Tambah Password", "Lihat Password", "Ubah Password", "Hapus Password", "Keluar")
Data_Tersimpan = [
    "Nama Aplikasi: Instagram | Username: gheaisywr | Password: Abc12345", 
    "Nama Aplikasi: Spotify | Username: kambingguling | Password: gatau098", 
    "Nama Aplikasi: YouTube | Username: dasterpink |Password: manasayatau135",
    "Nama Aplikasi: FaceBook | Username: jualbelimusang |Password: aigoo23124",
    "Nama Aplikasi: Twitter | Username: kia.nsantang |Password: yahahahayu00",
    "Nama Aplikasi: Threads | Username: bbiarapaa |Password: biarinaja21",
    "Nama Aplikasi: TikTok | Username: zakit_kepala50 |Password: butuhpertolongan",
    "Nama Aplikasi: TikTok | Username: nemokrasii |Password: 17plusdelapan"
]

print("💻 Hallo! Selamat Datang di Sistem Pencatat Password!")
print("-----Main Menu Sistem Pencatat Password-----")
print("0. Tambah Password")
print("1. Lihat Password")
print("2. Ubah Password")
print("3. Hapus Data")
print("4. Keluar")
print("============================================")
Pilihan = int(input("Silahkan Pilihan Menu (0-4): "))

# Create
if Pilihan == 0:
    print("(Tambah Password)")
    Aplikasi = input("Masukkan Nama Aplikasi: ")
    Username = input("Masukkan Username: ")
    Password = input("Masukkan Password: ")
    print()

    data_baru = f"Nama Aplikasi: {Aplikasi} | Username: {Username} | Password: {Password}"
    Data_Tersimpan.append(data_baru)
    print("-------------------------------------------------")
    print("Yey! Data Password Kamu Berhasil ditambahkan!")
    print("-------------------------------------------------")
    print("Nama Aplikasi: ", Aplikasi)
    print("Username: ", Username)
    print("Password: ", Password)
    print("-------------------------------------------------")  

# Read
elif Pilihan == 1:
    print("(Lihat Password)")
    print("---------- Daftar Password ---------- ")
    print("Data Tersimpan:", Data_Tersimpan[0])
    print("Data Tersimpan:", Data_Tersimpan[1])
    print("Data Tersimpan:", Data_Tersimpan[2])
    print("Data Tersimpan:", Data_Tersimpan[3])
    print("Data Tersimpan:", Data_Tersimpan[4])
    print("Data Tersimpan:", Data_Tersimpan[5])
    print("Data Tersimpan:", Data_Tersimpan[6])
    print("Data Tersimpan:", Data_Tersimpan[7])


# Update
elif Pilihan == 2:
    print("(Ubah Password)")
    idx = int(input(f"Pilih Data Untuk Mengubah Password (0-{len(Data_Tersimpan)-1}): "))
    if 0 <= idx < len(Data_Tersimpan):
        Passwpord_Baru = input("Masukkan Password Baru: ")
        Data_Lama = Data_Tersimpan[idx]
        start = Data_Lama.find("Password: ")
        
        if start != -1:
            Password_Lama = Data_Lama[start:].split()[1]

        data_baru = Data_Lama.replace(Password_Lama, Passwpord_Baru, 1)
        Data_Tersimpan[idx] = data_baru
        print("Wow, Kamu Telah Mengubah Password")
        print("Data Terbaru: ", Data_Tersimpan[idx])
        print("1.", Data_Tersimpan[0])
        print("2.", Data_Tersimpan[1])
        print("3.", Data_Tersimpan[2])
        print("4.", Data_Tersimpan[3])
        print("5.", Data_Tersimpan[4])
        print("6.", Data_Tersimpan[5])
        print("7.", Data_Tersimpan[6])
        print("8.", Data_Tersimpan[7])

    else:
        print("Format kamu tidak sesuai! tidak ditemukan kata 'Password:' ")

# Delete
elif Pilihan == 3:
    print("(Hapus Data)")
    idx = int(input(f"Pilih Data Yang Mau Dihapus(0-{len(Data_Tersimpan)-1}): "))
    if 0 <= idx < len(Data_Tersimpan):
        data_dihapus = Data_Tersimpan.pop(idx)
        print(f"Yah.. Kamu Telah Menghapus Data: {data_dihapus}")
        print("1.", Data_Tersimpan[0])
        print("2.", Data_Tersimpan[1])
        print("3.", Data_Tersimpan[2])
        print("4.", Data_Tersimpan[3])
        print("5.", Data_Tersimpan[4])
        print("6.", Data_Tersimpan[5])
        print("7.", Data_Tersimpan[6])


elif Pilihan == 4:
    print("(Keluar)")
    print("Byeeeeeeeeeeeeeeeee!")