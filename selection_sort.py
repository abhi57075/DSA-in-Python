def selection_sort(l):
  n = len(l)
  if n < 2:
    return l
  for i in range(n):
    for j in range(i+1,n):
      if l[j] < l[i]:
        l[i],l[j]=l[j],l[i]
    #print(l)
  return l
l = [3,6,4,5,1,2]
print(selection_sort(l))
