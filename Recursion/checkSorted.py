def check(l,start):
    if start >= len(l)-1:
        return True
    elif l[start]<=l[start+1]:
        return check(l,start+1)
    else:
        return False


l = [1,2,3,4]
print(check(l,0))