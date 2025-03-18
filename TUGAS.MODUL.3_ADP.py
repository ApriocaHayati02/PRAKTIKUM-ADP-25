print(" "*22,"WELCOME")
print(" "*24,'TO')
print(" "*17 ,"GAME TEBAK ANGKA ")
print(" ")
print("-"*21)
print("|      PEMAIN 1     |")
print("-"*21)
n = int(input('angka bom = '))
a = int(input('batas angka = '))

for i in range(1, a+1):
    if i % n == 0:
        print("BOM", end=" ")
    else:
        print(i, end=" ")

print(" ")
print("-"*21)
print('|     PEMAIN 2      |')
print("-"*21)

p = int(input(f"tebaklah angka dari 1 sampai {a} = "))

while p > a :
    p_baru = int(input('tebak lagi !! pilih angka = '))
    if p_baru < a :
        if p_baru % n == 0 :
            print('ups!! angka ' ,p_baru, ' adalah BOM, anda kalah')
            break
        else:
            print('SELAMAT!! angka ',p_baru, ' bukan BOM, ANDA MENANG!!!')
            break
        
if p <= a :
    if p % n == 0:
        print('ups!! angka ' ,p, ' adalah BOM, anda kalah')
    else:
        print('SELAMAT!! angka ',p, ' bukan BOM, ANDA MENANG!!!')
