class Barang:
    def __init__(self, id_barang, nama_barang, harga):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.harga = harga

class Inventory:
    def __init__(self):
        self.barang_list = []

    def tambah_barang(self, barang):
        self.barang_list.append(barang)
        print("Barang telah ditambahkan.")

    def tampilkan_barang(self):
        if self.barang_list:
            print("Daftar Barang:")
            for barang in self.barang_list:
                print(f"ID: {barang.id_barang}, Nama: {barang.nama_barang}, Harga: {barang.harga}")
        else:
            print("Tidak ada barang dalam inventori.")

    def cari_barang(self, id_barang):
        for barang in self.barang_list:
            if barang.id_barang == id_barang:
                return barang
        return None

    def update_barang(self, id_barang, nama_barang, harga):
        barang = self.cari_barang(id_barang)
        if barang:
            barang.nama_barang = nama_barang
            barang.harga = harga
            print("Barang telah diupdate.")
        else:
            print("Barang tidak ditemukan.")

    def hapus_barang(self, id_barang):
        barang = self.cari_barang(id_barang)
        if barang:
            self.barang_list.remove(barang)
            print("Barang telah dihapus.")
        else:
            print("Barang tidak ditemukan.")

def main():
    inventory = Inventory()

    while True:
        print("\nPilih operasi:")
        print("1. Tambah Barang")
        print("2. Tampilkan Barang")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            id_barang = input("Masukkan ID Barang: ")
            nama_barang = input("Masukkan Nama Barang: ")
            harga = input("Masukkan Harga Barang: ")
            barang = Barang(id_barang, nama_barang, harga)
            inventory.tambah_barang(barang)
        elif pilihan == '2':
            inventory.tampilkan_barang()
        elif pilihan == '3':
            id_barang = input("Masukkan ID Barang yang ingin diupdate: ")
            nama_barang = input("Masukkan Nama Barang baru: ")
            harga = input("Masukkan Harga Barang baru: ")
            inventory.update_barang(id_barang, nama_barang, harga)
        elif pilihan == '4':
            id_barang = input("Masukkan ID Barang yang ingin dihapus: ")
            inventory.hapus_barang(id_barang)
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()