def insertion_sort(l):
  n = len(l)
  for i in range(1,n):
    j = i
    while l[j-1] > l[j] and j>0:
      l[j-1],l[j] = l[j],l[j-1]
      j-=1
    #print(l)

arr = [2,6,5,4,3,1]
insertion_sort(arr)
print(arr)