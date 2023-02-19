def bs(l,target,start,end):
    mid = start + (end - start)//2
    #print(start,mid,end)
    if start > end:
        return -1
    elif l[mid] == target:
        return mid
    elif l[mid] > target:
        return bs(l,target,0,mid-1)
    else:
        return bs(l,target,mid+1,end)




l = [1,2,3]
target = 9
start = 0
end = len(l)-1
ans = bs(l,target,start,end)
print(ans)