#mencari nilai terkecil
class MhsTif():
    def __init__(self,nama,jarak,kota,uangsaku) -> None:
        self.nama = nama
        self.jarak =jarak
        self.kota = kota
        self.uangsaku= uangsaku

c0 = MhsTif("ricardo",10,'sukoharjo',369000)
c1 = MhsTif("tatang",30,'klaten',169000)
c2 = MhsTif("milos",40,'sukoharjo',269000)
c3 = MhsTif("ronaldo",30,'boyolali',369000)
c4 = MhsTif("starlord",30,'sukoharjo',469000)
c5 = MhsTif("shinomiya kaguya",25,"boyolali",9999999999999)
c6 = MhsTif("shirogane",'wornogiri',43,3000)
c7 = MhsTif("nopal",'wornogiri',43,3000)
Daftar=[c0,c1,c2,c3,c4,c5,c6,c7]

def KurangDari(kurang):
    smallest = []
    index = 0
    for i in Daftar :
        if i.uangsaku <= kurang:
            smallest.append(index)
        index += 1
    return smallest

print(KurangDari(40000))

print("uang saku kurang dari 25000")
for i in KurangDari(25000):
    print(Daftar[i].nama)

print("_______________________________")
print("l200210135 Naufal Hanief Mafaza")