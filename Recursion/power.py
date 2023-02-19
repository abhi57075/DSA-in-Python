def power(a,n):
    if n==0:
        return 1
    return a*power(a,n-1)

def POWER(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    ans = POWER(a,b//2)
    if b%2 == 0:
        return ans*ans
    else:
        return a*ans*ans


a = int(input())
n = int(input())
print(POWER(a,n))
    