from swap import swap

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j]>A[j+1]:
                swap(A,j,j+1)
x = [69,2,1,3,5,66,3]
bubbleSort(x)
print(x)