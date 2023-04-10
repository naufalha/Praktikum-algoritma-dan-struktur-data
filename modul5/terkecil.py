def cariPosisiYangTerkecil(A,dariSini,sampaiSini):
    terkecil = dariSini
    for i in range(dariSini+1,sampaiSini):
        if A[i] < A[terkecil]:
            terkecil = i
    return terkecil

