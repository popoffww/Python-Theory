nums = range(1, 18)
result = sum(nums)

for i in range(1, len(nums) // 2 + 1):
    result += sum(nums[i:-i])
print(result)