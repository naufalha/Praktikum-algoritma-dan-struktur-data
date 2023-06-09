class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None
        
# membuat simpul dan mengisi data
A = _SimpulPohonBiner('Ambarawa')
B = _SimpulPohonBiner('Bantul')
C = _SimpulPohonBiner('Cimahi')
D = _SimpulPohonBiner('Denpasar')
E = _SimpulPohonBiner('Enrekang')
F = _SimpulPohonBiner('Flores')
G = _SimpulPohonBiner('Garut')
H = _SimpulPohonBiner('Halmahera Timur')
I = _SimpulPohonBiner('Indramayu')
J = _SimpulPohonBiner('Jakarta')


# menghubungkan simpul
A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I
xx = [A, B, C, D, E, F, G, H, I, J]
for i in xx:
    print(i.data)


#ukuran pohon biner
def ukuranPohon(akar):
    if akar is None:
        return 0
    else:
        return ukuranPohon(akar.kiri) + 1 + ukuranPohon(akar.kanan)
    
print('ukuran pohon biner   ',ukuranPohon(A))