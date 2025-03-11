
nama=input("nama penumpang :")
umur=input("umur           :")
jk=input("jenis kelamin  :")

maskapai=input("kode maskapai  :")

if maskapai=="3012":
    tujuan = 'padang-jakarta'
    kelas=input("jenis maskapai :")
    jp=int(input("jumlah tiket   :"))
    
    if kelas == "ekonomi":
        harga = 800000
        harga2= harga * jp
        diskon = harga2 * 20/100
        total_harga = harga2 - diskon
        if jp > 3:
            print("                   diskon 20% ")
            print("total harga   = Rp.",total_harga)
        else:
            print("total harga   = Rp.",harga2)

    elif kelas == "bisnis":
        harga = 850000
        harga2= harga * jp
        diskon = harga2 * 20/100
        total_harga = harga2 - diskon
        if jp > 3:
            print("                   diskon 20% ")
            print("total harga   = Rp.",total_harga)
        else:
            print("total harga   = Rp.",harga2)


    elif kelas == "first class":
        harga = 900000
        harga2= harga * jp
        diskon = harga2 * 20/100
        total_harga = harga2 - diskon
        if jp > 3:
            print("                   diskon 20% ")
            print("total harga   = Rp.",total_harga)
        else:
            print("total harga   = Rp.",harga2) 
    else:
        harga = 0
        jp = 0
        harga = "-"
        harga2 = "-"

elif maskapai=="4015":
    tujuan = "Padang-Batam"
    kelas=input("jenis maskapai :")
    jp=int(input("jumlah tiket   :"))
    if kelas == "ekonomi":
        harga = 500000
        harga2= harga * jp
        diskon = harga2 * 20/100
        total_harga = harga2 - diskon
        if jp > 3:
            print("                   diskon 20% ")
            print("total harga   = Rp.",total_harga)
        else:
            print("total harga   = Rp.",harga2)

    elif kelas == "bisnis":
        harga = 550000
        harga2= harga * jp
        diskon = harga2 * 20/100
        total_harga = harga2 - diskon
        if jp > 3:
            print("                   diskon 20% ")
            print("total harga   = Rp.",total_harga)
        else:
            print("total harga   = Rp.",harga2)

    elif kelas == "first class":
        harga = 700000
        harga2= harga * jp
        diskon = harga2 * 20/100
        total_harga = harga2 - diskon
        if jp > 3:
            print("                   diskon 20% ")
            print("total harga   = Rp.",total_harga)
        else:
            print("total harga   = Rp.",harga2)
    else:
        harga = 0
        jp = 0
        harga = "-"
        harga2 = "-"

elif maskapai== "4050":
    tujuan = "Padang-Bandung"
    kelas=input("jenis maskapai :")
    jp=int(input("jumlah tiket   :"))
    if kelas == "ekonomi":
        harga = 700000
        harga2= harga * jp
        diskon = harga2 * 20/100
        total_harga = harga2 - diskon
        if jp > 3:
            print("                   diskon 20% ")
            print("total harga   = Rp.",total_harga)
        else:
            print("total harga   = Rp.",harga2)

    elif kelas == "bisnis":
        harga = 750000
        harga2= harga * jp
        diskon = harga2 * 20/100
        total_harga = harga2 - diskon
        if jp > 3:
            print("                   diskon 20% ")
            print("total harga   = Rp.",total_harga)
        else:
            print("total harga   = Rp.",harga2)

    elif kelas == "first class":
        harga = 850000
        harga2= harga * jp
        diskon = harga2 * 20/100
        total_harga = harga2 - diskon
        if jp > 3:
            print("                   diskon 20% ")
            print("total harga   = Rp.",total_harga)
        else:
            print("total harga   = Rp.",harga2) 
    else:
        harga = 0
        jp = 0
        harga = "-"
        harga2 = "-"

else:
    print("jenis maskapai tidak terdaftar")
    tujuan = "-"
    kelas = "-"
    jp = 0
    harga = "-"
    harga2 = "-"


print("----------------------------------")
print(">>>>>>>>>>>>AIR TICKET<<<<<<<<<<<<")
print("----------------------------------")

print("               ")
print("       ~ SELAMAT DATANG ~        ")
print("       KEMANA TUJUAN ANDA?          ")
print("               ")
print("----------------------------------")

print("jenis kelas pada '3012' :")
print("kelas ekonomi     : harga = 800000")
print("kelas bisnis      : harga = 850000")
print("kelas first class : harga = 900000")
print("                  ")
print("jenis kelas pada '4015' :")
print("kelas ekonomi     : harga = 500000")
print("kelas bisnis      : harga = 550000")
print("kelas first class : harga = 700000")
print("                  ")
print("jenis kelas pada '4050' :")
print("kelas ekonomi     : harga = 700000")
print("kelas bisnis      : harga = 750000")
print("kelas first class : harga = 850000")
print("                  ")
print("-----------------------------------")
print("               ")


print("     STRUK PEMBAYARAN     ")
print("1. Nama           : ",nama)
print("2. Umur           : ",umur)
print("3. Jenis kelamin  : ",jk)
print("4. kode maskapai  : ", maskapai)
print('          =======> ', tujuan)
print("5. jenis maskapai : ", kelas)
print("6. jumlah tiket   : ", jp)
if jp > 3 :
    print("7. total harga    : ", total_harga )
else :
    print("7. total harga    : ", harga2 )
print("                                   ")
print("-----------------------------------")

print("               ")
print("     >> Terima kasih",nama,"<<     ")
print(">>> Semoga Perjalananmu Menyenangkan <<<")
print(" >>>>>SELAMAT MENEMPUH PERJALANAN<<<<<")
