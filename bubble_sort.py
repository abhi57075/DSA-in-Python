def bubble_sort(l):
    for j in range(0,len(l)):
        check_for_swap = False
        for i in range(0,len(l)-1):
            if l[i]>l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
                check_for_swap = True
        if check_for_swap == False:
            break
    return l

arr = [2,3,6,4,1,9,8,7,0]
print(bubble_sort(arr))