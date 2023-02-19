'''contents covered
1. create an array using numpy
2. create a zero and a one array
3. use of arange 
4. use of linspace
5. sort array
6. search in a sorted array
7. concatenate an array
8. find dim,size,shape of array
9. use of reshape 
10. use of conditions in an array

'''



import numpy as np
#a = np.array(list(map(int,input().split())))
a = np.array([2,1,2,3,4])
print(a)

b = np.zeros(4) # creates an array of 4 elements all 0's
print(b)

c = np.ones(4) # creates an array of 4 elements all 1's
print(c)

d = np.arange(2,9,2)
print(d)

e = np.linspace(0,10,5, dtype = np.int64) # dtype stands for datatype default is float, give any 5 numbers starting from 0 to 10
print(e)

f = np.sort(a) 
print(f)

g = np.searchsorted(f,2) # search in f(sorted array) the element 2 and return its index
print(g)

l1 = np.array([1,2,3,4])
l2 = np.array([34,43])
h = np.concatenate((l1,l2))
print(h)

i = np.array([[1,2,3],[4,5,6]])
print(i.ndim) # returns number of axis in array
print(i.size) # returns number of elements in array
print(i.shape) # returns rows,columns in form of tuples

j = l1.reshape(2,2)
print(j)

print(a[a%2==0])
print(i[(i>2)])

print(np.nonzero(i<=3)) # nonzero prints indices of elements; here of those elements which are less than equal to 2



