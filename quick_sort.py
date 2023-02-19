def quick_sort(arr,left,right):
	if left<right: # len(arr)>1
		partition_pos = partition(arr,left,right)
		quick_sort(arr,left,partition_pos-1)
		quick_sort(arr,partition_pos+1,right)

def partition(arr,left,right):
	i = left
	j = right - 1
	pivot = arr[right]

	while i<j:
		while i<right and arr[i]<pivot:
			i+=1
		
		while j>left and arr[j]>=pivot:
			j-=1
		
		if i<j:
			arr[i],arr[j] = arr[j],arr[i]
		
	if arr[i]>pivot:
		arr[i],arr[right] = arr[right],arr[i]
	
	return i

arr = [22,11,88,66,55,77,33,44]
quick_sort(arr,0,len(arr)-1)
print(arr)

''' Quick sort principle:

1. Choose pivot element (Usually last or random)
2. Store element less than pivot in left subarray
   Store element more than pivot in right subarray
3. Call quick sort recursively on left subarray
   Call quick sort recursively on left subarray

Example : 22 11 88 66 55 77 33 44

pivot element = 44
i = 22 and j = 33
now i will see elements greater than 44 (pivot) and j will see elements smaller than 44 (pivot)
now i will stop when reaching 88 since it is greater than pivot 
now it is j's turn
since j which is at 33 is lesser than 44 we will swap i and j
now array is 22 11 33 66 55 77 88 44 	i->33; j->88

now i goes to 66 and j goes to 33 

now position of i is greater than position of j 
in such case we swap i and pivot position
now array is 22 11 33 44 55 77 88 66
it means 44 is at correct position in array

now left subarray is 22 11 33
pivot = 33 i = 22 j = 11
now i will be at pivot since 22 and 11 are lesser than pivot
now it is j's turn 
but since i's position is greater than j's position  we will swap i and pivot which will change nothing
so it means 33 is at correct position in the array

now left subarray is 11 22
here pivot = 22 and i = j = 11
if i > pivot swap else do nothing

now the same type of procedure will be followed for right subarray

'''