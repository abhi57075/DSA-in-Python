def total(l,sum):
    if len(l)==0:
        return sum
    sum+=l[0]
    l = l[1:]
    return total(l,sum)

l = [1,2,3,4,5]
print(total(l,0))