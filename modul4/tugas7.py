def binSe(kumpulan,target):
    low = 0 # dimulai dari elem 0
    high = len(kumpulan)-1
    indexed = []
    while low <= high:
        mid = (high+low)//2
        index = 0
        if kumpulan[mid]==target: ##jika target ada di tengah
            print(mid)
            indexed.append(mid)
        
        elif target < kumpulan[mid]: #mencari apakah kiri
            high = mid - 1
            
        else:
            low = mid + 1 #apakah dikiri 

        
      
   
   
x=[1,2,2,4,5,5,6]
binSe(x,2)