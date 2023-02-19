def merge(a,b): # here a and b should be sorted
    #print(a)
    #print(b)
    m = len(a)
    n = len(b)
    i = j = 0
    result = []
    while i<m and j<n:
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1

    result+=a[i:]
    result+=b[j:]
    #print(result)
    #print("\n")
    return result

def merge_sort(l):
    #print(l)
    if len(l)<=1:
        return l
    else:
        mid  = len(l)//2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        print(left,right)
        return merge(left,right)

a = [6,4,2,5,3,1]
print(merge_sort(a))
