import csv
data = []
with open('data.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        colomn1 = row[0]
        colomn2 = row[1]
        data.append(colomn1)
        




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

        
        
kontol = [2,423,43,31,23,123123,213,213,12,3123,123,12,312,31231,23,123,2,231312,231,3,123,123,1,23]
print(mergeSort(kontol))