def palindrome(s, ptr1, ptr2):
    if ptr1 > ptr2:
        return True
    elif s[ptr1] != s[ptr2]:
        return False
    ptr1+=1
    ptr2-=1
    return palindrome(s,ptr1,ptr2)

s = 'ghi'
print(palindrome(s,0,len(s)-1))