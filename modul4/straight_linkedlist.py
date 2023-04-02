def cariTerkecil(kumpulan):
    n = len(kumpulan)
    terkecil = kumpulan[0]
    for i in range (1,n):
        if kumpulan[i]<terkecil:
            terkecil=kumpulan[i]
    return terkecil
    
a = [2,3,4,5,6,69]
print(a)
print("angka terkecil ",cariTerkecil(a) )

