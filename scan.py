vocal=['a', 'e', 'i', 'o', 'u']
def jumlahHurufVokal(word):
    sum=[]
    voc=0
    sum.append(len(word))
    for i in word:
        if i.isalpha() and i.lower()  in vocal:
            voc+=1
    sum.append(voc)
    return sum
def jumlahHurufKonsonan(word):
    sum=[]
    voc=0
    sum.append(len(word))
    for i in word:
        if i.isalpha() and i.lower()  not in vocal:
            voc+=1
    sum.append(voc)
    return sum
        

print(jumlahHurufVokal("surakarta"))
print(jumlahHurufKonsonan("surakarta"))
print("--oleh L200210135--")