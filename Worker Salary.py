print("##   program penghitung Gaji Karyawan  ##")
print("_________________________________________\n\n")


def GajiKaryawan(Nama,golongan,jam):
    upah = 0
    if golongan == 'A':
        upah = 5000 
    elif golongan == 'B':
        upah = 7000 
    elif golongan == 'C':
        upah = 8000  
    elif golongan == 'D':
        upah = 10000  
    else: 
        return "\nGolongan tidak diketahui.\n\t(A/B/C/D)"

    if jam > 48:
        upahplus = (jam - 48) * 4000
    else:
        upahplus = 0

    gaji = jam * upah
    gajitotal = gaji + upahplus
    return f"\n{Nama} menerima upah sebesar Rp. {gajitotal} Per minggu.\n"


Nama=input("Nama Karyawan       : ")
golongan=input("Golongan            : ")
jam=int(input("Jumlah Jam Kerja    : "))

output = GajiKaryawan(Nama,golongan,jam)
print(output)



    
