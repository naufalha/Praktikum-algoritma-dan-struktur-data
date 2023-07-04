def ukuranPohon(akar):
    if akar is None:
        return 0
    else:
        return ukuranPohon(akar.kiri) + 1 + ukuranPohon(akar.kanan)