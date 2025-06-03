def buat_file_inventaris_awal(nama_file):
    with open(nama_file, 'w') as f:
        f.write(
            "9786020321234,Laskar Pelangi,Andrea Hirata,12,70000,85000\n"
            "9789791228001,Bumi,Tere Liye,4,75000,95000\n"
            "9789792259333,Negeri 5 Menara,Ahmad Fuadi,8,75000,90000\n"
            "9786022914311,Mariposa,Luluk HF,9,60000,75000\n"
            "9786022914120,dilan,Pidi Baiq,10,65000,80000\n"
            "9786020338492,Pulang,Tere Liye,18,72000,88000\n"
            "9786020630404,Sabtu Bersama Bapak,Adhitya Mulya,13,66000,88000\n"
            "9786024246964,Perahu Kertas,Dee Lestari,14,80000,95000\n"
            "9786024246946,Hujan,Tere Liye,20,75000,90000\n"
            "9786023851066,Arahkan Langkah,Fiersa Besari,7,72000,90000\n"
        )

def bersihkan_newline(teks):
    hasil = ''
    for huruf in teks:
        if huruf != '\n' and huruf != '\r':
            hasil += huruf
    return hasil

def pecah_data_manual(baris):
    data = []
    teks = ''
    koma_berurutan = False
    for huruf in baris:
        if huruf == ',':
            if not koma_berurutan:
                data.append(teks)
                teks = ''
                koma_berurutan = True
            continue
        if huruf == ' ' and koma_berurutan:
            koma_berurutan = False
            continue
        teks += huruf
        koma_berurutan = False
    data.append(teks)
    return data

def konversi_ke_int(teks):
    angka = 0
    daftar_angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for karakter in teks:
        for i in range(10):
            if karakter == daftar_angka[i]:
                angka = angka * 10 + i
                break
    return angka

def baca_data(nama_file):
    inventaris = []
    with open(nama_file, 'r') as f:
        while True:
            baris = f.readline()
            if baris == '':
                break
            baris_bersih = bersihkan_newline(baris)
            elemen = pecah_data_manual(baris_bersih)
            buku = {
                'ISBN': elemen[0],
                'Judul': elemen[1],
                'Penulis': elemen[2],
                'Stok': konversi_ke_int(elemen[3]),
                'Harga Beli': konversi_ke_int(elemen[4]),
                'Harga Jual': konversi_ke_int(elemen[5])
            }
            inventaris.append(buku)
    return inventaris

def tulis_laporan(inventaris, nama_file):
    with open(nama_file, 'w') as f:
        f.write("ISBN, Judul, Penulis, Stok, Harga Beli, Harga Jual, Potensi Keuntungan\n")
        for buku in inventaris:
            potensi = (buku['Harga Jual'] - buku['Harga Beli']) * buku['Stok']
            buku['Potensi Keuntungan'] = potensi
            f.write(
                buku['ISBN'] + ', ' + buku['Judul'] + ', ' + buku['Penulis'] + ', ' +
                str(buku['Stok']) + ', ' + str(buku['Harga Beli']) + ', ' +
                str(buku['Harga Jual']) + ', ' + str(potensi) + '\n'
            )

def cari_tertinggi(inventaris):
    tertinggi = inventaris[0]
    for buku in inventaris:
        if buku['Potensi Keuntungan'] > tertinggi['Potensi Keuntungan']:
            tertinggi = buku
    return tertinggi

def cari_terendah(inventaris):
    terendah = inventaris[0]
    for buku in inventaris:
        if buku['Potensi Keuntungan'] < terendah['Potensi Keuntungan']:
            terendah = buku
    return terendah

def analisis(inventaris):
    total = 0
    restock = []
    for buku in inventaris:
        total += buku['Stok'] * buku['Harga Beli']
        if buku['Stok'] < 5:
            restock.append(buku)

    tinggi = cari_tertinggi(inventaris)
    rendah = cari_terendah(inventaris)

    print("\n=== ANALISIS INVENTARIS ===")
    print("Total Nilai Inventaris (Harga Beli): Rp" + str(total))
    print("Buku dengan Potensi Keuntungan Tertinggi: " + tinggi['Judul'] + " (Rp" + str(tinggi['Potensi Keuntungan']) + ")")
    print("Buku dengan Potensi Keuntungan Terendah: " + rendah['Judul'] + " (Rp" + str(rendah['Potensi Keuntungan']) + ")")
    print("\nBuku yang perlu restock (stok < 5):")
    for buku in restock:
        print("- " + buku['Judul'] + " (Stok: " + str(buku['Stok']) + ")")

def main():
    nama_file = 'inventaris_buku.txt'
    nama_laporan = 'laporan_inventaris.txt'
    buat_file_inventaris_awal(nama_file)
    inventaris = baca_data(nama_file)
    tulis_laporan(inventaris, nama_laporan)
    analisis(inventaris)

main()
