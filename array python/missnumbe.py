def missingnumbe(list):
    missing = []
    for i in range(1, list[len(list)-1]):
        if i not in list:
            missing.append(i)
    return missing

a = missingnumbe([1,2,3,4,5,6,14,15,16,17,18])

print("missing numbe is ",a)