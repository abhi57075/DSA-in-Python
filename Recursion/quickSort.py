def partition(l, s, e):
    pivot = l[s]
    count = 0
    for i in range(s, e+1):
        if l[i] <= pivot:
            count += 1
    pivotCorrectIndex = s + count - 1
    l[s], l[pivotCorrectIndex] = l[pivotCorrectIndex], l[s]

    i = s
    j = e
    while i < pivotCorrectIndex and j > pivotCorrectIndex:
        while l[i] < pivot:
            i += 1
        while l[j] > pivot:
            j -= 1
        if i < pivotCorrectIndex and j > pivotCorrectIndex:
            l[i], l[j] = l[j], l[i]

    return pivotCorrectIndex

def quickSort(l, s, e):
    if s >= e:
        return l

    p = partition(l, s, e)

    quickSort(l, s, p-1)
    quickSort(l, p+1, e)
    return l

l = [3,5,8,2,1,-1,7,0,0]
print(quickSort(l, 0, len(l)-1))
