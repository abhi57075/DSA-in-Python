import itertools as it
import operator

a = [1,2,3,4]
b = ['a','b','c']
c = zip(a,b)
print(list(c))

d = list(iter("Hello"))
print(d)
print("\n")

for i in it.count(10,5): # 10 is start and 5 is step
    if i == 50:
        break
    else:
        print(i,end=" ")
print("\n")

temp = 0
for i in it.cycle("123"):
    if temp>3:
        break
    else:
        print(i,end = " ")
        temp+=1
print("\n")

val = ['college','education','knowledge']
iter = it.cycle(val)
for i in range(4):
    print(next(iter),end=" ")
print("\n")

print(list(it.repeat('Abhishek',5)))
print("\n")

# Cartesian product
print(list(it.product([1,2,3],repeat = 1))) # 3
print(list(it.product([1,2,3],repeat = 2))) # 3*3
print(list(it.product([1,2,3],repeat = 3))) # 3*3*3
# repetition is there in tuples
print("\n")

print(list(it.product([1,2,3],['a','b','c','d'])))
print("\n")

print(list(it.permutations([3,"python"],1)))
print(list(it.permutations([3,"python"],2)))
print(list(it.permutations([3,"python"],3)))

print(list(it.permutations([1,2,3,4,5],1))) # 5 
print(list(it.permutations([1,2,3,4,5],2))) # 5*4
print(list(it.permutations([1,2,3,4,5],3))) # 5*4*3 
# all values in the tuple will be unique that is no repetition
#print(list(it.permutations([1,2,3,4,5],4)))
#print(list(it.permutations([1,2,3,4,5],5)))
print("\n")

print(list(it.permutations("abcd"))) # 4*3*2
print("\n")

print(list(it.permutations(range(4),1))) # 4 
print(list(it.permutations(range(4),2))) # 4*3
print(list(it.permutations(range(4),3))) # 4*3*2
print(list(it.permutations(range(4),4))) # 4*3*2*1
print("\n")

print(list(it.combinations_with_replacement(range(4),3))) # 4*3*2 - 4
print(list(it.combinations_with_replacement(range(4),2))) # 4*3 - 2
print("\n")

l1 = [1,2,3,4,5]
print(list(it.accumulate(l1)))
print(list(it.accumulate(l1,operator.mul)))
print("\n")

l1 = [(1,2,3),(4,5,6),(7,8,9)]
print(list(it.starmap(max,l1)))
print(list(it.starmap(min,l1)))
print("\n")

print(list(it.zip_longest('Abhishek','college',fillvalue="_")))
print("\n")




