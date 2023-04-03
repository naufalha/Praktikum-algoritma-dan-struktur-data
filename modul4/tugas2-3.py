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

##mencari uang saku terkecil
def smoollest_money(list):
    smallest = list[0]
    index = 0
    for i in list:
        index += 1
        if i.uangsaku < smallest.uangsaku:
            smallest = i
            
    return smallest
print("uang saku terkecil adalah ",smoollest_money(Daftar).nama," hanya Rp.",smoollest_money(Daftar).uangsaku," awokawokwoak")

def listSmollMoney():
    smallest = [0]
    index = 0
    for i in Daftar :
        index += 1
        if i.uangsaku < Daftar[smallest[0]].uangsaku :
            smallest = [index]
        elif i.uangsaku == Daftar[smallest[0]].uangsaku:
            smallest.append(index)
    return smallest

print(listSmollMoney())
print("_______________________________")
print("l200210135 Naufal Hanief Mafaza")