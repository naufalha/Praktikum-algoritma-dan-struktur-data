import csv

data = []
with open('data.csv','r') as file:
    #membuat objek reader
    reader = csv.reader(file)
    
    #perulangan tiap baris pada csv
    for row in reader:
        column1 = row[0]
        column2 = row[1]
        data.append([column1, column2])
   
def mergeSort(A):
   # print("membelah ",A)
    if len(A) > 1:
        mid = len(A)//2
        separuhKiri = A[:mid]
        separuhKanan = A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k] = separuhKiri[i]
                i = i + 1
            else:
                A[k] = separuhKanan[j]
                j = j + 1
            k = k + 1
        while i < len(separuhKiri):
            A[k] = separuhKiri[i]
            i = i + 1
            k = k + 1

        while j < len(separuhKanan):
            A[k]=separuhKanan[j]
            j = j + 1
            k = k + 1
 
    return A

def sortData(data):
    absen = []
    sorted = []
    for i in range(len(data)):
        absen.append(data[i][1])
    absen = mergeSort(absen)
    for i in range(len(data)):
        if absen[i] in data[i]:
            sorted.append(data[i])
    return sorted
print(sortData(data))
      
    
        