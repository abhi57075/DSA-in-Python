def reverse(s,ans):
    if len(s) == 0:
        return ans
    ans += s[-1]
    return reverse(s[0:-1],ans)
     
s = 'Help'
print(reverse(s,""))