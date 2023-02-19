def counting(n):
    if n == 1:
        return 1
    print(n)
    return counting(n-1)

n = int(input())
print(counting(n))