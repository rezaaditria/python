print("##   program penghitung discount  ##")
print("____________________________________\n")

def diskon(TotalBelanja):
    if TotalBelanja < 100000:
        Persen = 0  
        print("\nmaaf anda tidak mendapatkan discount")
    elif TotalBelanja <=500000:
        Persen =10/100  
        print("\nselamat, anda mendapatkan discount 10%.") 
    elif TotalBelanja <=1000000:
        Persen =20/100  
        print("\nselamat, anda mendapatkan discount 20%.")
    else:
        Persen =30/100  
        print("\nselamat, anda mendapatkan discount 30%.")

    Diskon = TotalBelanja * Persen
    TotalBayar = TotalBelanja - Diskon

    return TotalBayar


TotalBelanja=(float(input("Total Belanja: Rp.")))
TotalBayar=diskon(TotalBelanja)

print("Total Bayar: Rp.", TotalBayar)