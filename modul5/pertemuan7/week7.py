##no 1 mencari index dari suatu angka dalam list dengan fungsi
##searchnumber("sebuah list", "angka yang dicari")
def searchnumbe(list, num):
    for i in range(len(list)):
        if num == list[i]:
            return i
    return -1
print(searchnumbe([1,2,3,4,5,6,7], 3))

##no 2 mencari titik tertinggi dari sebuah list yang tidak urut
def hilltop(list):
    highest = 0
    for i in range(len(list)):
        if list[i] > highest:
            highest = i 
    return highest
print(hilltop([1,2,3,4,5,6,7,8,9,10,21,3,2,1,23,3,3,3,5]))
print("___________")
print("naufal hanief mafaza l200210135")