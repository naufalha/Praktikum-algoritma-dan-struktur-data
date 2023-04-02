class Manusia(object):
    def __init__(self,nama) -> None:
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self,s):
        print("saya baru makan ",s)
        self.keadaan = "kenyang"
    def olahraga(self,k):
        print("saya baru saja latihan ",k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self,n):
        return n*2
    
p1 = Manusia("Ricardo Milos")
p1.ucapkanSalam()
p1.makan("bakso")
print(p1.keadaan)
p1.olahraga("Bersepeda")
print("hasil kali 3 =",p1.mengalikanDenganDua(3))