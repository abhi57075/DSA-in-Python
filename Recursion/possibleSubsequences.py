def PowerSet(arr, output, index, finalans):
    if index == len(arr):
        finalans.append(output)
        return finalans
    
    # Exclude wala case
    PowerSet(arr, output, index + 1, finalans)

    # Include wala case
    element = arr[index]
    output+=element
    PowerSet(arr, output, index + 1, finalans)

    #print(finalans)

    return finalans

s = 'BIG'
output = ""
finalans = []
index = 0
print(PowerSet(s, output, index, finalans))

