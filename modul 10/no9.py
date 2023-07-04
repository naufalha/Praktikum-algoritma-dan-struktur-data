import timeit
import time
import matplotlib.pyplot as plt


def carilurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

def tim():
    z=100
    a = [8, 7, 2, 1, 3, 2, 10]
    awal = time.time()
    U = carilurus(a, z)
    akhir=time.time()
    print("Worst case")
    print("mengurutkan %d bilangan, memerlukan %8.7f detik" %(U,akhir-awal))

tim()
###==========No 9b==========
import time
import random
import timeit
import matplotlib.pyplot as plt

def carilurus(wadah, target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

def tim():
    z=100
    a = [8, 7, 2, 1, 3, 2, 10]
    awal = time.time()
    U = carilurus(a, z)
    akhir=time.time()
    print("Worst case")
    print("mengurutkan %d bilangan, memerlukan %8.7f detik" %(U,akhir-awal))

tim()


def a(n):
    z=100
    a = [8, 7, 2, 1, 3, 2, 10]
    U = carilurus(a, n)

def ujia(n):
    ls = []
    jangkauan = range(1, n+1)
    siap = 'from __main__ import a'
    for i in jangkauan:
        t = timeit.timeit('a(' + str(i) + ')', setup = siap, number = 1)
        ls.append(t)
    return ls

n = 10
LS = ujia(n)

plt.plot(LS)
skala = 7700000
plt.plot([x*x/skala for x in range(1, n+1)])
plt.show()