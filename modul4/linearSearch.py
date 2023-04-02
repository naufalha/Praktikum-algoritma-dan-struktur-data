def cariLurus(wadah ,target):
    n = len(wadah)
    for i in range(n):
        if wadah[i] == target:
            return True
    return False

A =[10,33,22,12,33,42,33,44]
print(cariLurus(A,69))
print(cariLurus(A,22))