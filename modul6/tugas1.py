from mergeSort import mergeSort
from quickSort import *
class MhsTif():
    def __init__(self,nama,jarak,nim,kota,uangsaku) -> None:
        self.nama = nama
        self.nim=nim
        self.jarak =jarak
        self.kota = kota
        self.uangsaku= uangsaku

c0 = MhsTif("ricardo",10,"L200210134",'sukoharjo',369000)
c1 = MhsTif("tatang",30,"L200210132",'klaten',169000)
c2 = MhsTif("milos",40,"L200210131",'sukoharjo',269000)
c3 = MhsTif("ronaldo",30,"l20021033",'boyolali',369000)
c4 = MhsTif("starlord",30,"l200210333",'sukoharjo',469000)
c5 = MhsTif("shinomiya kaguya",25,"L200210136","boyolali",9999999999999)
c6 = MhsTif("nopal",32,"L200210135",'wornogiri',3000)

Daftar=[c0,c1,c2,c3,c4,c5,c6]
nim =[]

for i in Daftar:
    nim.append(i.nim)

#mergeSort(nim)
mergeSort(nim)
print("urutan data setelah di merge sort")
print(nim)
print("-----------------------------")
#reset urutan data
nim = []
for i in Daftar:
    nim.append(i.nim)
#quickSort(nim)
quickSort(nim)
print("urutan data setelah di quick sort")
print(nim)
print("-----------------------------")
print("L200210135_naufal hanief mafaza")

