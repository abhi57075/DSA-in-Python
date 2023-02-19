def linearSearch(l, target):
    if len(l)==0:
        return False
    elif l[0] == target:
        return True
    l = l[1:]
    return linearSearch(l, target)

l = [1,2,3]
print(linearSearch(l,4))