def insertSort(A):
    n = len(A)
    for i in range(1,n):
        nilai=A[i]
        pos = i
        while pos>0 and nilai < A[pos-1]:
            A[pos]=A[pos-1]
            pos = pos-1
        A[pos]=nilai


