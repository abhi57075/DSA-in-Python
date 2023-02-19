# Power set -> Set of all subsets
# Ex: {1,2,3} -> {},{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3} -> no of elements are 2^n

def PowerSet(arr, output, index, finalans):
    if index == len(arr):
        finalans.append(output[:])
        return finalans
    
    # Exclude wala case
    PowerSet(arr, output, index + 1, finalans)

    # Include wala case
    element = arr[index]
    output.append(element)
    PowerSet(arr, output, index + 1, finalans)

    #Reset the output list
    output.pop()

    return finalans

l = [1,2,3,4]
output = []
finalans = []
index = 0
print(PowerSet(l, output, index, finalans))
