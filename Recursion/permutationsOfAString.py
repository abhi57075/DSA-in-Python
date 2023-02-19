def permutations(nums,ans,index):
    if index >= len(nums):
        ans.append(nums)
        return

    for j in range(index,len(nums)):
        nums[index],nums[j] = nums[j],nums[index]
        permuatations(nums,ans,index+1)
        nums[index],nums[j] = nums[j],nums[index] # Backtracking

nums = '123'
ans = []
index = 0
permutations(nums,ans,index)
print(ans)