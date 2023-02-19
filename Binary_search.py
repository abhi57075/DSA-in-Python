def bs_recursion(l,low,high,given):
    if high >= low:
        mid = (high+low)//2
        if l[mid]==given:
            return mid
        elif l[mid]>given:
            return bs_recursion(l,low,mid-1,given)
        else:
            return bs_recursion(l,mid+1,high,given)
    else:
        return -1

def bs(l, given):
    beg = 0 
    end = len(l)-1
    while beg<=end:
        mid = (beg+end)//2
        if l[mid]==given:
            return mid
        elif given < l[mid]:
            end = mid
        else:
            beg = mid + 1
    return -1

l1 = [10,20,30,40,50]
length = len(l1)-1

print(bs_recursion(l1,0,length,10))
print(bs_recursion(l1,0,length,20))
print(bs_recursion(l1,0,length,30))
print(bs_recursion(l1,0,length,40))
print(bs_recursion(l1,0,length,50))
print(bs_recursion(l1,0,length,100))

print(bs(l1,10))
print(bs(l1,20))
print(bs(l1,30))
print(bs(l1,40))
print(bs(l1,50))
print(bs(l1,100))