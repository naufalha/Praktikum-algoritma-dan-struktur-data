from time import time as detak
from random import shuffle as kocok
from bubbleSort import bubbleSort 
from selection import selectionSort
k= range(1,6001)
kocok(k)

u_bub = k[:]
i_sel = k[:]
u_ins = k[:]

aw=detak()
bubbleSort(u_bub)
ak=detak()
pritn('bubble:%g'%(ak-aw))