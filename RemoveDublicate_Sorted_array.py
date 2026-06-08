def removeDuplicates(nums: list[int]) -> int:
    i = 1
    for j in range (1, len(nums)):
        if nums[j] != nums[i-1]:
            nums[i] = nums[j]
            i+=1
    return i

# example input
nums = [1,1,2]
result = removeDuplicates(nums)
print(result)  # Output: 2
print(nums[:result])  # Output: [1, 2]