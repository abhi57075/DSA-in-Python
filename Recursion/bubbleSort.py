def bubbleSort(l,index):
    if index < 0:
        return l
    
    for i in range(index-1):
        if l[i]>l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
    
    return(bubbleSort(l,index-1))


l = [12,34,12,12,54,14]
print(bubbleSort(l,len(l)))
    