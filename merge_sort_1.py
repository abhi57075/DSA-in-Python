def merge_list(a,b): # returns a single sorted list; here a and b are sorted lists 
    m = len(a)
    n = len(b)
    if m<1: # a is empty list
        return b
    elif n<1: # b is empty list
        return a
    
    result = []
    i = j = 0
    while i<m and j<n:
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    
    while i<m:
        result.append(a[i])
        i+=1
    
    while j<n:
        result.append(b[j])
        j+=1
    
    return result

l1 = [2,4,6,7,9,13,15]
l2 = [3,4,8,90,101,10001]
print(merge_list(l1,l2))