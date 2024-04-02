class daftar_tugas:
    def __init__(self):
        self.daftar_tugas = []
    def tambah_tugas(self, tugas):
        self.daftar_tugas.append(tugas)
        print("Tugas berhasil ditambahkan.")
    def lihat_tugas(self):
        if self.daftar_tugas:
            print("Daftar Tugas:")
            for idx, tugas in enumerate(self.daftar_tugas, start=1):
                print(f"{idx}. {tugas}")
        else:
            print("Belum ada tugas dalam daftar.")
    def edit_tugas(self, tugas_lama, tugas_baru):
        if tugas_lama in self.daftar_tugas:
            index = self.daftar_tugas.index(tugas_lama)
            self.daftar_tugas[index] = tugas_baru
            print("Tugas berhasil diubah.")
        else:
            print("Tugas tidak ditemukan.")
    def hapus_tugas(self, tugas):
        if tugas in self.daftar_tugas:
            self.daftar_tugas.remove(tugas)
            print("Tugas berhasil dihapus.")
        else:
            print("Tugas tidak ditemukan.")
to_do_list = daftar_tugas()
while True:
    print("\nMenu Utama:")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Edit Tugas")
    print("4. Hapus Tugas")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")
    if pilihan == "1":
        tugas = input("Masukkan nama tugas: ")
        to_do_list.tambah_tugas(tugas)
    elif pilihan == "2":
        to_do_list.lihat_tugas()
    elif pilihan == "3":
        tugas_lama = input("Masukkan nama tugas yang ingin diubah: ")
        tugas_baru = input("Masukkan nama tugas baru: ")
        to_do_list.edit_tugas(tugas_lama, tugas_baru)
    elif pilihan == "4":
        tugas = input("Masukkan nama tugas yang ingin dihapus: ")
        to_do_list.hapus_tugas(tugas)
    elif pilihan == "5":
        print("Terima kasih telah menggunakan To-Do List.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
