\
class Mahasiswa(Manusia):
    def __init__(self,nama,NIM,kota,us) -> None:
        self.nama = nama
        self.NIM = NIM
        self.kota = kota
        self.uang_saku = us
    def __str__(self) -> str:
        s = self.nama + '\n'+', NIM '+str(self.NIM) +'\n'+ '. Tinggal di' + self.kota +'\n'+ ". Uang saku Rp."+ self.uang_saku+" tiap bulan"
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uang_saku
    def makan(self,s):
        print("saya baru makan ",s,"sambil belajar")
        self.keadaan = "kenyang"
        print(self.keadaan)

