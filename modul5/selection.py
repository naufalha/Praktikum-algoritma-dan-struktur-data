from terkecil import cariPosisiYangTerkecil
from swap import swap
def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexkecil = cariPosisiYangTerkecil(A,i,n)
        if indexkecil !=i:
            swap(A,i,indexkecil)

x=[4,1,25,6,78,5]
selectionSort(x)
print(x)