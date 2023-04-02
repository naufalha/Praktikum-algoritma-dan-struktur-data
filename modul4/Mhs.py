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

Daftar=[c0,c1,c2,c3,c4]

target='boyolali'
for i in Daftar:
    if i.kota == target:
        print(i.nama + " tinggal di "+target)

terkecil = c0
terbesar = c0
kurang = []
lebih = []
for i in Daftar:
    if i.uangsaku < terkecil.uangsaku:
       terkecil=i
    
print("uang saku terkecil ",terkecil.nama ,"Rp.",terkecil.uangsaku)

for i in Daftar:
    if i.uangsaku > terbesar.uangsaku:
       terbesar=i
    
print("uang saku terkecil ",terbesar.nama ,"Rp.",terbesar.uangsaku)

for i in Daftar:
    if i.uangsaku < 250000:
       lebih.append(i.nama)
    
print("uang saku kurang dari 25000 ",lebih)

for i in Daftar:
    if i.uangsaku > 250000:
       kurang.append(i.nama)
    
print("uang saku lebih dari 25000 ",kurang)