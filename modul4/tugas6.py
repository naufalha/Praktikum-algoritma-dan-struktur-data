def binSe(kumpulan,target):
    low = 0 # dimulai dari elem 0
    high = len(kumpulan)-1
    index = 0
    while low <= high:
        mid = (high+low)//2
        index = 0
        if kumpulan[mid]==target: ##jika target ada di tengah
            index = mid
            print(mid)
            return True
        
        elif target < kumpulan[mid]: #mencari apakah kiri
            high = mid - 1
            
        else:
            low = mid + 1 #apakah dikiri 

    return False
x=[1,2,3,4,5,6,7,8,9]
print(binSe(x,88))
print(binSe(x,3))
        