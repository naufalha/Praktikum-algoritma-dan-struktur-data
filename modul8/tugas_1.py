#============Nama = Adnan Shafry Ari Purnama Aji===========#
#=====================NIM = L200170021 ===================#
#=====================Kelas = A ==========================#
#======================MODUL 8============================#

#nomer 1
class stack():
    def __init__(self):
        self.list = []
    def empty(self):
        return len(self.list) == 0
    def __len__(self):
        return len(self.list)
    def push(self, data):
        self.list.append(data)
    def pop(self):
        assert not self.empty(), 'No file'
        return self.list.pop()

def cetakHexa(angka):
    x = stack()

    if angka == 0:
        x.push(0)
    while angka != 0:
        sisa = angka % 16
        angka = angka // 16
        x.push(sisa)
    a = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    hasil = ''
    for i in range(len(x)):
        hasil += str(a[x.pop()])
    return hasil
print("desimal 223 = ",cetakHexa(223),"hexadesimal")

#nomer 2
a = stack()         
for i in range(16): 
    if i % 3 == 0:  
        a.push(i)
        print("push ke -",len(a),"=",a.list)
        
        

#nomer 3
nilai = stack()        
for i in range(16):     
    if i % 3 == 0:      
        nilai.push(i)
        print("langkah pushing ke -",i,",",i,"%3=0",nilai.list)   
    elif i % 4 == 0:    
        nilai.pop() 
        print("langkah popping ke -",i,",",i,"%4=0",nilai.list)    
                        
        
#nomer 4S
class Queue():
    def __init__(self):
        self.qlist = []
    def is_empty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist.pop(0)
    def get_front_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[0]
    def get_rear_most(self):
        assert not self.is_empty(), 'Antrian sedang kosoong'
        return self.qlist[-1]

Y = Queue()
Y.enqueue(30)
Y.enqueue(26)
Y.enqueue(7)
Y.enqueue(18)
Y.enqueue(14)

print(Y.get_front_most(),"(y.get_front_most())")
print(Y.get_rear_most(),"(y.get_rear_most())")
print(Y.qlist)

#nomer 5
