class human():
    def __init__(self, nama,age):
        self.nama = nama
        self.age = age
    def getname(self):
        return self.nama
    def getage(self):
        return self.age
    def setname(self,nama):
        self.nama = nama
    def setage(self,nama):
        self.nama = nama

def main():
    ricardo = human("ricardo", 20)
    print(ricardo.getname())
    print(ricardo.getage())

main()