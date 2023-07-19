def mergeSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_side = data[:mid]
        right_side = data[mid:]
        
        i = 0 ; j =0 ; k =0
        while i < left_side[i] and j < right_side[j]:
            if left_side[i] <  right_side[j]:
                data[k] = left_side[i]
                i += 1
                k += 1
            else:
                data[k] = right_side[j]
                j += 1
                k += 1
        while i < len(left_side):
            data[k] = left_side(i)
            k += 1
            i += 1
            
        while j < len(right_side):
            data[k] = right_side[j]
            j += 1
            k += 1
        
        
kontol=[234,32,4,34,3]
mergeSort(kontol)
print(kontol)