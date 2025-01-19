class ReservasiHotel:
    def _init_(self, nama_tamu, tipe_kamar, durasi_menginap, kolam_renang, status_kamar, status):
        self.nama_tamu = nama_tamu
        self.tipe_kamar = tipe_kamar
        self.durasi_menginap = durasi_menginap
        self.kolam_renang = kolam_renang
        self.status_kamar = status_kamar
        self.status = status


class ManajemenReservasi:
    def _init_(self):
        self.daftar_reservasi = [
            ReservasiHotel("Lee Jeno", "single", 24, "ada", "vip", "check-in"),
            ReservasiHotel("Mark", "single", 10, "tidak ada", "vip", "dipesan"),
            ReservasiHotel("Kim Soo-Hyun", "double", 48, "tidak ada", "vip", "dipesan"),
            ReservasiHotel("Hyun Bin", "suite", 20, "ada", "vip", "check-in"),
            ReservasiHotel("Lee Min-Ho", "double", 96, "ada", "vip", "dipesan"),
            ReservasiHotel("Lee Jong-Suk", "single", 24, "tidak ada", "vip", "check-in"),
            ReservasiHotel("Cha Eun-Woo", "single", 24, "ada", "vip", "check-in"),
            ReservasiHotel("Gong Yoo", "suite", 24, "tidak ada", "vip", "check-in"),
        ]

    def tambah_reservasi(self):
        print("\n=== Tambah Reservasi Baru ===")
        nama_tamu = input("Nama tamu: ")
        tipe_kamar = input("Tipe kamar (double, suite, single): ")
        durasi_menginap = int(input("Durasi menginap (dalam malam): "))
        kolam_renang = input("Apakah kamar memiliki kolam renang? (tidak, ada): ")
        status_kamar = input("Apakah kamar VIP atau biasa? (vip, biasa): ")
        status = input("Status (dipesan, check-in, check-out): ")
        reservasi = ReservasiHotel(nama_tamu, tipe_kamar, durasi_menginap, kolam_renang, status_kamar, status)
        self.daftar_reservasi.append(reservasi)
        print("\nReservasi berhasil ditambahkan!\n")

    def tampilkan_reservasi(self):
        if not self.daftar_reservasi:
            print("\nBelum ada reservasi yang terdaftar.\n")
            return
        print("\n=== Daftar Reservasi ===")
        for i, reservasi in enumerate(self.daftar_reservasi, start=1):
            print(f"{i}. Tamu: {reservasi.nama_tamu} | Kamar: {reservasi.tipe_kamar} | "
                  f"Durasi: {reservasi.durasi_menginap} malam | Kolam Renang: {reservasi.kolam_renang} | "
                  f"Status Kamar: {reservasi.status_kamar} | Status: {reservasi.status}")

    def batalkan_reservasi(self):
        self.tampilkan_reservasi()
        if not self.daftar_reservasi:
            return
        try:
            nomor = int(input("\nMasukkan nomor reservasi yang ingin Anda batalkan: "))
            if 1 <= nomor <= len(self.daftar_reservasi):
                reservasi = self.daftar_reservasi[nomor - 1]
                reservasi.status = "dibatalkan"
                print(f"\nReservasi untuk tamu {reservasi.nama_tamu} berhasil dibatalkan.\n")
            else:
                print("\nNomor reservasi tidak valid.\n")
        except ValueError:
            print("\nMasukkan angka yang valid.\n")

    def ubah_status_reservasi(self):
        self.tampilkan_reservasi()
        if not self.daftar_reservasi:
            return
        try:
            nomor = int(input("\nMasukkan nomor reservasi yang ingin Anda ubah statusnya: "))
            if 1 <= nomor <= len(self.daftar_reservasi):
                reservasi = self.daftar_reservasi[nomor - 1]
                status_baru = input("Masukkan status baru (dipesan, check-in, check-out): ")
                reservasi.status = status_baru
                print(f"\nStatus reservasi untuk tamu {reservasi.nama_tamu} berhasil diubah menjadi {status_baru}.\n")
            else:
                print("\nNomor reservasi tidak valid.\n")
        except ValueError:
            print("\nMasukkan angka yang valid.\n")


def main():
    manajemen = ManajemenReservasi()
    while True:
        print("\n=== Sistem Manajemen Reservasi Hotel ===")
        print("1. Tambah Reservasi")
        print("2. Tampilkan Daftar Reservasi")
        print("3. Batalkan Reservasi")
        print("4. Ubah Status Reservasi")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            manajemen.tambah_reservasi()
        elif pilihan == "2":
            manajemen.tampilkan_reservasi()
        elif pilihan == "3":
            manajemen.batalkan_reservasi()
        elif pilihan == "4":
            manajemen.ubah_status_reservasi()
        elif pilihan == "5":
            print("\nTerima kasih sudah menggunakan sistem ini. Sampai jumpa di lain waktu!\n")
            break
        else:
            print("\nPilihan tidak valid. Mohon coba lagi.\n")


if _name_ == "_main_":
    main()
