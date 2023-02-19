def PhoneKeypad(digits, output, index, ans, mapping):
    if index >= len(digits):
        ans.append(output)
        return
    
    number = int(digits[index])
    value = mapping[number]

    for i in range(len(value)): 
        output+=value[i]
        PhoneKeypad(digits,output,index+1,ans,mapping)
        output = output[0:len(output)-1]

digits = '23'
ans = []
output = ""
index = 0
mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
PhoneKeypad(digits,output,index,ans,mapping)
print(ans)