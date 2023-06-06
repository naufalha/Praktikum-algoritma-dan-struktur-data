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

def preorder_traversal(subpohon):
    if subpohon is not None:
        print(subpohon.data)
        preorder_traversal(subpohon.kiri)
        preorder_traversal(subpohon.kanan)
preorder_traversal()

#inorder_traversal
def inorder_traversal(subpohon):
    if subpohon is not None:
        inorder_traversal(subpohon.kiri)
        print(subpohon.data)
        inorder_traversal(subpohon.kanan)
        
#preorder_traversal        
def preorder_traversal(subpohon):
    if subpohon is not None:
        print(subpohon.data)
        preorder_traversal(subpohon.kiri)
        preorder_traversal(subpohon.kanan)
        
#postorder_traversal
def postorder_traversal(subpohon):
    if subpohon is not None:
        postorder_traversal(subpohon.kiri)
        postorder_traversal(subpohon.kanan)
        print(subpohon.data)
        
