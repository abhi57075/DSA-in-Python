def check(a,b):
    ans = 1
    for i in range(b):
        ans = ans * a
    return ans

def getNthRoot(m,n):
    low = 1
    high = m
    diff = 10**(-6)
    while (high - low > diff):
        mid = low + (high-low)/2
        if check(mid,n) == m:
            return mid
        elif check(mid,n) < m:
            low = mid-1
        else:
            high = mid+1

a,b = map(int,input().split())
print(getNthRoot(a,b))
    
        