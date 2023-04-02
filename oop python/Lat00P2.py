class Pesan(object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakter(self):
            print("kalimatku mempunyai",len(self.teks), 'karakter')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
