c = int(input("baris = "))
while c < 4 :
    c = int(input("baris = "))
    if c > 4:
        continue

a = int(input("kolom = "))
while a < 4 :
    a = int(input("kolom = "))
    if a > 4:
        continue

jumlah = 1
print("_"*35)
print(" "*6,"KURSI YANG TERSEDIA")
print("-"*35)
print(" ")
for i in range(1, c+1):
    for j in range(1, a+1):
        print(f"|{jumlah :2}|", end="\t")
        jumlah += 1
    print(" ")
    continue

o = c*a
while True:
    print(" ")
    print("_"*35)
    print("HALO! ADA YANG BISA KAMI BANTU?")
    print(" ")
    print("pilih opsi berikut :")
    print("   1. pesan tiket")
    print("   0. selesai")
    opsi = int(input("Pilih opsi = "))
    print("-"*35)
    print(" ")
    if opsi == 1 :
        no_kursi = set( )
        pesanan = int(input("no. kursi yang dipesan = "))
        if pesanan > o or pesanan == 0:
            print("maaf!! kursi tidak tersedia..")
            break
        elif pesanan in no_kursi :
            print("maaf! tiket sudah terjual")
            break
        else:
            no_kursi.add(pesanan)
            print(f"kursi {pesanan} berhasil di pesan!!")
            print("_"*35)
            print(" "*6,"KURSI YANG TERSEDIA")
            print("-"*35)
        for i in range(1,o+1):
            if i in no_kursi:
                print(f"|{' x':2}|", end="\t")
                if i % a == 0 :
                    print( )
            else:
                print(f"|{i:2}|", end="\t")
                if i % a == 0 :
                    print( )
        print(" ")
        print("!! TERIMAKASIH !!")
    elif opsi == 0 :
        print(" TERIMAKASIH!! SAMPAI JUMPA LAGI!!")
        break
    else:
        print("PERMINTAAN ANDA TIDAK TERSEDIA")
        break